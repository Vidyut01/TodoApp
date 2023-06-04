from django.db import models
from django.shortcuts import render, get_object_or_404

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Task


# Create your views here.

# def index(request):
#     return render(request, "todo/index.html", {})


class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = "tasks"
    model = Task
    
