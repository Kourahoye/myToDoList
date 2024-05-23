from datetime import UTC, datetime
from time import timezone
from arrow import utcnow
from django.db import models
from django.urls import reverse
from slugify import slugify
from accounts.models import Utilisateurs

# Create your models here.

class Task(models.Model):
    title = models.CharField(null = False, unique = True, max_length = 20,verbose_name="Titre")
    content = models.TextField(blank = True)
    done = models.BooleanField(null = False, default = False )
    slug = models.SlugField(unique = True)
    user = models.ForeignKey(to = Utilisateurs, on_delete = models.CASCADE)
    created = models.DateTimeField(null=False, default =f'{datetime.now() }')
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Task, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        
        managed = True
        verbose_name = 'Tache'
        verbose_name_plural = 'Tasks'
    
    def get_absolute_url(self):
       return reverse("details", kwargs={"slug": self.slug})