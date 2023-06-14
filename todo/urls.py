from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("task/<int:task_id>/", views.task, name="task"),
    path("accounts/create/", views.create_account, name="create_account"),
    #path("login/", views.login_page, name="login"),
    #path("logedin/", views.login_required_test, name="req"),
]
