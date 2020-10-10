"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls', namespace='products')), # main 화면 연결, 제품 관련 기능
    path('engineers/', include('engineers.urls', namespace="engineers")), # 설치 기사 관련 기능
    path('payments/', include('payments.urls', namespace='payments')),    # 예약 확인 및 주문 기능
    path('users/', include('users.urls', namespace="users")), # user login/logout 기능
    path('comments/', include('comments.urls', namespace="comments")), # comment url 연결
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)