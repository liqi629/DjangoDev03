import json
from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.filters import OrderingFilter
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Projects
from . import serializers

# Create your views here.


# 实现分页、排序、过滤
class ProjectList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # 过滤引擎,在setting里面已经有了
    filterset_fields = ['project_name', 'leader', 'tester']
    ordering_fields = ['id', 'project_name']

    def get(self, request):
        """获取项目列表"""
        return self.list(request)

    def post(self, request):
        """  
        :param request: 
        :return: 
        1.接收参数，转换类型
        2.校验
        3.数据库新增项目
        4.返回单个json（处理结果）
        """
        return self.create(request)


class ProjectDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericAPIView):
    queryset = Projects.objects.all()
    serializer_class = serializers.ProjectModelSerializer

    def get(self, request, pk):
        """获取指定项目信息"""
        return self.retrieve(request)

    def put(self, request, pk):
        """更新指定项目"""
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)
