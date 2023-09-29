from django.db import models

class Cidades(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f'{self.nome} {self.uf}'
    def __str__(self):
        return f'{self.nome} {self.uf}'
    
class Pessoas(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.pai} {self.mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade}'
    
class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nome} {self.site} {self.telefone}'
    
class AreaSaber(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
class Cursos(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.carga_horaria_total} {self.duracao_meses} {self.area_saber} {self.instituicao}'
    
class Matriculas(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()
    def __str__(self):
        return f'{self.instituicao} {self.curso} {self.pessoa} {self.data_inicio} {self.data_previsao_termino}'
    
class Periodos(models.Model):
    periodo = models.CharField()
    def __str__(self):
        return self.periodo
    
class Disciplinas(models.Model):
    nome = models.CharField(max_length=50)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.area_saber}'
    
class Avaliacoes(models.Model):
    descricao = models.CharField(max_length=50)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina}'
    
class Frequencia(models.Model):
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()
    def __str__(self):
        return f'{self.curso} {self.disciplina} {self.numero_faltas}'
    
class Turmas(models.Model):
    nome = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.nome} {self.periodo}'
    
    
class Ocorrencias(models.Model):
    descricao = models.CharField(max_length=50)
    data = models.DateField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.descricao} {self.data} {self.curso} {self. disciplina} {self.pessoa}'
    
class DisciplinaPorCurso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.CharField(max_length=50)
    curso =  models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodos, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome} {self.carga_horaria} {self.curso} {self.periodo}'
    
class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome



