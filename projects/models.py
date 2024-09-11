from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    progress_percentage = models.IntegerField()
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    LOCATION_CHOICES = [
        ('nepal', 'Nepal'),
        ('netherlands', 'Netherlands'),
        ('world', 'World'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)  # Ensure this is correct
    facebook_url = models.URLField(max_length=255, blank=True)
    twitter_url = models.URLField(max_length=255, blank=True)
    linkedin_url = models.URLField(max_length=255, blank=True)

    def __str__(self):
        return self.name
