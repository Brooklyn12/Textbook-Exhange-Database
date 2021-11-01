from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Admin
        fields = '__all__'


class TextbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Textbook
        fields = '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Buyer
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = '__all__'


class Chat_WithSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chat_With
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.University
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Complaint
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Schedule
        fields = '__all__'


class MeetUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meet_Up_Info
        fields = '__all__'


class SetCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Set_Cost
        fields = '__all__'


class TCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TC
        fields = '__all__'
