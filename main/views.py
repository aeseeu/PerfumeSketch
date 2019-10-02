from django.shortcuts import render
from .models import Post
# Create your views here.
def main(request):
    p = Post.objects.all()
    context={'p' : p}
    return render(request, 'main/home.html', context)