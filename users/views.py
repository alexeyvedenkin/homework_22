import secrets

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
from .models import CustomUser

from config.settings import EMAIL_HOST_USER


class RegisterView(CreateView):
    model = CustomUser
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения регистрации {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(CustomUser, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'users/login.html'


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile_success')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


class ProfileSuccessView(TemplateView):
    template_name = 'users/profile_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Ваш профиль успешно обновлен!'
        return context


class EditProfileView(View):
    def get(self, request):
        form = UserProfileForm(instance=request.user)  # Предполагая, что у вас есть форма
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request):
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile_success')  # Убедитесь, что используете именование с пространством
        return render(request, 'users/templates/edit_profile.html', {'form': form})