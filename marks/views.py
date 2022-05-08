from django.shortcuts import render, redirect
from .models import Mark
# Create your views here.
import operator

def index(request):
    if request.method == 'POST':
        if request.POST.get('enroll'):
            print("Marks")
            enroll = request.POST.get('enroll')
            marks_data = Mark.objects.filter(enroll=enroll).order_by('rollno')
            return render(request, 'marks/index.html', context={'marks_data': marks_data})
    else:
        print("Hello")
        marks_data = Mark.objects.order_by('rollno')
        return render(request, 'marks/index.html', context={'marks_data': marks_data})


def addData(request):

        if request.method == 'POST':
            if request.POST.get('name'):

                mark = Mark()
                mark.name = request.POST.get('name')
                mark.enroll = request.POST.get('enroll')
                mark.rollno = request.POST.get('roll')
                mark.eti1 = request.POST.get('eti')
                mark.mgt1 = request.POST.get('mgt')
                mark.mad1 = request.POST.get('mad')
                mark.pwp1 = request.POST.get('pwp')
                mark.wbp1 = request.POST.get('wbp')



                mark.save()
                return render(request, 'marks/addData.html')


        else:
            print("Hello")
            return render(request, 'marks/addData.html')
