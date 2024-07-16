from rest_framework.views import APIVew
from rest_framework.response import Response

class HelloApiView(APIVew):
    """Test API View"""

    def get(self , request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, delete)'
            'Is similar to a traditonal Django View'
        ]

        return Response({'Message': 'Hello' , 'an_apiview': an_apiview })
