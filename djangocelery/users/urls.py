from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('', user_views.register, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='user-login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='user-logout'),
]

#urlpatterns = [path('app/', include(urlpatterns))]