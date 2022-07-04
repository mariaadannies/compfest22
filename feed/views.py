from ast import For
from pipes import Template
from django.views.generic import TemplateView, DetailView, FormView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posted'] = Post.objects.all().order_by('created_time', 'name')

        return context

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        new_post = Post.objects.create(
            name = form.cleaned_data['name'],
            image = form.cleaned_data['image'],
            desc = form.cleaned_data['desc'],
            price = form.cleaned_data['price'],
        )
        print("YEAAAAAAAAYYYYY")
        return super().form_valid(form)

class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('autho')