from django.urls import path
from . import views

urlpatterns = [
    path('create-student', views.studentViews.as_view(), name='student'),
    path('get-student', views.getStudentView.as_view(), name='get-student'),
    path('update-student/<int:pk>', views.updateStudentView.as_view(), name='update-student'),
    path('delete-student/<int:pk>', views.deleteStudentView.as_view(), name='delete-student'),
]