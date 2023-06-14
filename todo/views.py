from django.db import models
from django.shortcuts import render, get_object_or_404

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from datetime import datetime

from .models import Task

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required



# Create your views here.

# def index(request):
#     return render(request, "todo/index.html", {})


# class IndexView(generic.ListView):
#     template_name = "todo/index.html"
#     context_object_name = "tasks"
#     model = Task

@login_required(login_url="/accounts/login/")
def index(request):
    username = request.user.username
    tasks = Task.objects.filter()
    status = {}
    for i in tasks:
        if i.done:
            status[i.id] = "Completed"
        elif i.due_date < timezone.now():
            status[i.id] = "Overdue"
        else:
            status[i.id] = ""
    context = {"tasks": tasks, "user_name": username, "status": status}

    return render(request, "todo/index.html", context)


@login_required(login_url="/accounts/login/")
def task(request, task_id):
    task_data = get_object_or_404(Task, pk=task_id)

    if request.method == "GET":
        status = "Due"

        if task_data.done:
            status = "Completed"
        elif task_data.due_date < timezone.now():
            status = "Overdue"

        return render(request, "todo/task.html", {"task_data": task_data, "status": status, "user_name": request.user.username})
    
    result = request.POST
    if ("rm" in result):
        task_data.delete()
    elif ("cmp" in result):
        task_data.done = not task_data.done
        task_data.save()

    return HttpResponseRedirect(reverse("todo:index"))
    

@login_required(login_url="/accounts/login/")
def new(request):
    if request.method == "POST":
        try:
            values = request.POST
            
            if not (values["task_name"] and values["task_desc"]):
                raise ValueError("Error: Task name or description not filled in. Please Try Again.")
            
            if len(values["task_name"]) > 50 or len(values["task_desc"]) > 250:
                raise ValueError("Error: Name or description too long.")

            try:
                # Convert html datetime-local string to datetime object
                date_format = "%Y-%m-%dT%H:%M"
                due_date = datetime.strptime(values["due_date"], date_format)
            except ValueError as err:
                raise ValueError("Error: No or Invalid time provided. Please Try Again.") from err
            
            if due_date < datetime.now():
                raise ValueError("Error: Due date cannot be before the time of creation. Please Try Again.")
            
        except ValueError as err:
            return render(request, "todo/new.html", {"message": str(err), "user_name": request.user.username})

        new_task = Task(
            task_name=values["task_name"],
            task_description=values["task_desc"],
            create_date=timezone.now(),
            due_date=due_date,
            done=False
            )
        
        new_task.save()
        
        return HttpResponseRedirect(reverse("todo:index"))
    
    return render(request, "todo/new.html", {"message": "", "user_name": request.user.username})

# def login_page(request):
#     if request.method == "POST":
#         user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("todo:index"))
#         else:
#             logout(request)
#             return HttpResponseRedirect(reverse("login"))
#     # use loginview instead
        
#     else:
#         return render(request, "todo/login.html")
    
# @login_required(login_url="/accounts/login/")
# def login_required_test(request):
#     return HttpResponse("Loged in user - " + request.user.username)


def create_account(request):
    if request.method == 'POST':
        value = request.POST
        
        try:
            if not value["username"] or not value["password"] or not value["password_re"]:
                raise ValueError("Fill all fields")
            user = get_user_model()
            
            if user.objects.filter(username=value["username"]).exists():
                raise ValueError("Error: Username already exists")
            
            if value["password"] != value["password_re"]:
                raise ValueError("Error: passwords do not match")
            
            u = user.objects.create_user(username=value["username"], password=value["password"])
            u.save()

            return HttpResponseRedirect(reverse("todo:index"))
                
        except ValueError as err:
            return render(request, "todo/create_account.html", {"message": str(err)})


        
    else:
        return render(request, "todo/create_account.html")
