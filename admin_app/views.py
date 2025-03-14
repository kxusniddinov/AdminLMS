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


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect("faculty_list")
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "faculty/form.html", ctx)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect("faculty_list")


@login_required_decorator
def faculty_list(request):
    faculties = services.get_faculties()
    print(faculties)
    ctx = {
        "faculties": faculties
    }
    return render(request, "faculty/list.html", ctx)


# Chair
@login_required_decorator
def chair_create(request):
    model = Chair()
    form = ChairForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get("actions", [])
        actions += [f"You created chair:"]
        request.session["actions"] = actions

        chair_count = request.session.get("chair_count", 0)
        chair_count += 1
        request.session["chair_count"] = chair_count

        return redirect("chair_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "chair/form.html", ctx)


@login_required_decorator
def chair_edit(request, pk):
    model = Chair.objects.get(pk=pk)
    form = ChairForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get("actions", [])
        actions += [f"You edited chair: "]
        request.session["actions"] = actions

        return redirect("chair_list")

    ctx = {
        "model": model,
        "form": form
    }
    return render(request, "chair/form.html", ctx)


@login_required_decorator
def chair_delete(request, pk):
    model = Chair.objects.get(pk=pk)
    model.delete()
    return redirect("chair_list")


@login_required_decorator
def chair_list(request):
    chairs = services.get_chairs()
    ctx = {
        "chairs": chairs
    }
    return render(request, "chair/list.html", ctx)


# SUBJECT
@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('subject_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'subject/form.html', ctx)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()
    return redirect('subject_list')


@login_required_decorator
def subject_list(request):
    subjects = services.get_subjects()
    ctx = {
        "subjects": subjects
    }
    return render(request, 'subject/list.html', ctx)


# TEACHER
@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        actions = request.session.get('actions', [])
        actions += [f"You added teacher: {request.POST.get('first_name')}"]
        request.session["actions"] = actions

        return redirect('teacher_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('teacher_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'teacher/form.html', ctx)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')


@login_required_decorator
def teacher_list(request):
    teachers = services.get_teachers()
    ctx = {
        "teachers": teachers
    }
    return render(request, 'teacher/list.html', ctx)


# GROUP
@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('group_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'group/form.html', ctx)


@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect('group_list')


@login_required_decorator
def group_list(request):
    groups = services.get_groups()
    ctx = {
        "groups": groups
    }
    return render(request, 'group/list.html', ctx)


# STUDENT
@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('student_list')
    ctx = {
        "model": model,
        "form": form
    }
    return render(request, 'student/form.html', ctx)


@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')


@login_required_decorator
def student_list(request):
    students = services.get_students()
    ctx = {
        "students": students
    }
    return render(request, 'student/list.html', ctx)


@login_required_decorator
def profile(request):
    return render(request, 'profile.html')
