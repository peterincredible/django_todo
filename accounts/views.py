from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == "POST":
        if request.POST["username"] and request.POST["password"]:
            user = auth.authenticate(username=request.POST["username"],password=request.POST["password"])
            if user is not None:
                auth.login(request,user)
                try:
                    if request.session["next"]:
                        print("in post oo",request.session["next"])
                        data = request.session["next"]
                        del request.session["next"]
                        return redirect(data)
                except:
                    return redirect("home")
            else:
                return render(request,"accounts/login.html",{"title":"login","error":" username or password not correct"})
        else:
            return render(request,"accounts/login.html",{"title":"login","error":" username or password field empty"})
    else:
        try:
            if request.GET["next"]:
                request.session["next"] = request.GET["next"]
                return render(request,"accounts/login.html",{"title":"login"})
        except:
            return render(request,"accounts/login.html",{"title":"login"})
            

def signup(request):
    if request.method == "POST":
        if (request.POST["password1"] == request.POST["password2"]) and request.POST["name"] and request.POST["email"] and request.POST["username"]:
            try:
                user = User.objects.get(username= request.POST["username"])
                return render(request,"accounts/signup.html",{"error":"username already exist"})
            except User.DoesNotExist:
                user = {}
                user["username"] = request.POST["username"]
                user["first_name"] = request.POST["name"]
                user["password"] = request.POST["password1"]
                user["email"] = request.POST["email"]
                user = User.objects.create_user(**user)
                user.save()
                auth.login(request,user)
                return redirect("home")
        else:
            return render(request,"accounts/signup.html",{"title":"signup","error":"password might not match or some fild might be empty"})
    else:
        return render(request,"accounts/signup.html",{"title":"signup"})

def logout(request):
    auth.logout(request)
    return redirect("home")