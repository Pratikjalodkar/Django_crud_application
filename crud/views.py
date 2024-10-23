from django.shortcuts import redirect, render
from django.views import View
from .models import student
from .forms import AddStudentForm

# def Home(request):

#     return render(request, 'home.html')

class Home(View):
    def get(self , request):
        stu_data = student.objects.all()
        return render(request, 'home.html', {'studata':stu_data})


class Add_student(View):
    def get(self, request):
        fm=AddStudentForm()
        return render(request, 'add_student.html',{'form':fm})
    
    def post(self,request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'add_student.html', {'form':fm})
        
class Delete_Student(View):
    def post(self,request):
        data=request.POST
        id = data.get('id')
        studata = student.objects.get(id=id)
        studata.delete()
        return redirect('/')
    
class EditStudent(View):
    def get(self,request,id):
        stu=student.objects.get(id=id)
        fm=AddStudentForm(instance=stu)
        return render(request, 'edit_student.html',{'form':fm})
    
    def post(self,request,id):
        stu=student.objects.get(id=id)
        fm=AddStudentForm(request.POST, instance=stu)   
        if fm.is_valid():
            fm.save()
            return redirect('/')
