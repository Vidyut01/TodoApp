from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Task

from datetime import datetime


@login_required(login_url="/accounts/login/")
def index(request):
    # Get and display users tasks
    username = request.user.username
    tasks = Task.objects.filter(user=username).order_by("-id") # Tasks filter from newest to oldest
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
    # 404s if task doesn't exist of if task is not owned by current user
    task_data = get_object_or_404(Task, pk=task_id, user=request.user.username)

    if request.method == "GET":
        # Get task status
        status = "Due"
        if task_data.done:
            status = "Completed"
        elif task_data.due_date < timezone.now():
            status = "Overdue"

        return render(request, "todo/task.html", {"task_data": task_data, "status": status, "user_name": request.user.username})
    
    # POST method
    result = request.POST

    # Remove task
    if ("rm" in result):
        task_data.delete()

    # Complete/Uncomplete task
    elif ("cmp" in result):
        task_data.done = not task_data.done
        task_data.save()

    return HttpResponseRedirect(reverse("todo:index"))
    

@login_required(login_url="/accounts/login/")
def new(request):
    if request.method == "POST":
        # Validates inputs
        try:
            values = request.POST
            
            # Checks if all fields are filled
            if not (values["task_name"] and values["task_desc"]):
                raise ValueError("Error: Task name or description not filled in. Please Try Again.")
            
            # Checks if name and description fit the size requirments
            if len(values["task_name"]) > 50 or len(values["task_desc"]) > 250:
                raise ValueError("Error: Name or description too long.")

            # Checks id date is valid
            try:
                # Convert html datetime-local string to datetime object
                date_format = "%Y-%m-%dT%H:%M"
                due_date = datetime.strptime(values["due_date"], date_format)
            except ValueError as err:
                raise ValueError("Error: No or Invalid time provided. Please Try Again.") from err
            
            # Checks if due date is before current date
            if due_date < datetime.now():
                raise ValueError("Error: Due date cannot be before the time of creation. Please Try Again.")
            
        # Aborts creating task if constraints are not met
        except ValueError as err:
            return render(request, "todo/new.html", {"message": str(err), "user_name": request.user.username})

        # Create new Task object and save to database
        new_task = Task(
            task_name=values["task_name"],
            task_description=values["task_desc"],
            create_date=timezone.now(),
            due_date=due_date,
            done=False,
            user=request.user.username
            )
        
        new_task.save()
        
        return HttpResponseRedirect(reverse("todo:index"))
    
    # GET method
    return render(request, "todo/new.html", {"message": "", "user_name": request.user.username})

def create_account(request):
    # Redirects user if they are already logged in
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("todo:index"))
    
    if request.method == 'POST':
        value = request.POST
        
        # Validating inputs 
        try:
            # Checks if all fields are present
            if not value["username"] or not value["password"] or not value["password_re"]:
                raise ValueError("Fill all fields")
            user = get_user_model()

            # Checks if username is valid
            if len(value["username"]) < 3 or ' ' in value["username"]:
                raise ValueError("Username must be atleast 3 characters long and can't contain spaces")
            
            # Checks if username already exists
            if user.objects.filter(username=value["username"]).exists():
                raise ValueError("Error: Username already exists")
            
            # Checks length of the password
            if len(value['password']) < 8:
                raise ValueError("Password must be at least 8 characters long")

            # Validates password
            has_upper = False
            has_num = False
            for i in value["password"]:
                if i.isupper():
                    has_upper = True
                elif i.isdigit():
                    has_num = True
            if not (has_upper and has_num):
                raise ValueError("Password must contain a uppercase letter and a number")
            
            # Checks if re-entered password is the same
            if value["password"] != value["password_re"]:
                raise ValueError("Error: passwords do not match")
            
            # Create new User object and save to database
            u = user.objects.create_user(username=value["username"], password=value["password"])
            u.save()

            return HttpResponseRedirect(reverse("todo:index"))
                
        # Aborts creating user if constraints are not met
        except ValueError as err:
            return render(request, "todo/create_account.html", {"message": str(err)})
    
    # GET method
    else:
        return render(request, "todo/create_account.html")
