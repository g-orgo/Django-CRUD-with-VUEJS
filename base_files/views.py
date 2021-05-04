from django.shortcuts import render

def home_vue(request):
    return render(request, 'base_files/index.html')