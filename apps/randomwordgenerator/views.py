from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def randomword(request):
    try:
        request.session['attempt'] += 1
    except KeyError:
        request.session['attempt'] = 0
    context = {
        'number': request.session['attempt'],
        'word': str(get_random_string(length=14))
    }
    return render(request, "index.html", context)

def reset(request):
    request.session['attempt'] = 0
    return redirect('/randomword/')