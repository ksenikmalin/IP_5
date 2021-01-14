from import_export import resources
from agency.models import Services


class ServicesResources(resources.ModelResource):
    class Meta:
        model = Services
