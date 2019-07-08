# django imports 
from django.conf.urls import url

# local imports
from company.api.views import CompanyView, OfficeView, ChangeCompanyHeadquaterView


urlpatterns = [
    url(r'^offices/$', OfficeView.as_view(), name='office'),
    url(r'^companies/$', CompanyView.as_view(), name='company'),
    url(r'^companies/(?P<cmp_id>[-\w]+)/_change_headquater/(?P<office_id>[-\w]+)/$', ChangeCompanyHeadquaterView.as_view(), name='change-company-headquater'),
]
