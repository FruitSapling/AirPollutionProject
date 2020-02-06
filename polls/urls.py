from django.urls import path
from . import views

urlpatterns = [
    # path(route, view, kwargs, names)
    # route is the URL string pattern
    # view is the view function, which path() calls with an httprequest object
    # name is
    path('', views.index, name='index'),
    # ex: /polls/5/
    # we send the data in the <> to the view function
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]