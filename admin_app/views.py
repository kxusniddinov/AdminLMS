from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Faculty, Chair, Subject, Teacher, Group, Student
from . import services
from .forms import FacultyForm, ChairForm, SubjectForm, StudentForm, GroupForm, TeacherForm


def login_required_decorator(func):
    return login_required(login_url="login_page")


@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, password=password, username=username)
        if user is None:
            login(request, user)
            return redirect("home_page")

    return render(request, "login.html")


@login_required_decorator
def home_page(request):
    faculties = services.get_faculties()
    chairs = services.get_chairs()
    subjects = services.get_subjects()
    teachers = services.get_teachers()
    groups = services.get_groups()
    students = services.get_students()
    ctx = {
        "counts": {
            "faculties": len(faculties),
            "chairs": len(chairs),
            "subjects": len(subjects),
            "teachers": len(teachers),
            "groups": len(groups),
            "students": len(students),
        }
    }
    return render(request, "index.html", ctx)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "faculty_form.html", ctx)