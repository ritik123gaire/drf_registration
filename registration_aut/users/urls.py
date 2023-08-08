from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserCreate, TeacherList, TeacherDetail, StudentList, StudentDetail

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreate.as_view(), name='register'),
    path('teachers/', TeacherList.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher_detail'),
    path('students/', StudentList.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student_detail'),
]