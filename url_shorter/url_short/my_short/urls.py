from . import views
from django.urls import path

urlpatterns = [
   path('register/', views.RegisterFormView.as_view()),
   path('login/' ,views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', views.MainView.as_view()),
    path('get_url/', views.save_short_url),
    path(r'<key>',views.redirect_view)
]