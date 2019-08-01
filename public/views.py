from django.shortcuts import render
import requests
import json
from .forms import YelpSearchForm
from django.views.decorators.csrf import csrf_exempt
from .passwords import passwords

api_key = "0tR7cGnD1qm8VRPOendQ0dHzD-NV_uiftDPlmAMwF0RBa8gmea32QrXy1wOPoi_0lrLRbctO3MsXYl2jX7Ew7j5cVCqiTpHoUq9bjGXT_Yc4iZ_DfJORaxOX3SBCXXYx"
headers = {'Authorization': 'Bearer %s' % api_key}


@csrf_exempt
def index(request):
    url = 'https://api.yelp.com/v3/businesses/search'
    if request.method == 'POST':
        form = YelpSearchForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            term = form.cleaned_data.get('term')
            location = form.cleaned_data.get('location')
            radius = form.cleaned_data.get('radius')
            categories = form.cleaned_data.get('categories')
            price = form.cleaned_data.get('price')
            open_now = form.cleaned_data.get('open_now')
            if password in passwords:
                params = {}
                if term:
                    params.update({'term': term})
                if location:
                    params.update({'location': location})
                if radius:
                    params.update({'radius': radius})
                if categories:
                    params.update({'categories': categories})
                if price:
                    params.update({'price': price})
                if open_now:
                    params.update({'open_now': open_now})
                req = requests.get(url, params=params, headers=headers)
                status_code = ('The status code is {}'.format(req.status_code))
                if format(req.status_code) == '200':
                    status_code = 'Request made successfully'
                business_response = json.loads(req.text)
                total = business_response["total"]
                context = {
                    'form': YelpSearchForm(),
                    'status_code': status_code,
                    'total': total,
                    'response': business_response,
                }
                return render(request, 'index.html', context=context)
            else:
                context = {
                    'form': YelpSearchForm(),
                    'error': 'Incorrect Password. Request a password by private messaging u/YoomamaFTW on reddit.com',
                }
                return render(request, 'index.html', context=context)
        else:
            print(form.errors)
    elif request.method == 'GET':
        form = YelpSearchForm()
        return render(request, 'index.html', {'form': form})
