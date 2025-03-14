from django.urls import path
from .views import home_page, logout_page, login_page, faculty_create

urlpatterns = [
    path('', home_page, name='home_page'),
    path('logout/', logout_page, name='logout_page'),
    path('login/', login_page, name='login_page'),

    path('faculty_create/', faculty_create, name='faculty_create'),

]
