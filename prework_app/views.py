from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from prework_app.models import Topic,Webpage,AccessRecord
from prework_app.forms import NewUserForm
from . import forms
# Create your views here.
class IndexView(TemplateView):
    template_name = 'prework_app/index.html'

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}

    return render(request,'prework_app/index.html',context=date_dict)

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
