from django.shortcuts import render
from app.models import Session
from django.views.generic import *
from app.forms import SessionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')

class SessionList(ListView):
    model = Session

class SessionDetail(DetailView):
    model = Session

class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm

class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm

class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    # needs to match the name of the view i want to send the user back to
    success_url = reverse_lazy('sessions_list')


# from django.contrib.auth.decorators import login_required
# @login_required
# def submit_session(request):
#     return render(request, 'app/submit_session.html')