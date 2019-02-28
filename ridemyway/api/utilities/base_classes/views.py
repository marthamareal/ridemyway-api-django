""" Base classes for Views """

from rest_framework import generics, status
from rest_framework.response import Response

from ..helpers.renderers import ApiRenderer
from ..helpers.success_messages import success_message


class BaseModelView(generics.ListCreateAPIView):
    """ Base class for views that don't need a primary key for the object"""

    renderer_classes = ApiRenderer,

    def post(self, request, *args, **kwargs):
        """ Method for creating an object"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = {
            'data': serializer.data,
            'status': status.HTTP_201_CREATED,
            'message': success_message['created'].format(self.model_name)
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """ Method for getting a list of objects"""

        queryset = self.filter_queryset(self.get_queryset())
        if queryset.count() == 0:
            return Response({'message': 'No data available'})

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            'data': serializer.data,
            'status': 200,
            # 'message': success_message['fetched'].format(self.model_name)
        }
        return Response(response_data, status=status.HTTP_200_OK)


class BaseSingleModelView(generics.RetrieveUpdateDestroyAPIView):
    """ Base class for views with a primary key for the object"""
    
    renderer_classes = ApiRenderer,

    def retrieve(self, request, *args, **kwargs):
        """ Method for retrieving a single object"""

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        response_data = {
            'data': serializer.data,
            'status': 200,
            # 'message': success_message['fetched'].format(self.model_name)
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """ Method for updating an object"""

        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        response_data = {
            'data': serializer.data,
            'status': 200,
            'message': success_message['updated'].format(self.model_name)
        }
        return Response(response_data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """ Method for deleting an object"""

        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = {
            'status': 200,
            'message': success_message['deleted'].format(self.model_name)
        }
        return Response(response_data, status=status.HTTP_200_OK)
