import random
import secrets
import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, View

from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        verification_link = self.request.build_absolute_uri(
            reverse('users:email-verification', kwargs={'token': token})
        )
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет, перейдите по ссылке для подтверждения почты: {verification_link}',
            from_email='your_email@example.com',
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = ''
    user.save()
    return redirect(reverse('users:login'))


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class PasswordResetView(View):
    def get(self, request):
        return render(request, 'users/password_reset.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = make_password(new_password)
            user.save()
            send_mail(
                'Восстановление пароля',
                f'Ваш новый пароль: {new_password}',
                'your_email@example.com',
                [user.email],
                fail_silently=False,
            )
        return redirect('users:login')
