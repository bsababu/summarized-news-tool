from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import allArticle

class InshamakeZinkuru(APIView):
    def get(self, request):
        inkuru = allArticle()
        if inkuru:
            return Response(inkuru)
        else:
            return Response({"error": "Nta inkuru iri kuza"}, status=status.HTTP_400_BAD_REQUEST)
        