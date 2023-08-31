from django.urls import path,include
from . import views
# from rest_framework.views import 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView


urlpatterns = [
    path('',views.Student_details.as_view(),name='student'),
    path('<int:pk>/',views.Student_updates.as_view(),name='student'),
    path('gettoken/',TokenObtainPairView.as_view(),name='tokenobtainpairview'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='tokenrefreshview'),
    path('verifytoken/',TokenVerifyView.as_view(),name='tokenverifyview')

]   