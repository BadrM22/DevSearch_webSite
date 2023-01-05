from django.shortcuts import render,redirect
from .models import Project
from .forms import ProjectForm



def projects(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    
    return render(request,'projects/projects.html',context=context)

def project(request,pk):
    project_obj = Project.objects.get(id=pk)
    context = {
        'project':project_obj,
    }
    return render(request,'projects/project.html',context=context)

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context=context)

def updateProject(request,pk):
    proj = Project.objects.get(id=pk)
    form = ProjectForm(instance=proj)
    if request.method == 'POST':
        form = ProjectForm(request.POST,instance=proj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context=context)

def deleteProject(request,pk):
    proj = Project.objects.get(id=pk)
    context = {'obj':proj}
    if request.method == 'POST':
        proj.delete()
        return redirect('projects')
    return render(request,'projects/delete-template.html',context=context)