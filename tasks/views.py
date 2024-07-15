from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task, MongoTask

# Create your views here.
def home(request): 
    task_list = Task.objects.all()
    mongo_tasks = MongoTask.objects.all()
    return render(request, 'index.html', {'tasks': task_list, 'mongo_tasks': mongo_tasks})

def create_task_page(request): 
    return render(request, 'create_task.html')

def edit_task_page(request, task_id): 
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'edit_task.html', {'task': task})

def task_details(request, task_id): 
    response = "You're looking at the results of question %s."
    return HttpResponse(response % task_id)

def create_task(request): 
    if(request.method == 'POST'): 
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on' 
        Task.objects.create(title=title, description=description, is_completed=is_completed)

        return redirect('home')
    return render(request, 'create_task.html')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'
        
        task.title = title
        task.description = description
        task.is_completed = is_completed
        task.save()
        
        return redirect('home')
    
    return render(request, 'edit_task.html', {'task': task})

def delete_task(request, task_id): 
    task = get_object_or_404(Task, pk=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
 
    return redirect('home')

def create_mongo_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed') == 'on'

        mongo_task = MongoTask(
            title=title,
            description=description,
            is_completed=is_completed
        )
        mongo_task.save()

        return redirect('home')
    return render(request, 'create_mongo_task.html')

