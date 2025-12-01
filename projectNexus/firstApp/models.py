from django.db import models

# Create your models here.
class Shoes(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    size = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def _str_(self):
        return f"Shoes {self.name}"
    
    class Meta:
        ordering = ["-created_at", "-updated_at"]


class Bags(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    material = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def _str_(self):
        return f"Bags {self.name}"
    
    class Meta:
        ordering = ["-created_at", "-updated_at"]


class Clothes(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    design = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def _str_(self):
        return f"Clothes {self.name}"
    
    class Meta:
        ordering = ["-created_at", "-updated_at"]