from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "phone", "company", "address", "city", "status", "notes"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Enter full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "name@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+91 98765 43210"}),
            "company": forms.TextInput(attrs={"placeholder": "Company name"}),
            "address": forms.Textarea(attrs={"rows": 3, "placeholder": "Street / area / landmark"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            "status": forms.Select(),
            "notes": forms.Textarea(attrs={"rows": 4, "placeholder": "Add useful notes about this customer"}),
        }
