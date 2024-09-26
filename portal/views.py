from django.shortcuts import render

# Create your views here.
# view index
def index(request):
  return render(request, 'portal/index.html')