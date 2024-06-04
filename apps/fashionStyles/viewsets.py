from collections import defaultdict
from django.shortcuts import render
from rest_framework.response import Response
from .models import Category, Styles
from apps.profiles.serializers import CategorySerializer, StyleSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action


class StylesCategoryViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def styles_by_category(self, request):
        try:
            categories = Category.objects.all()
            all_style_category = defaultdict(list)
            for category in categories:
                styles = Styles.objects.get()
                styles_serialized = StyleSerializer(styles, many=True).data
                all_style_category[category.name].extend(styles_serialized)

            return Response(dict(all_style_category), status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

