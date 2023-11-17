from django.shortcuts import render

# Create your views


def about(request):
    return render(request, "about.html", {"link":"about"})

def blog(request):
    context = {"link":"blog"}
    return render(request, "blog.html", context)

