"""A Django view that renders the home page."""
from django.shortcuts import render
import uuid



def home(request):
    """A view that displays the home page."""
    cache_id = str(uuid.uuid4())
    return render(request, 'home.html', {'cache_id': cache_id})

