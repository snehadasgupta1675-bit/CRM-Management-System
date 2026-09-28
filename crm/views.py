from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomerForm
from .models import Customer

def dashboard(request):
    customers = Customer.objects.all()
    context = {
        "total_customers": customers.count(),
        "active_customers": customers.filter(status="Active").count(),
        "leads": customers.filter(status="Lead").count(),
        "inactive_customers": customers.filter(status="Inactive").count(),
    }
    return render(request, "dashboard.html", context)

def customer_list(request):
    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()
    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(company__icontains=query) |
            Q(city__icontains=query)
        )
    if status in {"Active", "Lead", "Inactive"}:
        customers = customers.filter(status=status)

    return render(request, "customers/list.html", {
        "customers": customers,
        "query": query,
        "selected_status": status,
    })

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, "customers/detail.html", {"customer": customer})

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f"{customer.name} was added successfully.")
            return redirect("customer_detail", pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, "customers/form.html", {"form": form, "title": "Add New Customer", "button": "Save Customer"})

def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f"{customer.name}'s details were updated.")
            return redirect("customer_detail", pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, "customers/form.html", {"form": form, "title": "Edit Customer", "button": "Update Customer", "customer": customer})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        name = customer.name
        customer.delete()
        messages.success(request, f"{name} was deleted.")
        return redirect("customer_list")
    return render(request, "customers/delete.html", {"customer": customer})

def reports(request):
    customers = Customer.objects.all()
    cities = {}
    for customer in customers:
        if customer.city:
            cities[customer.city] = cities.get(customer.city, 0) + 1
    top_cities = sorted(cities.items(), key=lambda item: item[1], reverse=True)[:6]
    context = {
        "total": customers.count(),
        "active": customers.filter(status="Active").count(),
        "leads": customers.filter(status="Lead").count(),
        "inactive": customers.filter(status="Inactive").count(),
        "top_cities": top_cities,
    }
    return render(request, "reports.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        messages.success(request, "Thank you! Your message has been received.")
        return redirect("contact")
    return render(request, "contact.html")
