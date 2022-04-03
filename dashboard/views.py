from django.shortcuts import render


def dash_aluno(request):
    return render(request, 'dash_aluno/index_aluno.html')

