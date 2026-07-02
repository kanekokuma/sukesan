from django.shortcuts import render


def index(request):
    return render(request, "quiz/index.html")


def quiz(request):
    return render(request, "quiz/quiz.html")


def correct(request):
    return render(request, "quiz/correct.html")


def wrong(request):
    return render(request, "quiz/wrong.html")
