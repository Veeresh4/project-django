"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from TestApp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from TestApp.views import RegisterAPI
from knox import views as knox_views
from TestApp.views import LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),     # url for user that we created in admin
    path('', views.home, name='home'),
    path('Registration', views.test, name='test'),
    path('userdata', views.userdata, name='userdata'),
    path('update/<id>', views.update, name='update'),
    path('delete/<id>', views.delete, name='delete'),

    # path('getdata', views.getdata, name='getdata'),                 # func based url
    # path('getdata1/<int:pk>/', views.getdata1, name='getdata1'),    # func based url
    path('get_data', views.get_data.as_view()),                         # class based url
    path('update_data/<int:pk>/', views.update_data.as_view()),         # class based url

    # path('gen_data', views.gen_data.as_view()),                     # generic based url
    # path('gen_data1/<int:pk>/', views.gen_data1.as_view()),         # generic based url
    # path('mix_data', views.mix_data.as_view()),                       # mixins based url
    # path('mix_data1/<int:pk>/', views.mix_data1.as_view()),           # mixins based url

    # path('comp_getdata', views.comp_getdata.as_view(), name='comp_getdata'),                      # company class based url
    # path('comp_updatedata/<int:pk>/', views.comp_updatedata.as_view(), name='comp_updatedata'),    # compnay class based url
    # path('emp_getdata', views.emp_getdata.as_view(), name="emp_getdata"),                        # employee class based url
    # path('emp_updatedata/<int:pk>/', views.emp_updatedata.as_view(), name="emp_updatedata"),     # employee class based url

    path('comp_gen_data', views.comp_gen_data.as_view()),                     # company generic url
    path('comp_gen_data1/<int:pk>/', views.comp_gen_data1.as_view()),         # compnay generic url
    path('emp_gen_data', views.emp_gen_data.as_view()),                     # company generic url
    path('emp_gen_data1/<int:pk>/', views.emp_gen_data1.as_view()),         # company generic url

    # path('comp_mix_data', views.comp_mix_data.as_view()),                    # company mixins url
    # path('comp_mix_data1/<int:pk>/', views.comp_mix_data1.as_view()),        # company mixins url
    # path('emp_mix_data', views.emp_mix_data.as_view()),                       # employee mixins url
    # path('emp_mix_data1/<int:pk>/', views.emp_mix_data1.as_view()),           # employee mixins url

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),       # for token generation
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      # for token refresh
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),         # for token verify

    path('api/myRegister/', RegisterAPI.as_view(), name='myRegister'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
