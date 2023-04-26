from django.shortcuts import render, redirect
from TestApp.models import register_db, company_db, emp_db
# from django.core.mail import send_mail
from django.conf import settings
from TestApp.serializers import registerSerializer, CompanySerializer, EmpSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, filters
# from rest_framework import mixins
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import (
    UserRateThrottle,
    AnonRateThrottle,
    ScopedRateThrottle,
)
# from TestApp.throttle import user_throttle
from TestApp.pagination import Custom, Limit
from TestApp.serializers import myUserSerializer, myRegisterSerializer
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView


"""Function based APIs views """
# @api_view(['GET', 'POST'])
# def getdata(request):
#     if request.method == "GET":
#         get1 = register_db.objects.all()
#         serializer = registerSerializer(get1, many=True)
#         return Response(serializer.data)
#     if request.method == "POST":
#         serializer = registerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def getdata1(request, pk):
#     if request.method == 'PUT':
#         get2 = register_db.objects.get(pk=pk)
#         serializer = registerSerializer(get2, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#     if request.method == 'DELETE':
#         get3 = register_db.objects.get(pk=pk)
#         get3.delete()
#     return Response("Data Deleted sucessfully")


"""Class based APIs views"""
class get_data(APIView):
    def get(self, request):
        get1 = register_db.objects.all()
        serializer = registerSerializer(get1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = registerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class update_data(APIView):
    def get(self, request, pk):
        get1 = register_db.objects.all()
        serializer = registerSerializer(get1, many=True)
        return Response(serializer.data)

    def put(self, request, pk):
        get2 = register_db.objects.get(pk=pk)
        serializer = registerSerializer(get2, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        get3 = register_db.objects.get(pk=pk)
        get3.delete()
        return Response({"status": "Data Deleted sucessfully"})


"""Generic class based views"""
# class gen_data(generics.ListCreateAPIView):
#     queryset = register_db.objects.all()
#     serializer_class = registerSerializer

# class gen_data1(generics.RetrieveUpdateDestroyAPIView):
#     queryset = register_db.objects.all()
#     serializer_class = registerSerializer


"""mixins class based views"""
# class mix_data(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = register_db.objects.all()
#     serializer_class = registerSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class mix_data1(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = register_db.objects.all()
#     serializer_class = registerSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


"""Home page"""
def home(request):
    return render(request, "home.html")

"""Storing data in django databse"""
def test(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        obj = register_db.objects.create(
            fullname=fullname,
            username=username,
            email=email,
            phone=phone,
            address=address,
        )
        obj.save()
        """sending mail"""
        # send_mail(
        #     'Application status ', #subject
        #     f'Hello Mr.{username} \nWe are curently reviewing your application once it done. we will communicate through the email.', #body
        #     settings.EMAIL_HOST_USER, #sender
        #     [email], #receiver
        #     fail_silently=False,
        # )
        return redirect("userdata")
    return render(request, "index.html")


"""displaying userdata in html page"""
def userdata(request):
    users = register_db.objects.all()
    obj = {"user_obj": users}
    return render(request, "data.html", obj)


"""To update userdata"""
def update(request, id):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        users = register_db.objects.get(id=id)
        users.fullname = fullname
        users.username = username
        users.email = email
        users.phone = phone
        users.address = address
        users.save()
        return redirect("userdata")
    users = register_db.objects.get(id=id)
    obj = {"user_obj": users}
    users.save()
    return render(request, "update.html", obj)


"""To Delete userdata"""
def delete(request, id):
    users = register_db.objects.get(id=id)
    users.delete()
    return redirect("userdata")
"""END"""


"""creating class APIviews for company data"""
# class comp_getdata(APIView):
#     def get(self, request):
#         get1 = company_db.objects.all()
#         serializer = CompanySerializer(get1, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class comp_updatedata(APIView):
#     def get(self, request, pk):
#         get1 = company_db.objects.get(pk=pk)
#         serializer = CompanySerializer(get1)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         get2 = company_db.objects.get(pk=pk)
#         serializer = CompanySerializer(get2, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk):
#         get3 = company_db.objects.get(pk=pk)
#         get3.delete()
#         return Response({
#             "status": "Data Deleted sucessfully"
#             })


"""creating class APIviews for Employee data"""
# class emp_getdata(APIView):
#     def get(self, request):
#         get1 = emp_db.objects.all()
#         serializer = EmpSerializer(get1, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EmpSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# class emp_updatedata(APIView):
#     def get(self, request, pk):
#         get1 = emp_db.objects.get(pk=pk)
#         serializer = EmpSerializer(get1)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         get2 = emp_db.objects.get(pk=pk)
#         serializer = EmpSerializer(get2, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self, request, pk):
#         get3 = emp_db.objects.get(pk=pk)
#         get3.delete()
#         return Response({
#             "status": "Data Deleted sucessfully"
#             })


"""Generic class based views for company"""
class comp_gen_data(generics.ListCreateAPIView):
    queryset = company_db.objects.all()
    serializer_class = CompanySerializer
    pagination_class = Limit        # limit offset pagination
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]        # permissions

    """throttling"""
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # default throttle declaration class
    # throttle_classes = [ScopedRateThrottle]       # scope rate throttle
    # throttle_scope = 'myuser'
    # throttle_classes = [user_throttle]        # custom throttle

    """filtering"""
    # filter_backends = [DjangoFilterBackend]       # for DjangoFilterBackend
    # filterset_fields = ['company_name', 'company_type', 'company_phone', 'company_email', 'company_address']
    filter_backends = [filters.SearchFilter]  # SearchFilter
    search_fields = [
        "company_name",
        "company_type",
        "company_phone",
        "company_email",
        "company_address",
    ]
    # filter_backends = [filters.OrderingFilter]       # OrderingFilter
    # ordering_fields = '__all__'


class comp_gen_data1(generics.RetrieveUpdateDestroyAPIView):
    queryset = company_db.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


"""generic class based views for employee"""
class emp_gen_data(generics.ListCreateAPIView):
    queryset = emp_db.objects.all()
    serializer_class = EmpSerializer   
    pagination_class = Custom       # Custom Pagination
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]        # permissions

    """throttling"""
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # throttle class
    # throttle_classes = [ScopedRateThrottle]       # scope rate throttle
    # throttle_scope = 'myuser'
    # throttle_classes = [user_throttle]        # custom throttle

    """filtering"""
    # filter_backends = [DjangoFilterBackend]          # for DjangoFilterBackend
    # filterset_fields = ['emp_id', 'emp_fullname', 'emp_email', 'emp_phone', 'emp_companyname', 'emp_role', 'emp_domain', 'emp_location', 'emp_status']
    filter_backends = [filters.SearchFilter]     # SearchFilter
    search_fields = [
        "emp_id",
        "emp_fullname",
        "emp_email",
        "emp_phone",
        "emp_companyname",
        "emp_role",
        "emp_domain",
        "emp_location",
        "emp_status",
    ]
    # filter_backends = [filters.OrderingFilter]          # OrderingFilter
    # ordering_fields = '__all__'


class emp_gen_data1(generics.RetrieveUpdateDestroyAPIView):
    queryset = emp_db.objects.all()
    serializer_class = EmpSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


"""mixins class based views for company"""
# class comp_mix_data(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = company_db.objects.all()
#     serializer_class = CompanySerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class comp_mix_data1(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = company_db.objects.all()
#     serializer_class = CompanySerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


"""mixins class based view for employee"""
# class emp_mix_data(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = emp_db.objects.all()
#     serializer_class = EmpSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class emp_mix_data1(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = emp_db.objects.all()
#     serializer_class = EmpSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


"""creating new user"""
class RegisterAPI(generics.GenericAPIView):
    serializer_class = myRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": myUserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


"""creating new login """
class LoginAPI(KnoxLoginView):
    permission_classes = permissions.AllowAny

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
