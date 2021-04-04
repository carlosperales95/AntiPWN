from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Safe

@login_required
def home(request):
    context = {
        'safes': Safe.objects.all()
    }
    return render(request, 'vaulter/home.html', context)

def about(request):
    return render(request, 'vaulter/about.html', {'title': 'About'})


class SafeListView(ListView):
    model = Safe
    template_name = 'vaulter/home.html'
    context_object_name = 'safes'
    ordering = ['date_modified_last']

class SafeDetailView(DetailView):
    model = Safe

class SafeCreateView(LoginRequiredMixin, CreateView):
    model = Safe
    fields = ['service', 'username', 'email', 'password']

    def form_valid(self, form):
        form.instance.vaulter = self.request.user
        return super().form_valid(form)

class SafeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Safe
    
    fields = ['service', 'username', 'email', 'password']

    def form_valid(self, form):
        #safe = form.save(commit=False)
        #form.instance.password = pbkdf2_sha256.encrypt(form.instance.password, rounds=12000, salt_size=32)
        form.instance.vaulter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.vaulter:
            return True
        return False


class SafeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Safe
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.vaulter:
            return True
        return False
