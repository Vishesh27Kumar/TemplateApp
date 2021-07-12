from engine.dao.engineDAO import TemplatesDAO
from django.http import JsonResponse
from rest_framework import status
from bson import json_util
import json

class TemplateService:

    templates = TemplatesDAO()

    def __init__(self):
        pass

    @classmethod
    def getTemplateByCustomerId(cls, customerId):
        template = cls.templates.getTemplateByCustomerId(customerId)

        if template:
            template = json.loads(json_util.dumps(template))
            return JsonResponse(template, safe=False, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'Template not found for the given customerId.'}, safe=False, status=status.HTTP_404_NOT_FOUND)

    @classmethod
    def createTemplateByCustomerId(cls, customerId):

        alreadyTemplateExist = cls.templates.getTemplateByCustomerId(customerId) 

        if alreadyTemplateExist:
            return JsonResponse({'message': 'Template already exist for the given customerId'}, safe=False, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            newTemplate = dict()
            newTemplate['type'] = 'customer'
            newTemplate['entity'] = 'entity'
            newTemplate['customerId'] = customerId
            newTemplate['law'] = 'base'
            newTemplate['fields'] = list()

            systemTemplates = cls.templates.getSystemTemplates()

            for template in systemTemplates:
                newTemplate['fields'] += template['fields']

            result = cls.templates.createTemplate(newTemplate)

            if result:
                return JsonResponse({'message': 'Template created successfully for the given customerId'}, safe=False, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'message': 'Something went wrong in creating template.'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
