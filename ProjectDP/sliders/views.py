# Create your views here.
from bokeh.embed import server_document

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def sliders(request: HttpRequest) -> HttpResponse:
    
    script = server_document(request.build_absolute_uri())
    # print(script)
    # return HttpResponse("Hello World!")
    return render(request, "sliders.html", dict(script=script))