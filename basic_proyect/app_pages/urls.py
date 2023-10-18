from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('pagina1/', views.pagina1, name='pagina1'),
    path('pagina2/', views.pagina2, name='pagina2'),
    path('encuesta/', views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('detalle/<int:question_id>/', views.detail, name='detalle'),
    path('formulario/', views.formulario, name="formulario")
    ]