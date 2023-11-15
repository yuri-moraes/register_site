from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Verificar se o usuário já existe
        usuario_existente = Usuario.objects.filter(nome=nome).first()

        if usuario_existente:
            return HttpResponseRedirect(reverse('home'))

        # Se o usuário não existe, criar um novo registro
        novo_usuario = Usuario(nome=nome, idade=idade)
        novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', usuarios)
