from django.shortcuts import render,redirect
from Task.models import TaskModel
# from Category.models import CategoryModel
# Create your views here.
def show_task(request):
    data = TaskModel.objects.all()
    # print(data)
    # for i in data:
    #     print(i)
    #     for j in i.categories.all():
    #         print(j)
    #     print()

    return render(request, 'show_task.html', {'data' : data} )