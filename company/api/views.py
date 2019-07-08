# django imports
from django.shortcuts import get_object_or_404

# rest-framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

# local imports
from company.models import Company, Office
from company.api.serializers import CompanySerializer, OfficeSerializer, CompanyListSerializer, ChangeCompanyHeadquaterSerializer


class CompanyView(CreateAPIView):
    '''
        API POST view to create company with office information and 
        GET view to all companies in the DB with headquater office information
    '''

    serializer_class = CompanySerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data,
                context={'request': request})
        serializer.is_valid(raise_exception=True)
        company_id = serializer.save()
        return Response({'status': True, 'data': {'company_id': company_id}}, 
            status=status.HTTP_201_CREATED)


    def get(self, request, format=None):

        companies = Company.objects.all()
        serializer = CompanyListSerializer(companies, many=True)
        return Response({'status': True, 'data': serializer.data}, 
            status=status.HTTP_200_OK)


class OfficeView(CreateAPIView):
    '''
        API to add office according to company 
    '''

    serializer_class = OfficeSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data,
                context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': True, 'data': serializer.data}, 
            status=status.HTTP_201_CREATED)


class ChangeCompanyHeadquaterView(UpdateAPIView):
    '''
        API view to update company headquater
    '''

    serializer_class = ChangeCompanyHeadquaterSerializer

    def patch(self, request, cmp_id, office_id, format=None):

        company = get_object_or_404(Company, pk=cmp_id)
        office = get_object_or_404(Office, pk=office_id)
        serializer = self.serializer_class(office, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': True, 'data': 'Successfully Updated'},
            status=status.HTTP_200_OK)
