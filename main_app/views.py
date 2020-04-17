from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from .models import Wackywidgets
from .forms import WackywidgetsForm


class wackywidgetsDelete(DeleteView):
    model = Wackywidgets
    success_url = '/'


def home(request):
    wackywidgets = Wackywidgets.objects.all()
    wackywidgets_form = WackywidgetsForm()

    return render(request, 'home.html', {

        'wackywidgets': wackywidgets, 'wackywidgets_form': wackywidgets_form
    })


def add_wackywidgets(request):
    form = WackywidgetsForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
    return redirect('home')
