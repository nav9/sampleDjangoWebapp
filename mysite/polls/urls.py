from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

#urlpatterns = [
#    #path('', views.index, name='indexx'),#name does not matter for the URL. Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file
#    # ex: /polls/
#    path('', views.index, name='index'),
#    # ex: /polls/5/
#    path('<int:question_id>/', views.detail, name='detail'),
#    # ex: /polls/5/results/
#    path('<int:question_id>/results/', views.results, name='results'),
#    # ex: /polls/5/vote/
#    path('<int:question_id>/vote/', views.vote, name='vote'),    
#]


