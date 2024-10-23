from django.contrib import admin
from django.urls import path
from crud import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('add-student/', Add_student.as_view(), name='add-Student'),
    path('delete-student/', Delete_Student.as_view(), name='delete-Student'),
    path('edit-student/<int:id>/', EditStudent.as_view(), name='edit-Student'),
]
