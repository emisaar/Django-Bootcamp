from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from gameapi.models import Company
from gameapi.serializers import CompanySerializer

from gameapi.variables.responses import not_found, resource_deleted, not_allowed

def company_actions(request, pk):
    try:
        company_obj = Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        return JsonResponse(not_found(), status=404)
    
    serialized_company = CompanySerializer(company_obj)

    if request.method == 'GET': # Get company
        data = {
            'data': serialized_company.data
        }
        return JsonResponse(data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)

        company_obj.name = data['name']
        company_obj.country = data['country']

        company_obj.save()

        return JsonResponse(serialized_company.data, status=200)
    
    elif request.method == 'DELETE':
        company_obj.delete()
        return JsonResponse(resource_deleted(), status=204)
    else:
        return JsonResponse(not_allowed(), status=405)
