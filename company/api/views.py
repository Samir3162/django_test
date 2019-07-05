# django imports
from django.shortcuts import get_object_or_404

# rest-framework imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView

# local imports
from company.models import Company, Office
from company.api.serializers import CompanySerializer, OfficeSerializer, OfficeDetailSerializer, ChangeCompanyHeadquaterSerializer


class CompanyView(CreateAPIView):
    '''
        API view to create company with office information
    '''

    serializer_class = CompanySerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data,
                context={'request': request})
        if serializer.is_valid():
            company_id = serializer.save()
            return Response({'status': True, 'data': {'company_id': company_id}}, 
                status=status.HTTP_201_CREATED)
        else:
            message = ''
            for error in serializer.errors:
                err = error +": "+ serializer.errors[error][0]
                message += err
                message += " "
            return Response({'status': True, 'data': message}, 
                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):

        companies = Company.objects.all()
        offices = Office.objects.filter(company__in=companies, headquater=True)
        serializer = OfficeDetailSerializer(offices, many=True)
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
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': serializer.data}, 
                status=status.HTTP_201_CREATED)
        else:
            message = ''
            for error in serializer.errors:
                err = error +": "+ serializer.errors[error][0]
                message += err
                message += " "
            return Response({'status': True, 'data': message}, 
                status=status.HTTP_400_BAD_REQUEST)


class OfficeListView(ListAPIView):
    '''
        API view to get all the offices for a company
    '''

    serializer_class = OfficeSerializer

    def get(self, request, pk, format=None):

        company = get_object_or_404(Company, pk=pk)
        offices = Office.objects.filter(company=company)
        serializer = self.serializer_class(offices, many=True)
        return Response({'status': True, 'data': serializer.data}, 
            status=status.HTTP_200_OK)


class ChangeCompanyHeadquaterView(UpdateAPIView):
    '''
        API view to update company headquater
    '''

    serializer_class = ChangeCompanyHeadquaterSerializer

    def patch(self, request, cmp_id, office_id, format=None):

        company = get_object_or_404(Company, pk=cmp_id)
        office = get_object_or_404(Office, pk=office_id)
        serializer = self.serializer_class(office, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'data': 'Successfully Updated'},
                status=status.HTTP_200_OK)
        else:
            message = ''
            for error in serializer.errors:
                err = error +": "+ serializer.errors[error][0]
                message += err
                message += " "
            return Response({'status': True, 'data': message}, 
                status=status.HTTP_400_BAD_REQUEST)
