from django.db import models
from django.utils import timezone
# Create your models here.
class studentwork(models.Model):
  PROJECTS_CREATED = [
    ('AWS', 'AWS Practice'),
    ('nodejs', 'tour-app')
  ]
  name = models.CharField(max_length=30)
  Github_url = models.URLField(max_length=200, blank=True, null=True)
  image = models.ImageField(upload_to='profile_pics/')
  date_added=models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=10, choices=PROJECTS_CREATED)