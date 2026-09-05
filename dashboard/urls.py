from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (
    AdminLoginView,
    dashboard_view,
    workers_view,
    worker_detail_view,
    certificates_view,
    certificate_detail_view,
    verify_certificate_view,
    analytics_view,
    profile_view,
)

urlpatterns = [
    path(
        "login/",
        AdminLoginView.as_view(),
        name="admin-login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="admin-logout",
    ),

    path(
        "",
        dashboard_view,
        name="admin-dashboard",
    ),

    path(
        "workers/",
        workers_view,
        name="workers",
    ),

    path(
        "workers/<str:worker_id>/",
        worker_detail_view,
        name="worker-detail",
    ),

    path(
        "certificates/",
        certificates_view,
        name="certificates",
    ),

    path(
        "certificates/<str:certificate_id>/",
        certificate_detail_view,
        name="certificate-detail",
    ),
    
     # VERIFY CERTIFICATE
    path(
        "certificates/<str:certificate_id>/verify/",
        verify_certificate_view,
        name="verify-certificate",
    ),
    

    path(
        "analytics/",
        analytics_view,
        name="analytics",
    ),

    path(
        "profile/",
        profile_view,
        name="profile",
    ),
]