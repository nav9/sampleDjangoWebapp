from django.shortcuts import render
from django.http import HttpResponse
#import logging
#
#logger = logging.getLogger(__name__)

def index(request):        
    context = {'_': None}
    r = str(request)
    #logger.info(r)
    #return HttpResponse("the request: ")
    #return render(request, 'landingPage/index.html', context)
    return render(request, 'landingPage/index.html', context)
