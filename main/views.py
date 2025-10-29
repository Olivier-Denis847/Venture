from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json

from main import gemini

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
    product = gemini.product_name(prompt)
    description = gemini.product_description(product)
    tagline = gemini.product_tagline(product)
    logo_img = gemini.product_logo(product)
    return render(request, 'main/landing.html', {
        'product' : product,
        'description' : description,
        'tagline' : tagline,
        'logo_img' : logo_img
    })

def slides(request):
    data = json.loads(request.body)    
    product = data.get('product')
    mode = int(data.get('mode'))
    return JsonResponse({'url':gemini.product_slide(product, mode)}, status = 200)