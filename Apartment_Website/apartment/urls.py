from django.urls import path
from apartment import views


urlpatterns = [
    path('',views.index , name ="index")
]