from django.contrib import admin
from django.contrib import admin

from .models import (
    Worker,
    TrainingModule,
    TrainingStep,
    TrainingAttempt,
    MistakeEvent,
    Certificate,
)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        "worker_id",
        "full_name",
        "organization",
        "sector",
        "language",
        "created_at",
    )

    search_fields = (
        "worker_id",
        "full_name",
        "organization",
    )

    list_filter = (
        "sector",
        "language",
    )


@admin.register(TrainingModule)
class TrainingModuleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "module_type",
        "version",
        "passing_score",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    list_filter = (
        "module_type",
        "is_active",
    )


@admin.register(TrainingStep)
class TrainingStepAdmin(admin.ModelAdmin):
    list_display = (
        "module",
        "order",
        "step_type",
        "score",
        "is_critical",
    )

    list_filter = (
        "step_type",
        "is_critical",
    )


@admin.register(TrainingAttempt)
class TrainingAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "worker",
        "module",
        "score",
        "status",
        "critical_violation",
        "started_at",
    )

    list_filter = (
        "status",
        "critical_violation",
    )


@admin.register(MistakeEvent)
class MistakeEventAdmin(admin.ModelAdmin):
    list_display = (
        "attempt",
        "step",
        "is_critical",
        "created_at",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "certificate_id",
        "worker",
        "module",
        "score",
        "status",
        "issued_at",
    )

    search_fields = (
        "certificate_id",
        "worker__worker_id",
        "worker__full_name",
    )

    list_filter = (
        "status",
        "module",
    )
# Register your models here.
