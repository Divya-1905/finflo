from django.urls import path
from .views import EmployeeCreate
urlpatterns=[
    path('work/',(EmployeeCreate.as_view())),
]