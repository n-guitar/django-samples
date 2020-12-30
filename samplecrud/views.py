from django.shortcuts import render
from .models import Todo
from django.views import generic
from django.urls import reverse_lazy

class ListPage(generic.ListView):
    model = Todo
    template_name = 'list.html'

class CreatePage(generic.CreateView):
    model = Todo
    template_name = 'create.html'
    fields = ('title','memo')
    success_url = reverse_lazy('list')

class UpdatePage(generic.UpdateView):
    model = Todo
    template_name = 'update.html'
    fields = ('title','memo')
    success_url = reverse_lazy('list')

class DeletePage(generic.DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('list')