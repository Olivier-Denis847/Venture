from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class promptForm(forms.Form):
    prompt = forms.CharField(label='Enter your prompt', max_length=15)

def index(request):
    if request.method == 'POST':
        form = promptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            return HttpResponseRedirect(reverse('landing', args=[prompt]))
    return render(request, 'main/index.html', 
                  {'form': promptForm()})

def landing(request, prompt):
    return render(request, 'main/landing.html')