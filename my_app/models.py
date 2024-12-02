from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()
    all_objects = models.Manager()  # Includes soft deleted objects

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)

class CustomUser(AbstractUser):
    AUTISTIC = 'autistic'
    PARENT = 'parent'
    GUARDIAN = 'guardian'

    USER_TYPES = [
        (AUTISTIC, 'Autistic'),
        (PARENT, 'Parent'),
        (GUARDIAN, 'Guardian'),
    ]

    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default=AUTISTIC,
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Profile(SoftDeleteModel):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    diagnosis_date = models.DateField()
    severity = models.CharField(max_length=50)
    communication_level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        db_table = 'profile'
        unique_together = ('user',)  # Ensure each user has one profile


class Trigger(SoftDeleteModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    trigger_type = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    management_strategy = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        db_table = 'trigger'

class Behavior(SoftDeleteModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    behavior_type = models.CharField(max_length=100)
    description = models.TextField()
    frequency = models.IntegerField()
    context = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        db_table = 'behavior'


class Intervention(SoftDeleteModel):
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    intervention_type = models.CharField(max_length=100)
    description = models.TextField()
    effectiveness = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        db_table = 'intervention'

class Session(SoftDeleteModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    session_date = models.DateField()
    therapist = models.CharField(max_length=100)
    notes = models.TextField()
    goals = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        db_table = 'session'