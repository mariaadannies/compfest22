from ast import For
from pipes import Template
from django.views.generic import TemplateView, DetailView, FormView, DeleteView
from .forms import PostForm
from .models import Post
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
        print("okay")
        return super().form_valid(form)

# class BalanceBoxView(TemplateView):
#     template_name = "balance.html"

#     def get_context_data(self, **kwargs):

#         balance = 0.00

#         context = super().get_context_data(**kwargs)

#         context['posted'] = Post.objects.all().order_by('-created_time', '-name')

#         return balance

# class AddWithdrawBalanceView(FormView):
#     template_name = "add_withdraw_balance.html"
#     form_class = BalanceForm
#     success_url = "/"

#     def form_valid(self, form):
#         new_post = Post.objects.create(
#             person = form.cleaned_data['person'],
#             add_amount = form.cleaned_data['add'],
#             withdraw_amount = form.cleaned_data['withdraw'],
#         )
#         print("okay")
#         return super().form_valid(form)


class DeletePostView(DeleteView):
    # pst = Post.objects.get(pk=id)
    # pst.delete()
    # return redirect('index')
    template_name = "confirm_buy.html"
    model = Post
    success_url = "/"