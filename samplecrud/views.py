from django.shortcuts import render
from .models import Todo

def list_page(request):
    object_list = Todo.objects.all()
    return render(request, 'list.html', {'object_list':object_list})

def create_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        memo = request.POST['memo']
    return render(request,'create.html')
