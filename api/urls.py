from django.urls import path,include
from . import views
urlpatterns = [
    path('syncdb',views.load_data,name='Load_data'),
    path('fetch',views.fetch.as_view(),name='fetch'), 
]
