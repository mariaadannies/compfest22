from ast import For
from pipes import Template
from django.forms import Form
from django.views.generic import TemplateView, DetailView, FormView, DeleteView
from .forms import BalanceForm, PostForm
from .models import Balance, Post
from django.http import HttpResponseRedirect

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posted'] = Post.objects.all().order_by('created_time', 'name')

        return context

class HomePageViewDesccendingView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posted'] = Post.objects.all().order_by('-created_time', '-name')

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
        return super().form_valid(form)

class BalanceBoxView(FormView):
    template_name = "balance.html"
    model = Balance
    form_class = BalanceForm

    def form_valid(self, form):
        transc = Balance.objects.create(
            add_amount = form.cleaned_data['add_amount'],
            withdraw_amount = form.cleaned_data['withdraw_amount'],
        )
        return super().form_valid(form)


class DeletePostView(DeleteView):
    # pst = Post.objects.filter(pk)
    # pst.delete()
    # return redirect('index')
    # template_name = "confirm_buy.html"
    model = Post
    success_url = "/"
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)