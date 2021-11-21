from django.shortcuts import render

# this is for rendering the files
from django.shortcuts import render

# this view function needs to send the RESPONSE
from django.http import HttpResponse

# HERE, I need to import the HTML page that I want and then i can return it LATER
from createOrder.models import Employee, job_order, ticket


################# Create your views here. ################

# this is to pull up ALL the orders submitted by the customer (search for the records itself)
def findOrdersPageView(request):
    return render(request, 'trackOrders/displayOrders.html')

# findTrackOrdersPageView --> this displays all of orders


def searchOrdersPageView(request):
    sFirst = request.GET['first_name']
    sLast = request.GET['last_name']
    data = job_order.objects.filter(
        emp_first=sFirst, emp_last=sLast)

    if data.count() > 0:
        context = {
            "customer_order": data
        }
        return render(request, 'trackOrders/displayOrders.html', context)
    else:
        return HttpResponse("Not found")

# this is if the order needs to be edited BEFORE being ADD to the TICKET table, which is just an order being confirmed


def EditOrderPageView(request):
    # context = we need to make this load all of the data from the database
    return render(request, 'trackOrders/editOrder.html')

# this is to ADD to the TICKET table, which is just an order being confirmed


def AcceptOrderPageView(request):
    return render(request, 'trackOrders/ticketsSummary.html')


################### THIS is not displayed to the manager, it will MAKE a ticket ################
def storeTicketPageView(request):
    # Create a new ticket object from the model (like a new record)
    new_ticket = ticket()

    # Store the data from the form to the new object's attributes (like columns)
    # we still need to edit these (:
    new_ticket.order_id = request.POST.get('order_id')
    new_ticket.product_id = request.POST.get('product_id')
    new_ticket.employee_id = request.POST.get('employee_id')
    new_ticket.confirmed_date = request.POST.get('confirmed_date')
    new_ticket.status = request.POST.get('status')
    new_ticket.status_change_date = request.POST.get('status_change_date')
    new_ticket.filing_cabinet = request.POST.get('filing_cabinet')
    new_ticket.file_name = request.POST.get('file_name')
    new_ticket.notes = request.POST.get('notes')

    # Save the ticket information record which will generate the autoincremented id
    new_ticket.save()

    # Make a list of all of the employee records and store it to the variable
    data = ticket.objects.all()

    # Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "our_ticket": data
    }
    return render(request, 'trackOrders/displayOrders.html', context)


############## this is a display of the unconfirmed orders ##############
def TicketsSummaryView(request):
    return render(request, "trackOrders/displayOrders.html")
