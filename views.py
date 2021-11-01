from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from . import serializers
from . import models


class AccountList (APIView):
    def get(self, request, format=None):
        acc = models.Account.objects.all()
        serializer = serializers.AccountSerializer (acc, many=True)
        return Response (serializer.data)

    def post(self, request, format=None):
        serializer = serializers.AccountSerializer (data=request.data)
        if serializer.is_valid ( ):
            serializer.save ( )
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail (APIView):

    def get(self, request, pk, format=None):
        acc = models.Account.objects.get (pk=pk)
        serializer = serializers.AccountSerializer(acc)
        return Response (serializer.data)

    def put(self, request, pk, format=None):
        acc = models.Account.objects.filter(pk=pk).first()
        serializer = serializers.AccountSerializer(acc, data=request.data)
        print(acc)
        if serializer.is_valid ( ):
            print(request.data)
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        acc = models.Account.objects.filter (pk=pk)
        acc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# need to edit and add views.
# below are all simplistic dummy views
class TextbookViewSet(viewsets.ModelViewSet):
    queryset = models.Textbook.objects.all().order_by('id')
    serializer_class = serializers.TextbookSerializer


class AdminViewSet(viewsets.ModelViewSet):
    queryset = models.Admin.objects.all().order_by('username')
    serializer_class = serializers.AdminSerializer
    
    
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = models.Buyer.objects.all().order_by('username')
    serializer_class = serializers.BuyerSerializer
    
class SellerViewSet(viewsets.ModelViewSet):
    queryset = models.Seller.objects.all().order_by('username')
    serializer_class = serializers.SellerSerializer
    
    
class Chat_WithViewSet(viewsets.ModelViewSet):
    queryset = models.Chat_With.objects.all()
    serializer_class = serializers.Chat_WithSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer

class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = models.Complaint.objects.all()
    serializer_class = serializers.ComplaintSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class MeetUpViewSet(viewsets.ModelViewSet):
    queryset = models.Meet_Up_Info.objects.all()
    serializer_class = serializers.MeetUpSerializer

class Set_CostViewSet(viewsets.ModelViewSet):
    queryset = models.Set_Cost.objects.all()
    serializer_class = serializers.MeetUpSerializer
    
class Set_CostViewSet(viewsets.ModelViewSet):
    queryset = models.TC.objects.all()
    serializer_class = serializers.TCSerializer
