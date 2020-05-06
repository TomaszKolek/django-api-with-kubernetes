from django.urls import path
from classifier.api import GetAttributesApi

urlpatterns = [
    path('get-attributes/', GetAttributesApi.as_view(), name="get-attributes"),
]
