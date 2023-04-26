from django.contrib.auth.models import User
from rest_framework import serializers
from TestApp.models import register_db, company_db, emp_db

"""Validators"""
# def username(value):
#     if value != Number:
#         raise serializers.ValidationError("You dont have give int values") 
#     return value

"""Taking serializers fields for validators"""
# class registerSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=200, validators=[username])
#     email = serializers.CharField(max_length=200)
#     address = serializers.CharField(max_length=200)

"""importing models fields"""    
"""Serializers Method fields"""
class registerSerializer(serializers.ModelSerializer):
    len_username = serializers.SerializerMethodField(read_only=True)   #declaring Serializers method field
    len_phone = serializers.SerializerMethodField(read_only=True)

    def get_len_username(self, obj):
        length = len(obj.username)
        return length

    def get_len_phone(self, obj):
        length = len(str(obj.phone))
        return length

    class Meta:
        model = register_db
        fields = "__all__"


"""Employee serializers class declaration"""
class EmpSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(source='get_company_name')  # to display foreign key name we declared in model
    user = serializers.SerializerMethodField(source='get_user')        # declare for foreign key name

    class Meta:
        model = emp_db
        fields = "__all__"

    def get_company_name(self, obj):
        display = str(obj.company_name)
        return display

    def get_user(self, obj):
        display = str(obj.user)
        return display


"""Company serializer class declaration"""
class CompanySerializer(serializers.ModelSerializer):
    # emp_fullname = serializers.SerializerMethodField(source='get_emp_fullname')  # to display foreign key name we declared serializer method
    employee = EmpSerializer(many=True, read_only=True)         # nested serializer method
    # employee = serializers.StringRelatedField(many=True)
    # employee = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # employee = serializers.SlugRelatedField(many=True, read_only=True, slug_field='emp_id')
    # employee = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='emp_gen_data1'
    # )

    class Meta:
        model = company_db
        fields = "__all__"   

    # def get_emp_fullname(self, obj):
    #     display = str(obj.emp_fullname)
    #     return display


"""Object validations"""    
# def validate(self, data):
#     if data["username"] == data["address"]:
#         raise serializers.ValidationError("Username and address should not be same")
#     elif len(data['username']) >= 5:
#         raise serializers.ValidationError("You dont have to take more than 5 characters")
#     elif register_db.objects.filter(email=data['email']).exists():
#         raise serializers.ValidationError("email alredy existed")
#     elif data['email'] == nullcontext:
#         raise serializers.ValidationError("dont leave the email field empty")
#     elif data['address'] != Number:
#         raise serializers.ValidationError("you may not give int value")
#     else:
#         return data

"""Field validations"""
# def validate_username(self, value):
#     if len(value) <= 4:
#         raise serializers.ValidationError('username must have min 4 characters')
#     return value

# def validate_address(self, value):
#     if value != Number:
#         raise serializers.ValidationError('you dont have to give int values')
#     return value

# User Serializer


class myUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class myRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user