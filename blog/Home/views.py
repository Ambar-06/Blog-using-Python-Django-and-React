from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BaseAuthentication

# Create your views here.
def test(request):
    data = {'Status' : 200}
    return HttpResponse(json.dumps(data))

@api_view(['POST'])
@authentication_classes([SessionAuthentication, BaseAuthentication])
@permission_classes([IsAuthenticated])
def signUp(request):
    pass