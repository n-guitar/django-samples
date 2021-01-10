from django.shortcuts import render, redirect
from .models import Todo

def list_page(request):
    object_list = Todo.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def create_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        memo = request.POST['memo']
        Todo.objects.create(title=title, memo=memo)
        return redirect('list')
    return render(request, 'create.html')

def update_page(request, pk):
    if request.method == 'POST':
        title = request.POST['title']
        memo = request.POST['memo']
        Todo.objects.filter(pk=pk).update(title=title, memo=memo)
        return redirect('list')
    object = Todo.objects.get(pk=pk)
    return render(request, 'update.html', {'object':object})

def delete_page(request, pk):
    if request.method == 'POST':
        object = Todo.objects.get(pk=pk)
        object.delete()
        return redirect('list')
    object = Todo.objects.get(pk=pk)
    return render(request, 'delete.html', {'object':object})