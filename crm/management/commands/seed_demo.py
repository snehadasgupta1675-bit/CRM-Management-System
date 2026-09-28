from django.core.management.base import BaseCommand
from crm.models import Customer

class Command(BaseCommand):
    help = "Add sample CRM customers"

    def handle(self, *args, **kwargs):
        demo = [
            ("Aarav Mehta","aarav@example.com","+91 98765 10001","Nova Retail","Kolkata","Active"),
            ("Diya Sharma","diya@example.com","+91 98765 10002","Bright Media","Delhi","Lead"),
            ("Rohan Sen","rohan@example.com","+91 98765 10003","Urban Tech","Mumbai","Active"),
            ("Ananya Roy","ananya@example.com","+91 98765 10004","Green Foods","Bengaluru","Inactive"),
            ("Kabir Das","kabir@example.com","+91 98765 10005","Prime Works","Pune","Lead"),
        ]
        for name,email,phone,company,city,status in demo:
            Customer.objects.get_or_create(email=email, defaults={
                "name": name, "phone": phone, "company": company, "city": city, "status": status,
                "address": "Sample business address", "notes": "Demo customer record."
            })
        self.stdout.write(self.style.SUCCESS("Demo customers added."))
