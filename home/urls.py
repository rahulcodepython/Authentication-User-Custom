from django.urls import path
from home import views

urlpatterns = [

    path('', views.index, name="index"),

    path('login_temp', views.login_temp, name="login_temp"),
    path('login_user', views.login_user, name="login_user"),
    path('register_temp', views.register_temp, name="register_temp"),
    path('register_user', views.register_user, name="register_user"),
    path('logout_user', views.logout_user, name="logout_user"),


    path('admin_panel', views.admin_panel, name="admin_panel"),
    path('profile', views.profile, name="profile"),

]
