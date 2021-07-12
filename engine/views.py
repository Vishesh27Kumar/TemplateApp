from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from engine.services.TemplateService import TemplateService

@api_view(['GET', 'POST'])
def handleGetAndCreateCustomerTemplates(request, customer_id):
    
    if request.method == 'POST':
        return TemplateService.createTemplateByCustomerId(customer_id)

    if request.method == 'GET':
        return TemplateService.getTemplateByCustomerId(customer_id)
