from django.shortcuts import render, redirect
from .models import Expense
from django.http import HttpResponse


# Create your views here.
# home
def home(request):
    expenses = Expense.objects.all()
    return render(request, 'index.html', {'expenses': expenses})

# create
def add(request):
    if request.method == 'POST':
        item = request.POST['item']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']

        expense = Expense(item=item, amount=amount, category=category, date=date)
        expense.save()

    return redirect(home)


