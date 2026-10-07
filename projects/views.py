from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects, paginateProjects 

def projects(request):
    projects,search_query=searchProjects(request)
    custom_range,projects=paginateProjects(request,projects,6)          

    context = {
    'projects': projects,
    'search_query': search_query,
    'custom_range': custom_range,
    
    }
 
    return render(request,'projects/projects.html',context)

def project(request,pk):   #single project
    projectObj=Project.objects.get(id=pk)
    form=ReviewForm()
    if request.method=='POST':
        form=ReviewForm(request.POST)
        review=form.save(commit=False)
        review.project=projectObj
        review.owner=request.user.profile
        review.save()

        projectObj.getVoteCount
        messages.success(request,'Your Review is Submitted')
        return redirect('project',pk=projectObj.id)



    return render(request,'projects/single-project.html',{'project':projectObj,'form':form,})
      
@login_required(login_url="login")
def createProject(request):
    profile=request.user.profile
    form=ProjectForm() 
    
     #object
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('projects')

    context={'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile=request.user.profile
    projectTBE=profile.project_set.get(id=pk) #we get the project we want to edit or update using this variable then we will pass this insrtance of the project to the form
    form=ProjectForm(instance=projectTBE) 
    
     #object
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=projectTBE)
        if form.is_valid():
            form.save()
            return redirect('account')

    context={'form':form}
    return render(request,'projects/project_form.html',context)


@login_required(login_url="login")
def deleteProject(request,pk):
    profile=request.user.profile
    projectTBD=profile.project_set.get(id=pk)                       #Project is the model the main database containing all the projects to be deleted edited or created :)
    
    if request.method=='POST':
        projectTBD.delete()
        return redirect('projects')
    context={'object':projectTBD}

    return render(request,'delete_template.html',context)