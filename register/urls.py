from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
	path('',views.vote_index,name='vote_index'),
	path('vote_view/',views.vote_view,name='vote_view'),
	path('vote_results/(?P<id>[0-9]+)',views.vote_results,name='vote_results'),
	path('vote/(?P<id>[0-9]+)',views.vote,name='vote'),
	path('details/(?P<id>[0-9]+)',views.details,name='details'),
]