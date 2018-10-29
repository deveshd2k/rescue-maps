from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('login', auth_views.LoginView.as_view(template_name="login.html"),name = 'login'),
	path('signup',views.signup,name="signup"),
	path('org_map',views.org_map,name='org_map'),
	path('user_map',views.user_map,name='user_map'),
	path('survey',views.survey,name='survey'),
	path('logout',views.user_logout,name = 'logout'),
	path('dashboard',views.orgdash,name = 'dashboard'),
	path('dashboard/rescueCenter',views.rescueCenter,name = 'rescueCenter')
]