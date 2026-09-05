from django.db import models
import uuid

from django.contrib.auth.models import User
from django.db import models


class Worker(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="worker_profile",
    )

    worker_id = models.CharField(
        max_length=50,
        unique=True,
    )

    full_name = models.CharField(
        max_length=150,
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    organization = models.CharField(
        max_length=150,
        blank=True,
    )

    sector = models.CharField(
        max_length=100,
        blank=True,
    )

    language = models.CharField(
        max_length=20,
        default="en",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.worker_id} - {self.full_name}"


class TrainingModule(models.Model):
    MODULE_TYPES = [
        ("fire", "Fire & Explosion"),
        ("gas", "Gas Leak & Confined Space"),
        ("machinery", "Machinery Safety"),
        ("electrical", "Electrical Safety"),
        ("ppe", "PPE Safety"),
    ]

    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        unique=True,
    )

    module_type = models.CharField(
        max_length=50,
        choices=MODULE_TYPES,
    )

    description = models.TextField(
        blank=True,
    )

    version = models.PositiveIntegerField(
        default=1,
    )

    passing_score = models.PositiveIntegerField(
        default=75,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title


class TrainingStep(models.Model):
    STEP_TYPES = [
        ("instruction", "Instruction"),
        ("find_target", "Find Target"),
        ("select_option", "Select Option"),
        ("ar_interaction", "AR Interaction"),
        ("sequence", "Sequence"),
        ("question", "Question"),
    ]

    module = models.ForeignKey(
        TrainingModule,
        on_delete=models.CASCADE,
        related_name="steps",
    )

    order = models.PositiveIntegerField()

    step_type = models.CharField(
        max_length=50,
        choices=STEP_TYPES,
    )

    title = models.CharField(
        max_length=200,
        blank=True,
    )

    instruction = models.TextField(
        blank=True,
    )

    target = models.CharField(
        max_length=100,
        blank=True,
    )

    score = models.PositiveIntegerField(
        default=0,
    )

    is_critical = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.module.title} - Step {self.order}"


class TrainingAttempt(models.Model):
    STATUS_CHOICES = [
        ("in_progress", "In Progress"),
        ("passed", "Passed"),
        ("failed", "Failed"),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="attempts",
    )

    module = models.ForeignKey(
        TrainingModule,
        on_delete=models.CASCADE,
        related_name="attempts",
    )

    score = models.FloatField(
        default=0,
    )

    critical_violation = models.BooleanField(
        default=False,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="in_progress",
    )

    started_at = models.DateTimeField(
        auto_now_add=True,
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.worker.full_name} - {self.module.title}"


class MistakeEvent(models.Model):
    attempt = models.ForeignKey(
        TrainingAttempt,
        on_delete=models.CASCADE,
        related_name="mistakes",
    )

    step = models.ForeignKey(
        TrainingStep,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    description = models.TextField()

    is_critical = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.description[:50]


class Certificate(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("revoked", "Revoked"),
        ("expired", "Expired"),
    ]

    certificate_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="certificates",
    )

    attempt = models.OneToOneField(
        TrainingAttempt,
        on_delete=models.CASCADE,
        related_name="certificate",
    )

    module = models.ForeignKey(
        TrainingModule,
        on_delete=models.CASCADE,
    )

    score = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="active",
    )

    issued_at = models.DateTimeField(
        auto_now_add=True,
    )

    expires_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.certificate_id)
# Create your models here.
