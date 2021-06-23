from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CodesView


codes_list = CodesView.as_view({
    'post': 'create',
    'get': 'list'
})

codes_detail = CodesView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('codes/', codes_list, name='codes_list'),
    path('codes/<int:pk>', codes_detail, name='codes_detail'),
]
