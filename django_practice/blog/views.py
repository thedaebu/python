from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # changes default html file url
    context_object_name = 'posts' # changes default object variable name
    ordering = ['-date_posted'] # sorts by model attribute


class PostDetailView(DetailView):
    model = Post


# LoginRequiredMixin requires being logged in or redirects
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # overwrites form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UserPassesTestMixin helps implement validations
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # overwrites form_valid method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # used with UserPassesTestMixin
    def test_func(self):
        post = self.get_object() # gets the current model object
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object() # gets the current model object
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html')
