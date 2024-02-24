from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
#from django.core.mail import send_mail
#from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




class PersonelGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = Personel.objects.all()
                serializer_class = PersonelSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Personel.objects.all()
                    serializer = PersonelSerializer(snippets, many=True)
                    return Response(serializer.data)


class PersonelDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Personel.objects.get(pk=pk)
        except Personel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PersonelSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = PersonelSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










class AvancementGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = Avancement.objects.all()
                serializer_class = AvancementSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Avancement.objects.all()
                    serializer = AvancementSerializer(snippets, many=True)
                    return Response(serializer.data)


class AvancementDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Avancement.objects.get(pk=pk)
        except Avancement.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AvancementSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AvancementSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








class AbsanceGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = Absance.objects.all()
                serializer_class = AbsanceSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Absance.objects.all()
                    serializer = AbsanceSerializer(snippets, many=True)
                    return Response(serializer.data)


class AbsanceDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Absance.objects.get(pk=pk)
        except Absance.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AbsanceSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AbsanceSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class SanctionGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = Sanction.objects.all()
                serializer_class = SanctionSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Sanction.objects.all()
                    serializer = SanctionSerializer(snippets, many=True)
                    return Response(serializer.data)


class SanctionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Sanction.objects.get(pk=pk)
        except Sanction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SanctionSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SanctionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class RandementGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = Randement.objects.all()
                serializer_class = RandementSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Randement.objects.all()
                    serializer = RandementSerializer(snippets, many=True)
                    return Response(serializer.data)


class RandementDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Randement.objects.get(pk=pk)
        except Randement.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RandementSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = RandementSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CongeGlobal(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
                #authentication_classes = [TokenAuthentication]
                #permission_classes = [IsAuthenticated]
                queryset = Conge.objects.all()
                serializer_class = CongeSerializer

                def post(self, request, *args, **kwargs):
                    return self.create(request, *args, **kwargs)

                def get(self, request, format=None):
                    snippets = Conge.objects.all()
                    serializer = CongeSerializer(snippets, many=True)
                    return Response(serializer.data)


class CongeDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Conge.objects.get(pk=pk)
        except Conge.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CongeSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CongeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)