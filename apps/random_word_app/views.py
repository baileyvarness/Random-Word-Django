from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "unique_id": get_random_string(length=14)
    }
    if 'counter' not in request.session:
        request.session['counter'] = 1
    return render(request, "index.html", context)

def random_word(request, method="POST"):
    print("Generate Button Was Clicked")
    request.session['counter'] += 1
    return redirect("/")

def random_word_reset(request):
    request.session.clear()
    return redirect("/")

