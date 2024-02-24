from django.shortcuts import render

# Create your views here.

def student(request):
    return render(request, 'student.html')
def index(request):
    return render(request, 'index.html')
def teacher(request):
    return render(request, 'teacher.html')
