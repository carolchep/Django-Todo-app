from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    template_name = "task/home.html"

@login_required
def create_task(request):
    if request.method == 'POST':
      form = TaskForm(request.POST)
      if form.is_valid(): 
        form.save()
        return redirect('/')
    else:
      form = TaskForm()
    return render(request, 'task/create.html', {'form': form})

@login_required
def list_view(request):
    
    Todos = Task.objects.all()
         
return render(request, "list_view.html", {'Todos',Todos})

def detail_view(request, id):
    
    deta = Task.objects.get(id = id)
         
    return render(request, "detail_view.html", {"deta",deta})

     


def update_view(request, id):
    
    obj = get_object_or_404(Task, id = id)
    form = GeeksForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    else:
        form = GeeksForm(request.POST or None, instance = obj)

 
    return render(request, "update_view.html", "form",form)