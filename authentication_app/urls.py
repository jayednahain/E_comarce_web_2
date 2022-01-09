from django.urls import path
from authentication_app.views import login_view,register_view


urlpatterns = [

   path('/login',login_view,name='log_in_link'),
   path('/register',register_view,name='register_link')

]