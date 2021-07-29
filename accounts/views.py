from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from accounts.forms import LoginForm, RegistrationForm


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('posts_list_url'))

        login_form = LoginForm()
        return render(request,'accounts/login.html',context={'login_form':login_form})


    def post(self,request):
        bound_form = LoginForm(request.POST)
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user = authenticate(username= username, password=password)

            if user:
                login(request, user)
                return redirect(reverse('posts_list_url'))

        return render(request,'accounts/login.html',context={'login_form':bound_form})

class RegistrationView(View):
    def get(self, request):
        registration_form = RegistrationForm()
        return render(request, 'accounts/login.html', context={'registration_form': registration_form})


    def post(self, request):
        bound_form = RegistrationForm(request.POST)
        User = get_user_model()
        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            first_name = bound_form.cleaned_data.get('first_name')
            last_name = bound_form.cleaned_data.get('last_name')
            if not User.objects.filter(username=username).exists():
                user=User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name)
                login(request,user)
                return redirect(reverse('posts_list_url'))
        return render(request, 'accounts/registration.html', context={'registration_form': bound_form})



