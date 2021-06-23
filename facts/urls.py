from django.urls import path
from .views import FactsList, FactsDetail

urlpatterns = [
    path('', FactsList.as_view(), name='facts_list'),
    path('facts/<int:pk>', FactsDetail.as_view(), name='facts_details'),
]