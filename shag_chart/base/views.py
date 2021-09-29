import random
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, DeleteView
from django.contrib.auth import get_user_model

from .forms import PostForm
from .models import Post

User = get_user_model()


class IndexView(TemplateView):
    template_name = 'base/index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['test_months'] = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                                  'October', 'November', 'December']
        context['test_numbers'] = random.sample(range(1, 30), 12)
        return context

class PostFormView(FormView):
    template_name = 'base/post-create.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)