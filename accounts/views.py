"""Passar para CBV"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView
from accounts.models import Usuario, Barbeiro
from django.shortcuts import get_object_or_404
from django.http import Http404


def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('listBarbershops')
    else:
        user_form = UserCreationForm()
    return render(request, 'registro.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listBarbershops')
        else:
            login_view = AuthenticationForm()
    else:
        login_view = AuthenticationForm()
    return render(request, 'login.html', {'login_view': login_view})


def logout_view(request):
    logout(request)
    return redirect('listBarbershops')


class perfilView(DetailView):
    model = Usuario
    template_name = 'perfilUsuario.html'

    def get_object(self):
        tipo_usuario = self.kwargs['user']
        pk = self.kwargs['pk']

        if tipo_usuario == "Barbeiro":
            self.template_name = 'perfilBarbeiro.html'
            return get_object_or_404(Barbeiro, pk=pk)
        elif tipo_usuario == "Usuario":
            self.template_name = 'perfilUsuario.html'
            return get_object_or_404(Usuario, pk=pk)
        else:
            raise Http404("Tipo de usuário não encontrado")
