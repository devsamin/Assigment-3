from django.shortcuts import render,redirect
from Task.forms import TaskForm
from Task.models import TaskModel
# Create your views here.
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showtask')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html' , {'form' : form})

def edit_task(request, id):
    form = TaskModel.objects.get(pk=id)
    EditForm = TaskForm(instance=form)
    print(form.Task_title)
    if request.method == 'POST':
        EditForm = TaskForm(request.POST, instance=form)
        if EditForm.is_valid():
            EditForm.save()
            return redirect('showtask')
    else:
        form = TaskForm()
    return render(request, 'task/add_task.html' , {'form' : EditForm})

def delete_task(request, id):
    form = TaskModel.objects.get(pk=id)
    form.delete()
    return redirect('showtask')
