from django.urls import path
from .views import Newsp,Home,SportNews, Contact, NewsDate, register, addUser, modelform, addModelForm

#مثال مدل فرم
app_name = 'polls'
from . import views



urlpatterns = [
    path('', Home, name = 'home'),
    path('news/', Newsp, name = 'news'),
    path('sportnews/', SportNews, name = 'snews'),
    path('newsdate/<int:year>', NewsDate, name = 'newsdate'),
    path('contact/', Contact, name = 'contact'),
    path('signup/', register, name = 'register'),
    path('addUser/', addUser, name = 'addUser'),
    path('model/', modelform, name = 'model'),
    path('addmodelform/', addModelForm, name = 'modelform'),

]