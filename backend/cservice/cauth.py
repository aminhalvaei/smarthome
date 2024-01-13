# from rest_framework.authentication import BaseAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# class APIKeyAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         api_key = request.headers.get('API-Key')
#         if api_key == 'your_api_key':  # Replace with your actual API key
#             return ('api_user', None)
#         return None
