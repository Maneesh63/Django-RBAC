from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken
from django.contrib.auth import get_user_model
from rbac.models import product
from rbac.permissions import HasPermission
from rbac.permission_constants import Permissions

User = get_user_model()


class SignupView(APIView):
    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            return Response({"detail": "Username, email, and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(email=email).exists():
            return Response({"detail": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        
        
        user.save()

        return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

       
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
        
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)




class productsView(APIView):
    permission_classes = [HasPermission]

    required_permissions = {
        'GET': Permissions.VIEW_PRODUCT,
        'POST': Permissions.ADD_PRODUCT,
        'PUT': Permissions.EDIT_PRODUCT,
        'DELETE': Permissions.DELETE_PRODUCT,
    }
    
    def post(self, request):
        user = request.user
        name = request.data.get("name")
        description = request.data.get("description")
        price = request.data.get("price")
        stock = request.data.get("stock")

        if not name or not description or not price or not stock:
            return Response({"detail": "Name, description, price, and stock are required."}, status=status.HTTP_400_BAD_REQUEST)

        product_instance = product.objects.create(
            user=user,
            name=name,
            description=description,
            price=price,
            stock=stock
        )
        
        product_instance.save()

        return Response({"detail": "Product created successfully."}, status=status.HTTP_201_CREATED)