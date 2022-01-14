from django.shortcuts import render
from blog.models import Blog
from project.models import Project
# Create your views here.
def home(request):
    blogs = Blog.objects.order_by('-created_at')
    projects = Project.objects.order_by('-created_at')
    return render(request, 'portfolio/home.html', {'blogs':blogs, 'projects':projects})



