from django.utils.deprecation import MiddlewareMixin
from django.conf import settings

class GetConstantData(MiddlewareMixin):
    def process_template_response(self, request, response):
        response.context_data.update(settings.SITE_CONFIG)
        return response
