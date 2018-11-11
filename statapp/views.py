from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db.models.functions import datetime
from django.views.generic.edit import FormView

from statapp.forms import ContactForm
from statapp.models import Contact
from untitled1.settings import EMAIL_HOST_USER


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "../contact/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class ContactView(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '../contact/'
    login_url = '../login/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        val = send_mail('test mail', message + '\nSent by ' + email, EMAIL_HOST_USER,
                        [EMAIL_HOST_USER], fail_silently=False)
        if val == 0:
            status = 'unsuccessfully'
        else:
            status = 'successfully'
        contact = Contact(email=email, message=message, status=status, date=datetime.Now())
        contact.save()
        return super(ContactView, self).form_valid(form)
