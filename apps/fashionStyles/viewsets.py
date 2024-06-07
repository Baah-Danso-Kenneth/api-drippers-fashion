from collections import defaultdict
from django.shortcuts import render
from rest_framework.response import Response
from .models import Category, Styles
from apps.profiles.serializers import CategorySerializer, StyleSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action



class StylesCategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        categories = Category.objects.all()
        all_titles = set()

        # Collect unique titles across all categories
        for category in categories:
            styles = Styles.objects.filter(category=category)
            all_titles.update(style.title for style in styles)

        return Response({"titles": list(all_titles)}, status=status.HTTP_200_OK)
    
