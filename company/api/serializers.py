# rest-framework imports
from rest_framework import serializers

# local imports
from company.models import Company, Office


class CompanySerializer(serializers.ModelSerializer):
    '''
        Create company with office information serializer
    '''

    street = serializers.CharField(max_length=256, allow_blank=True)
    postal_code = serializers.CharField(max_length=32, allow_blank=True)
    city = serializers.CharField(max_length=128, allow_blank=True, allow_null=True)
    monthly_rent = serializers.DecimalField(decimal_places=2, max_digits=10, allow_null=True)

    def create(self, validated_data):

        company = Company.objects.create(name=validated_data['name'])
        del validated_data['name']
        validated_data['company'] = company
        validated_data['headquater'] = True
        office = Office.objects.create(**validated_data)
        return company.id

    class Meta:
        model = Company
        fields = ['name', 'street', 'postal_code', 'city', 'monthly_rent']


class OfficeSerializer(serializers.ModelSerializer):
    '''
        Create office and list offices serializer
    '''

    def create(self, validated_data):
        return Office.objects.create(**validated_data)

    class Meta:
        model = Office
        fields = '__all__'


class OfficeDetailSerializer(serializers.ModelSerializer):
    '''
        Get office detail of company headquater serializer
    '''

    id = serializers.SerializerMethodField()
    company = serializers.SerializerMethodField()
    monthly_rent_sum = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.company.id

    def get_company(self, obj):
        return obj.company.name

    def get_monthly_rent_sum(self, obj):
        rents = Office.objects.filter(company=obj.company).values_list('monthly_rent', flat=True)
        return sum(rents)

    class Meta:
        model = Office
        fields = '__all__'


class ChangeCompanyHeadquaterSerializer(serializers.ModelSerializer):
    '''
        Update company headquater serializer
    '''

    def update(self, instance, validated_data):

        office = Office.objects.get(company=instance.company, headquater=True)
        office.headquater = False
        office.save()
        instance.headquater = validated_data.get('headquater', instance.headquater)
        instance.save()
        return instance

    class Meta:
        model = Office
        fields = ['headquater']
