from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API Views"""

    def get(self, request, format=None):
        """Resturns a list of APIView features"""


        an_apiview = [
                'Uses HTTP methods as function (get, post, patch, put, delete)',
                'Is Similar to the traditional Django View',
                'Gives you the most control over your application logic',
                'Is mapped manually to URLs',
        ]

        return Response({'message' : 'Hello', 'an_apiview': an_apiview})
