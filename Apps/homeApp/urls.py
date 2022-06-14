from django.contrib import admin
from django.urls import path,include
from .views import userhome,usersignup,userrealtime,userlogin,base,predict_csv_single,predict_csv_multi,predict_data_manually,change_password,login2,add_files_multi,about,dashboard,userLogout,prediction_button,enter_form_data_manually,add_files_single

urlpatterns = [
    path('',base),
    path('login/',login2,name='login2'),
    path('logout/',userLogout,name='userLogout'),
    path('userlogin/',userlogin,name='userlogin'),
    path('usersignup/',usersignup,name='usersignup'),
    path('userhome/',userhome,name='userhome'),
    path('about/',about,name='about'),
    path('userrealtime/',userrealtime,name="userrealtime"),
    path('dashboard/',dashboard,name='dashboard'),
    path('prediction_button/',prediction_button,name='prediction_button'),
    path('enter_form_data_manually/',enter_form_data_manually,name='enter_form_data_manually'),
    path('add_files_single/',add_files_single,name='add_files_single'),
    path('add_files_multi/',add_files_multi,name='add_files_multi'),

    path('predict_data_manually/',predict_data_manually,name='predict_data_manually'),
    path('predict_csv_single/',predict_csv_single,name='predict_csv_single'),
    path('predict_csv_multi/',predict_csv_multi,name='predict_csv_multi'),
    path('change_password/',change_password,name='change_password')
]
