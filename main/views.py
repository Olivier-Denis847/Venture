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
    theme = gemini.procuct_theme(product).lower()
    templates = {
        'minimalist' : 'main/min_landing.html',
        'luxury' : 'main/luxury_landing.html',
        'organic' : 'main/organic_landing.html',
        'tech' : 'main/tech_landing.html',
        'cartoon' : 'main/cartoon_landing.html'
    }
    route = templates.get(theme, 'main/min_landing.html')
    description = gemini.product_description(product)
    tagline = gemini.product_tagline(product)
    logo_img = gemini.product_logo(product)
    return render(request, route, {
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