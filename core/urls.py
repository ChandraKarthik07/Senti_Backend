from django.urls import path, include, re_path
from .views import *
urlpatterns = [
    path("home/", home, name="test"),
    path("get_scan_id/", GenerateScanView.as_view(), name="get_scan_id"),
    path("scan/<str:scan_id>/", ChannelInfoAPIView.as_view(), name="scan_id"),
    path('signup/', UserSignupView.as_view(), name='signup'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('monthlystats/<str:scan_id>/', MonthlyStatsAPIView.as_view(), name='monthlystats'),
    path('videostats/<str:scan_id>/', VideoStatsAPIView.as_view(), name='videostats'),
]

urlpatterns += [
    re_path(r'^auth/', include('drf_social_oauth2.urls', namespace='drf'))
]
