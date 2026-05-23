from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Album

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        
        # Keep our temporary admin hook logic safe and simple
        # NOTE: Make sure this username matches what you type on the signup page!
        if user.username == 'admin_user':
            user.is_staff = True
            user.is_superuser = True
            
        user.save()
        return super().form_valid(form)


# READ: List albums with strict RBAC isolation
class AlbumListView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'albums/album_list.html'
    context_object_name = 'albums'

    def get_queryset(self):
        """
        Enforce Strict RBAC Query Filtering:
        - If the logged-in user is an administrator/superuser, show ALL assets.
        - Otherwise, isolate the data stream so standard users only see their own content.
        """
        if self.request.user.is_superuser:
            return Album.objects.all()
        return Album.objects.filter(created_by=self.request.user)


# CREATE: Add a new album (Must be logged in)
class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    fields = ['title', 'description', 'cover_image'] 
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def form_valid(self, form):
        # Set the logged-in user as the creator of the album
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# UPDATE: Edit (RBAC Data Interceptor - Blocks URL tampering)
class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    fields = ['title', 'description', 'cover_image']
    template_name = 'albums/album_form.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        # Enforce view execution permission boundaries
        album = self.get_object()
        return self.request.user == album.created_by or self.request.user.is_superuser
    
    def get_queryset(self):
        # Additional database safeguard constraint
        if self.request.user.is_superuser:
            return Album.objects.all()
        return Album.objects.filter(created_by=self.request.user)


# DELETE: Remove album (RBAC Data Interceptor - Blocks URL tampering)
class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'
    success_url = reverse_lazy('album-list')

    def test_func(self):
        # Enforce view execution permission boundaries
        album = self.get_object()
        return self.request.user == album.created_by or self.request.user.is_superuser

    def get_queryset(self):
        # Additional database safeguard constraint
        if self.request.user.is_superuser:
            return Album.objects.all()
        return Album.objects.filter(created_by=self.request.user)