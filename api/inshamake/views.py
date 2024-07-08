from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse
from .utils import allArticle_2, send_email

class InshamakeZinkuru(APIView):
    def get(self, request):
        #inkuru = asyncio.run(allArticle())
        inkuru_2 = list(allArticle_2())
        if inkuru_2:
            return Response(inkuru_2)
        else:
            return Response({"error": "Nta inkuru iri kuza"}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class SubscribeView(APIView):
    @method_decorator(require_http_methods(["POST"]))
    def post(self,request):
        try:
            data = json.loads(request.body)
            receiver = data.get("email")
            if not receiver:
                return JsonResponse({
                    "status":"error",
                    "message": "email is missing"
                }, status=400)
            result = send_email(receiver)
            return JsonResponse(result)
        except json.JSONDecodeError:
            return JsonResponse({})
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)
