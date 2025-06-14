from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from .views import RegisterView, email_verification, CustomLoginView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(template_name='users/login.html', success_url='/catalog/product_list/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm')

]