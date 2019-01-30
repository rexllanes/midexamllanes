from django.urls import path
from . import views

app_name = 'votes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:votes_id>/', views.candidate_create, name = 'cancreate'),
    path('<int:votes_id>/update', views.candidate_update, name = 'canupdate'),
    path('<int:votes_id>/create', views.position_create, name = 'poscreate'),
    path('<int:votes_id>/createe', views.candidate_create, name = 'cancreate'),
    path('<int:votes_id>/vote', views.vote, name = 'vote'),

]
