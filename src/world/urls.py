from django.urls import path

from world import views

urlpatterns = [
    path("point/search/", views.WorldBordersPointSearch.as_view())
]
