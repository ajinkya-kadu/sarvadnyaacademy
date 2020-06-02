##student app urls.py

from django.urls import path
from.import views 

urlpatterns = [
    path("",views.index,name="studentsHome"),
    path('about/',views.about,name='about'),    path('ourresult/',views.ourresult,name='ourresult'),
    path('admissions/',views.admissions,name='admissions'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('sarvid/',views.sarvid,name='sarvid'),
    path('contactus/',views.contactus,name='contactus'),
    path('download/',views.download,name='download'),
    path('testseries/',views.testseries,name='testseries'),
    path('examtimetable/',views.examtimetable,name='examtimetable '),
    
]