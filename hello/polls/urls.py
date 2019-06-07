from django.urls import path 
from polls.views import home,inscrição 

app_name= 'polls'

urlpatterns = [

 path('home/',home),
 path('inscrição/',inscrição)
 

]