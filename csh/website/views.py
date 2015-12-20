from django.shortcuts import render

# Django transaction system so we can use @transaction.atomic
from django.db import transaction


@transaction.atomic
def home(request):
    context = {}
    return render(request, 'website/home.html', context)
