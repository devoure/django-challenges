from django.urls import path
from . import views

urlpatterns = [
    path("all/", views.StudentsValues.as_view(), name="get-all"),
    path("create/", views.CreateStudentValues.as_view(), name="create"),
    path("update/<str:pk>", views.UpdateStudentValues.as_view(), name="update"),
    path("delete/<str:pk>", views.DeleteStudentValues.as_view(), name="delete"),
    path("<str:pk>/", views.StudentValues.as_view(), name="get-one"),
]
