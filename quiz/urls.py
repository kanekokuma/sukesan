from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("quiz/", views.quiz, name="quiz"),
    path("correct/", views.correct, name="correct"),
    path("wrong/", views.wrong, name="wrong"),
]
