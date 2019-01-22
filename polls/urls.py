from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id/results>/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
	path('register/', views.crate_new_user, name='register'),
	path('users/', views.show_users, name='all_users')
]