from django.shortcuts import redirect, render, HttpResponse
from .models import TodoTable

# Create your views here.
def home(request):
    todo = TodoTable.objects.all()
    context = {'todos': todo}
    return render(request, 'index.html', context)

def add_todo(request):
    if request.method == "POST":
        todo = request.POST.get("todo")
        if len(todo) >1 :
            t = TodoTable(text = todo)
            t.save()
            # TodoTable.objects.create(text = todo)
    return redirect("/")
    

def update(request, pk):
    todo = TodoTable.objects.get(id=pk)
    context = {
        'todos': todo
        }
    if request.method =='POST':
        new_todo = request.POST.get("update")
        todo.text = new_todo
        todo.save()
        return redirect("/")
    return render(request, 'update.html',context)


def delete(request, pk):
    todo = TodoTable.objects.get(id= pk)
    todo.delete()
    return redirect("/")
