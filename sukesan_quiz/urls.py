from django.urls import include, path


urlpatterns = [
    path("", include("quiz.urls")),
]
