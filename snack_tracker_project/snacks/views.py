from django.shortcuts import render
from django.views.generic import ListView,DetailView
# to link our view to the model we import Snack from .models
from .models import Snack

# Create your views here.


class SnackListView(ListView):
    template_name = 'snack_list.html'
    # to link the view with a specific model
    model = Snack
    context_object_name = 'snack_list'

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    # to link the view with a specific model 
    model = Snack
