from django.shortcuts import render
from .models import Project, SocialLink
from django.shortcuts import render, get_object_or_404
from .models import Project

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})
    
def home(request):
    social_links = SocialLink.objects.all()
    return render(request, 'index.html', {
        'social_links': social_links
    })

def projects(request):
    projects = Project.objects.all().order_by('-date_created')
    return render(request, 'projects.html', {
        'projects': projects
    })
