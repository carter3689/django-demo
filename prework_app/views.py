from django.shortcuts import render
from prework_app.models import Topic,Webpage,AccessRecord
from prework_app.forms import NewUserForm
from . import forms
from . import models

#Generic views
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
# Create your views here.
class IndexView(TemplateView):
    template_name = 'prework_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context

class UserView(ListView):
    model = models.Users
    # The ListView by default will create a context dictionary which lowercases the model.
    # So the above Users model comes back to the front end it is callable by a different name
    # That name is users_list



#def index(request):
    #webpage_list = AccessRecord.objects.order_by('date')
    #date_dict = {'access_records': webpage_list}

    #return render(request,'prework_app/index.html',context=date_dict)

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'prework_app/users.html', {'form':form})


def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('VALIDATION SUCCESS!!!')
            print("Name:"+ form.cleaned_data['name'])
            print('Email:' + form.cleaned_data['email'])
            print('Email:' + form.cleaned_data['text'])
    return render(request,'prework_app/form_page.html',{'form': form})
