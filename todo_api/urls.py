from django.db import router
# # from django.conf.urls import url
# from django.conf.urls import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (RegisterView, HomeView, DriveView, DriveUpdateView)
# router(r'another', ProfileList)
app_name = "todo_api"
urlpatterns = [
    path('<str:username>', HomeView.as_view()),
    path('<str:username>/drive', DriveView.as_view()),
    path('<str:username>/drive/<int:id>', DriveUpdateView.as_view()),
    # path('api/aa/<int:pk>', TodoAPIView.as_view(), name='api_aa'),
    # path('api/dr', DriverPassenger.as_view()),
    # path('profile_list', ProfileList.as_view(template_name = 'rest_framework/profile_list.html',),name='profile_list'),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register', RegisterView.as_view(), name='register'),
    # path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)