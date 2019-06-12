from django.urls import path 
from polls.views import homeTemplateView,inscrição,listagem
from django.views.generic import TemplateView

app_name= 'polls'

urlpatterns = [

 path('home/',homeTemplateView.as_view()),
 path('inscrição/',inscrição),
 path('listagem/',listagem)


 

]