
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Skill, Category, Contact
from .forms import ContactForm
from django.contrib import messages

def index(request):
    featured = Project.objects.filter(featured=True).order_by('-created_at')[:3]
    recent = Project.objects.all().order_by('-created_at')[:6]
    skills = Skill.objects.all()
    categories = Category.objects.all()
    context = {
        'featured': featured,
        'recent': recent,
        'skills': skills,
        'categories': categories,
    }
    return render(request, 'portfolio/index.html', context)


def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects, 'categories': categories})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    projects = category.projects.all().order_by('-created_at')  # related_name in model
    return render(request, 'portfolio/category_detail.html', {'category': category, 'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks — your message was sent.")
            return redirect('portfolio:contact')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
