from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

# Create your views here.
class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 't1'

class detailview(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def index(request):
    tic = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        t1=task(name=name,priority=priority,date=date)
        t1.save()
    return render(request,"home.html",{'t1':tic})

def delete(request,taskid):
    new=task.objects.get(id=taskid)
    if request.method=='POST':
        new.delete()
        return redirect('/')
    return render(request,"delete.html")


def update(request,id):
    new=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=new)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'f':f,'new':new})