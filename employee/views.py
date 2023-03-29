from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from employee.models import Task
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'index.html'
    context_object_name = 'task1'
class TaskDetailview(DetailView):
    model=Task
    template_name = 'details.html'
    context_object_name = 'task'
class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','desig','adress')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def add(request):
    task1=Task.objects.all()

    if request.method=='POST':
        name=request.POST.get('task','')
        adress=request.POST.get('adress','')

        task=Task(name=name)
        task.save()

    return  render(request,'index.html',{'task1':task1})
# Create your views here.
# def details(request):
#     return render(request,'details.html',)
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})