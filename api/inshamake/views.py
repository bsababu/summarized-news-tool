from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import summarize

class InshamakeZinkuru(APIView):
    def get(self, request):
        inkuru = request.query_params.get('inkuru', None)
        