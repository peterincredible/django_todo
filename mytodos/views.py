from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import MyTodosModel
from datetime import datetime



# Create your views here.
def home(request):
    todos = MyTodosModel.objects.all()
    return render(request,"mytodos/home.html",{"title":"home","todos":todos,"link":"home"})



@login_required(login_url="login")
def addtodo(request):
    if request.method == "POST":
        try:
            if request.FILES["image"] and request.POST["title"] and request.POST["content"] and request.POST["dt"]:
                data = {
                    "title":request.POST["title"],
                    "image": request.FILES["image"],
                    "datetime":request.POST["dt"],
                    "content": request.POST["content"],
                    "user":request.user
                }
                datetime = MyTodosModel(**data)
                datetime.save()
                return redirect("home")
        except:
            print("errrorrr")
            return redirect("addtodo")
    
    else:
        return render(request,"mytodos/addtodo.html",{'title':"addtodo","link":"addtodo"})


def edit(request,todo_key):
    todos = MyTodosModel.objects.get(pk=todo_key)
    if request.method == "POST":
        try:
            if request.POST["title"] and request.POST["content"] and request.POST["dt"] :
                todos.title = request.POST["title"]
                todos.datetime = request.POST["dt"]
                todos.content = request.POST["content"]
                try:
                    if request.FILES["image"]:
                         todos.image.delete(save=False)
                         todos.image = request.FILES["image"]
                         todos.save()
                except:
                    todos.save()

                return redirect("home")
        except:
            print("errrorrr")
            return render(request,"mytodos/edit.html",{"title":"edit","todo":todos})
    
    else:
        return render(request,"mytodos/edit.html",{"title":"edit","todo":todos})

def delete(request,todo_key):
    todos = MyTodosModel.objects.get(pk=todo_key)
    todos.delete()
    return redirect("home")