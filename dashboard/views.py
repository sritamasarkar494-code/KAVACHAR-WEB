from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .services.springboot import get_from_spring, post_to_spring


# --------------------------------------------------
# ADMIN ACCESS
# --------------------------------------------------

def admin_required(view_func):
    """
    Allow only Django staff/superuser accounts
    to access the admin dashboard.
    """
    @login_required
    def wrapper(request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            raise PermissionDenied

        return view_func(request, *args, **kwargs)

    return wrapper


class AdminLoginView(LoginView):
    """
    Login page for Django administrators only.
    """

    template_name = "dashboard/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()

        if not (user.is_staff or user.is_superuser):
            form.add_error(
                None,
                "You are not authorized to access the admin panel."
            )
            return self.form_invalid(form)
# AUTHENTICATE / LOGIN
        login(self.request, user)
        return redirect("admin-dashboard")


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

@admin_required
def dashboard_view(request):
    """
    Get dashboard data from Spring Boot
    and display it.
    """
    data = {
        "total_workers": 248,
        "completed_training": 192,
        "certificates_issued": 156,
        "pending_certificates": 12,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        {"data": data},
    )

    #data = get_from_spring("/api/admin/dashboard")

    ###return render(
        #request,
        #"dashboard/dashboard.html",
        #{
           # "data": data,
        #},
    #)


# --------------------------------------------------
# WORKERS
# --------------------------------------------------

@admin_required
def workers_view(request):
    """
    Get workers from Spring Boot.
    """

    #workers = get_from_spring("/api/admin/workers")
    workers = [
        {
            "workerId": "W001",
            "name": "Rahul Kumar",
            "phone": "9876543210",
            "organization": "KavachAR Industries",
            "progress": 90,
            "status": "Active",
        },
        {
            "workerId": "W002",
            "name": "Amit Singh",
            "phone": "9876543211",
            "organization": "KavachAR Industries",
            "progress": 75,
            "status": "Active",
        },
        {
            "workerId": "W003",
            "name": "Sunita Devi",
            "phone": "9876543212",
            "organization": "KavachAR Industries",
            "progress": 100,
            "status": "Completed",
        },
    ]


    return render(
        request,
        "workers/workers.html",
        {
            "workers": workers,
        },
    )


@admin_required
def worker_detail_view(request, worker_id):
    """
    Get one worker's details from Spring Boot.
    """
# REAL SPRING BOOT IMPLEMENTATION
    #worker = get_from_spring(
        #f"/api/admin/workers/{worker_id}"
   # )
   #attempts = worker.get("attempts", [])
    # certificates = worker.get("certificates", [])
    workers = {
        "W001": {
            "workerId": "W001",
            "name": "Rahul Kumar",
            "phone": "9876543210",
            "organization": "KavachAR Industries",
            "progress": 90,
            "status": "Active",
        },

        "W002": {
            "workerId": "W002",
            "name": "Amit Singh",
            "phone": "9876543211",
            "organization": "KavachAR Industries",
            "progress": 75,
            "status": "Active",
        },

        "W003": {
            "workerId": "W003",
            "name": "Sunita Devi",
            "phone": "9876543212",
            "organization": "KavachAR Industries",
            "progress": 100,
            "status": "Completed",
        },
    }
    # Demo training attempts
    # ---------------------------------------------------------

    attempts = {
        "W001": [
            {
                "moduleTitle": "Fire Safety",
                "score": 92,
                "status": "Passed",
                "date": "02 Sep 2026",
            },
            {
                "moduleTitle": "PPE Safety",
                "score": 78,
                "status": "Passed",
                "date": "03 Sep 2026",
            },
            {
                "moduleTitle": "Emergency Response",
                "score": 65,
                "status": "Failed",
                "date": "04 Sep 2026",
            },
        ],

        "W002": [
            {
                "moduleTitle": "Fire Safety",
                "score": 88,
                "status": "Passed",
                "date": "01 Sep 2026",
            },
            {
                "moduleTitle": "PPE Safety",
                "score": 81,
                "status": "Passed",
                "date": "03 Sep 2026",
            },
        ],

        "W003": [
            {
                "moduleTitle": "Fire Safety",
                "score": 96,
                "status": "Passed",
                "date": "28 Aug 2026",
            },
            {
                "moduleTitle": "Emergency Response",
                "score": 94,
                "status": "Passed",
                "date": "30 Aug 2026",
            },
        ],
    }
    # Demo certificates
    # ---------------------------------------------------------

    certificates = {
        "W001": [
            {
                "certificateId": "CERT001",
                "moduleTitle": "Fire Safety",
                "score": 92,
                "status": "Verified",
            },
        ],

        "W002": [
            {
                "certificateId": "CERT002",
                "moduleTitle": "PPE Safety",
                "score": 85,
                "status": "Pending",
            },
        ],

        "W003": [
            {
                "certificateId": "CERT003",
                "moduleTitle": "Emergency Response",
                "score": 96,
                "status": "Verified",
            },
        ],
    }


     # GET DATA FOR THIS PARTICULAR WORKER
    # =========================================================

    worker_attempts = attempts.get(worker_id, [])
    worker_certificates = certificates.get(worker_id, [])

    worker = workers.get(
        worker_id,
        {
            "workerId": worker_id,
            "name": "Unknown Worker",
            "phone": "N/A",
            "organization": "N/A",
            "progress": 0,
            "status": "Unknown",
        },
    )
    return render(
        request,
        "workers/worker_detail.html",
        {
            "worker": worker,
            "attempts": worker_attempts,
            "certificates": worker_certificates,
        },
    )


# --------------------------------------------------
# CERTIFICATES
# --------------------------------------------------

@admin_required
def certificates_view(request):
    """
    Get certificates from Spring Boot.
    """

    #certificates = get_from_spring(
       # "/api/admin/certificates"
    #)
    certificates = [
        {
            "certificateId": "CERT001",
            "workerName": "Rahul Kumar",
            "score": 92,
            "status": "Verified",
        },
        {
            "certificateId": "CERT002",
            "workerName": "Amit Singh",
            "score": 85,
            "status": "Pending",
        },
        {
            "certificateId": "CERT003",
            "workerName": "Sunita Devi",
            "score": 96,
            "status": "Verified",
        },
    ]

    return render(
        request,
        "certificates/certificates.html",
        {"certificates": certificates},
    )

    return render(
        request,
        "certificates/certificates.html",
        {
            "certificates": certificates,
        },
    )


@admin_required
def certificate_detail_view(request, certificate_id):
    """
    Get one certificate from Spring Boot.
    """

    #certificate = get_from_spring(
       # f"/api/admin/certificates/{certificate_id}"
    #)
    certificate = {
        "certificateId": certificate_id,
        "workerName": "Rahul Kumar",
        "score": 92,
        "status": "Pending",
    }


    return render(
        request,
        "certificates/certificate_detail.html",
        {
            "certificate": certificate,
        },
    )


# --------------------------------------------------
# CERTIFICATE VERIFICATION
# --------------------------------------------------

@admin_required
@require_POST
def verify_certificate_view(request, certificate_id):
    """
    Send the admin's verification request to Spring Boot.

    Spring Boot performs the actual business logic.
    """

    result = post_to_spring(
        f"/api/admin/certificates/{certificate_id}/verify"
    )

    messages.success(
        request,
        result.get(
            "message",
            "Certificate verification request sent successfully."
        ),
    )

    return redirect(
        "certificate-detail",
        certificate_id=certificate_id,
    )


# --------------------------------------------------
# ANALYTICS
# --------------------------------------------------

@admin_required
def analytics_view(request):
    """
    Get analytics data from Spring Boot.
    """
# REAL SPRING BOOT IMPLEMENTATION
    #analytics = get_from_spring(
        ##"/api/admin/analytics"
    #)
    analytics = {
        "total_workers": 248,
        "active_workers": 210,
        "completed_training": 192,
        "certificates_issued": 156,
        "certificates_pending": 12,
        "average_score": 84.5,
        "passed_attempts": 205,
        "failed_attempts": 43,
        "completion_rate": 77.4,
    }

    return render(
        request,
        "analytics/analytics.html",
        {
            "analytics": analytics,
        },
    )


# --------------------------------------------------
# ADMIN PROFILE
# --------------------------------------------------

@admin_required
def profile_view(request):
    """
    Display the currently logged-in Django admin.
    """

    return render(
        request,
        "profile/profile.html",
        {
            "admin": request.user,
        },
    )