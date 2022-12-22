from django.urls import path
from .views import EmployeeCreate,NonWorkerCreate
urlpatterns=[
    path('work/',(EmployeeCreate.as_view())),
    path('nonworker/',(NonWorkerCreate.as_view())),
]