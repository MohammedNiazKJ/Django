from django.http import HttpResponse
from datetime import date

def home_page_view(request):
    today = date.today()
    formatted_date = today.strftime("%d-%m-%y")
    return HttpResponse(formatted_date)
    