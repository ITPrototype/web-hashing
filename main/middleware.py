# middleware.py

from django.utils.deprecation import MiddlewareMixin

class LogUserIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        from .models import UserAccessLog  # Import model dynamically

        ip_address = self.get_client_ip(request)
        UserAccessLog.objects.create(ip_address=ip_address)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
