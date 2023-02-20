from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from gameapi.methods.Auth.user_authorization import validate_jwt

from gameapi.models import Company
from gameapi.serializers import CompanySerializer

from gameapi.variables.responses import not_allowed

def companies_actions(request):
    if request.method == 'POST': # Create new company
        data = JSONParser().parse(request)
        company = CompanySerializer(data=data)

        if company.is_valid():
            company.save()
            return JsonResponse(company.data, status=201)
    elif request.method == 'GET': # Get all companies
        if validate_jwt(request) == True:
            companies = Company.objects.all()
            serialized_companies = CompanySerializer(companies, many=True)
            return JsonResponse(serialized_companies.data, safe=False)
        else:
            return JsonResponse({'message': 'Not authorized. User should be logged in.'}, status=401)
    else:
        return JsonResponse(not_allowed(), status=405)