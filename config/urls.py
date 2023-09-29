from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('matriculas/', matricula, name='matricula'),
    path('cursos/', curso, name = 'curso'),
    path('instituicao/', instituicao, name = 'instituicao'),
    path('ocupacao/', ocupacao, name = 'ocupacao')
]