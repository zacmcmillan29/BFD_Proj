from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
# HERE, I need to import the HTML page that I want and then i can return it LATER
from createOrder.models import Employee, job_order, ticket


################# Create your views here. ################

##### This pulls up the createOrder page ##########
def orderPageView(request):
    return render(request, 'createOrder/createOrder.html')


################### THIS is not displayed to the customer, it will MAKE an order ################
def storeOrderPageView(request):
    # Create a new ticket object from the model (like a new record)
    new_order = job_order()

    # Store the data from the form to the new object's attributes (like columns)
    new_order.order_id = request.POST.get('order_id')
    new_order.product_id = request.POST.get('product_id')
    new_order.employee_id = request.POST.get('employee_id')
    new_order.confirmed_date = request.POST.get('confirmed_date')
    new_order.status = request.POST.get('status')
    new_order.status_change_date = request.POST.get('status_change_date')
    new_order.filing_cabinet = request.POST.get('filing_cabinet')
    new_order.file_name = request.POST.get('file_name')
    new_order.notes = request.POST.get('notes')

    # Save the ticket information record which will generate the autoincremented id
    new_order.save()

    # Make a list of all of the employee records and store it to the variable
    data = job_order.objects.all()

    # Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_ticket": data
    }
    return render(request, 'trackOrders/displayOrders.html', context)


############## this is a display of the FINAL orders created by customers ##############
def OrdersSummaryView(request):
    return render(request, "trackOrders/displayOrders.html")
