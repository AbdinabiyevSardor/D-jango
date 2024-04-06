from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="hello"),
    path('cours/',views.main1,name="hello"),
    path('text/',views.main2,name="hello"),
    path('talk/',views.main3,name="hello"),
]
