from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

# from django.contrib.auth.decorators import login_required
#@login_required
#def submit_session(request):
#    return render(request, 'app/submit_session.html')