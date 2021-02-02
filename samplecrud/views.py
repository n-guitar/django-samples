from django.shortcuts import render
from .models import Todo
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListPage(generic.ListView):
    model = Todo
    template_name = 'list.html'

class CreatePage(LoginRequiredMixin, generic.CreateView):
    model = Todo
    template_name = 'create.html'
    fields = ('title','memo')
    success_url = reverse_lazy('list')

class UpdatePage(LoginRequiredMixin, generic.UpdateView):
    model = Todo
    template_name = 'update.html'
    fields = ('title','memo')
    success_url = reverse_lazy('list')

class DeletePage(LoginRequiredMixin, generic.DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('list')