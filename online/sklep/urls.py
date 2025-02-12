from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from polls import views as polls_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', polls_views.register, name='register'),
    path('dashboard/', polls_views.dashboard, name='dashboard'),
    path('o_nas/', polls_views.o_nas, name='o_nas'),
    path('region/<str:region_id>/', polls_views.region_view, name='region_view'),
    path('vote_city/', polls_views.vote_city, name='vote_city'),
    path('', polls_views.home, name='home'),
]