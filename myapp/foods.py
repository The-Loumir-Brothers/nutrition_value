from django.shortcuts import render, HttpResponse

def food(request):
    return render(request, "foods.html")