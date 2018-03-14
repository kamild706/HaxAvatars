from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from avatars import views

urlpatterns = [
    url(r'^$', views.AvatarList.as_view()),
    url(r'^(?P<pk>\d+)/$', views.AvatarDetail.as_view()),
    url(r'^manage/((?P<state>deleted)/)?$', views.AdminAvatarList.as_view()),
    url(r'^manage/(?P<pk>\d+)/$', views.AdminAvatarDetail.as_view()),
    url(r'^auth/$', obtain_jwt_token),
    url(r'^auth/refresh/$', refresh_jwt_token),
]
