from django.urls import path
from .import views as v

urlpatterns = [
    
    path("home", v.home, name="home"),
    path('',v.regstr,name="regstrpage"),
     path("about", v.about, name="aboutpage"),
    path("add", v.add, name="addemp"),
    path('editemp/<em_id>', v.editemp, name="editemp"),
    path('delemp/<em_id>', v.delemp, name="delemp"),
    path('vemployee', v.vemp, name='viewemployeepage'),
    path('login',v.logins,name="loginpage"),
    path('logout', v.logouts, name="logouts"),
]