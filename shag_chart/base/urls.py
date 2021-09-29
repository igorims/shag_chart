from django.urls import path

from .views import IndexView, PostFormView, PostDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/create/', PostFormView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]