from django.shortcuts import render,redirect
from tasks.forms import TaskStoreForm,TaskStoreModel

# Create your views here.

def home(request):
    return render(request,'home.html')

def store_task(request):
    if request.method == 'POST':
        task =TaskStoreForm(request.POST) 
        if task.is_valid():
            task.save(commit=True)
            print(task.cleaned_data)
            return redirect('show_task')
    else:
        task =TaskStoreForm() 
    return render(request,'store_task.html',{'form':task})

def show_task(request):
    task = TaskStoreModel.objects.all()
   
    print(task)
    return render(request,'show_task.html',{'data':task})


def edit_task(request, id):
    task = TaskStoreModel.objects.get(pk=id)
    form = TaskStoreForm(instance=task)
    if request.method == 'POST':
        form =TaskStoreForm(request.POST,instance=task) 
        if form.is_valid():
            form.save(commit=True)
            return redirect('show_task')
    return render(request,'store_task.html',{'form':form})


def delete_task(request,id):
    task = TaskStoreModel.objects.get(pk=id).delete()
    return redirect('show_task')

def complete_task(request,id):
    task = TaskStoreModel.objects.get(pk=id).delete()
    return redirect('show_task')


