from django.http import HttpResponse

def index(request):
    return HttpResponse("whatTo.Eat is ALIVE!")

def about(request):
    return HttpResponse("We should have all of our information here")

