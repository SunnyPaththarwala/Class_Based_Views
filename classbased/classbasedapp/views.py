from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from classbasedapp.models import Student
# Create your views here.
class Myview(View):
    def get(self,request):
        # return HttpResponse('Welcome to class Based views !!!')
        return render(request,'temp1.html')
    def post(self,request):
        pass
class Addstudent(View):
    def get(self,request):
        return render(request,'addstu.html')
    def post(self,request):
        n = request.POST['name']   
        b = request.POST['branch']    
        p = request.POST['percentage']
        stu= Student.objects.create(name=n,branch=b,perc=p)
        stu.save()
        return redirect('/allstudents')
class StudentList(View):
    def get (self,request):
        data=Student.objects.all()
        context={'students':data}
        return render(request,'stulist.html',context)   
    
class Deletestu(View):
    def get(self,request,sid):
        stu =Student.objects.get(id=sid)
        stu.delete()
        return redirect('/allstudents')     
    
class Updatestu(View):
    def get(self,request,sid):
        stu =Student.objects.get(id=sid)
        context ={'stu':stu}
        return render(request,'updatestu.html',context)
    def post(self,request,sid):
        stu = Student.objects.filter(id=sid)
        n = request.POST['name']   
        b = request.POST['branch']    
        p = request.POST['percentage']
        stu.update(name=n,branch=b,perc=p)
        return redirect('/allstudents')     

    
    

         
    