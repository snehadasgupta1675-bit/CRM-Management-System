from django.db import models

class Customer(models.Model):
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Lead", "Lead"),
        ("Inactive", "Inactive"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    company = models.CharField(max_length=120, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=80, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
