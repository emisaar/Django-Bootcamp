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
        # data = {
        #     'data': serialized_company.data
        # }
        # return JsonResponse(data, status=200)
        company_data = serialized_company.data
        company_name = company_data['name']
        company_country = company_data['country']
        
        data_dict = {
            'id': company_data['id'],
            'name': company_name,
            'country': company_country,
        }

        return JsonResponse(data_dict, status=200)

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
