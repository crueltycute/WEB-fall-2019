from django.shortcuts import render

from .models import get_computers, get_browsers_by_computer


def index(request):
    computers = get_computers()

    browsers = []

    for c in computers:
        browsers.append(get_browsers_by_computer(c))

    context = {
        'browsers': browsers
    }

    return render(request, 'index.html', context)
