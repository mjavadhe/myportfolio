from django.db import models
from django.urls import reverse

class Project(models.Model):
    # فیلدهای موجود
    title = models.CharField(max_length=100)
    description = models.TextField()
    # اضافه کردن فیلد جدید
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    technologies = models.CharField(max_length=200, blank=True)
    technologies2 = models.CharField(max_length=200, blank=True)
    technologies3 = models.CharField(max_length=200, blank=True)
    technologies4 = models.CharField(max_length=200, blank=True)

    date_created = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    # بقیه کدها...
# models.py
class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('github', 'GitHub'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('telegram', 'Telegram'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon_class = models.CharField(max_length=50)
    
    # رنگ‌های مربوط به هر پلتفرم
    @property
    def platform_color(self):
        colors = {
            'github': 'gray',
            'linkedin': 'blue',
            'instagram': 'pink',
            'twitter': 'sky',
            'telegram': 'indigo',
        }
        return colors.get(self.platform, 'gray')
    
    def __str__(self):
        return self.platform
