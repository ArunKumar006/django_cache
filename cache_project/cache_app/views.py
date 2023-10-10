from django.shortcuts import render
from django.http import JsonResponse
import requests
import pdb
from django.views.decorators.cache import cache_page
@cache_page( 60 * 15, key_prefix="test_cache" )
def blog( request ):
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    # print(r.json(),"jjjjj","jsjsjsjsjjs")
    return JsonResponse(r.json(),safe=False)
