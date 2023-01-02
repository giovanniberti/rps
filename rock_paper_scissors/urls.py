from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rock_paper_scissors import views

urlpatterns = [
    path('', views.RockPaperScissorsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
