from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.POST['text']
    amount_of_text = len(text.split())
    return render(request, 'counter.html', {'amount':amount_of_text})