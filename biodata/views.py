from django.shortcuts import render

# Create your views here.

def biodata_index(request):
    return render(request,'biodata/index.html')
