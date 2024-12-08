from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


# SoftDeleteModel for handling soft delete functionality
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


# CustomUser model extending AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

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

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']  # Fields required for superuser creation

    def __str__(self):
        return self.username


# Profile model linked to CustomUser
class Profile(SoftDeleteModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profiles')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    diagnosis_date = models.DateField()
    severity = models.CharField(max_length=50)
    communication_level = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.first_name} {self.last_name} (Profile of {self.user.username})"


# Episode model to encapsulate triggers, behaviors, and interventions
class Episode(SoftDeleteModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='episodes')
    description = models.TextField()  # A description of the episode
    start_time = models.DateTimeField()  # When the episode starts
    end_time = models.DateTimeField()  # When the episode ends
    episode_date = models.DateField()
    title = models.CharField(max_length=100)
    severity = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'),
                                                        ('High', 'High')])  # Severity of the episode
    notes = models.TextField(blank=True)  # Additional notes about the episode

    def __str__(self):
        return f"Episode {self.id} for {self.profile.first_name} {self.profile.last_name}"

    @property
    def duration(self):
        return self.end_time - self.start_time  # Calculate the duration of the episode


# Trigger model
class Trigger(SoftDeleteModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='triggers')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='triggers')
    trigger_type = models.CharField(max_length=100)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    management_strategy = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # The time when the trigger occurred during the episoFde

    def __str__(self):
        return f"Trigger {self.trigger_type} for Episode {self.episode.id}"


# Behavior model
class Behavior(SoftDeleteModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='behaviors')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='behaviors')
    behavior_type = models.CharField(max_length=100)
    description = models.TextField()
    frequency = models.IntegerField()  # How often the behavior occurred during the episode
    context = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # The time when the behavior occurred during the episode

    def __str__(self):
        return f"Behavior {self.behavior_type} for Episode {self.episode.id}"


# Intervention model
class Intervention(SoftDeleteModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='interventions')
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='interventions')
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE, related_name='interventions')
    intervention_type = models.CharField(max_length=100)
    description = models.TextField()
    effectiveness = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)  # The time when the intervention was applied during the episode

    def __str__(self):
        return f"Intervention {self.intervention_type} for Episode {self.episode.id}"


# Therapy Session Model linked to Profile
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

    def __str__(self):
        return f"Session for {self.profile.first_name} {self.profile.last_name} on {self.session_date}"


#shools

class School(SoftDeleteModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    program_details = models.TextField(help_text="Brief description of the programs offered.")
    student_capacity = models.IntegerField(help_text="Maximum number of students.")
    teacher_student_ratio = models.DecimalField(max_digits=3, decimal_places=1, help_text="Teacher-to-student ratio.")
    enrollment_policies = models.TextField(blank=True, null=True, help_text="Simple enrollment process or criteria.")

    def __str__(self):
        return self.name
#therapist
class Therapist(SoftDeleteModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, help_text="Therapist's area of expertise.")
    contact_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='therapists', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


