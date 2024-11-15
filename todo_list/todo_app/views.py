from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        TodoItem.objects.create(title=title, description=description)
        return redirect('todo_list')
    return render(request, 'add_todo.html')

def delete_todo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return redirect('todo_list')
