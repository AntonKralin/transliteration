from django.shortcuts import render
from .forms import TextForm
from .functions import translit, trancate

# Create your views here.

def index(request):
    result = ""
    form = TextForm()
    if request.method == "POST":
        text = request.POST.get("text")
        result = translit(text)
        result2 = trancate(result)
    return render(request, 'transliteration/index.html', 
                  {"form": form,
                   "result": result,
                   "result2": result2})
