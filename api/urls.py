from django.urls import path,include
from . import views
urlpatterns = [
    path('syncdb',views.load_data,name='Load_data'),
    path('fetch',views.fetch.as_view(),name='fetch'), 
    path('input-data',views.userinput.as_view(),name='input-data'), 
    path('click-data',views.userclick.as_view(),name='click-data'), 
    path('logout-data',views.logout.as_view(),name='logout-data'), 
    path('api-token-auth', views.obtain_expiring_auth_token, name='api_token_auth')
]
