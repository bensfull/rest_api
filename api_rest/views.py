from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer, PostSerializer


# Documentação (Swagger): Para que outros desenvolvedores saibam como usar sua API sem precisar ler todo o seu código Python.
from drf_spectacular.utils import extend_schema



import json


@api_view(['GET'])

def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])

def get_by_nick(request, nick):
    
    try:
        user = User.objects.get(pk=nick)
        
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        
        serializer = UserSerializer(user)
        
        return Response(serializer.data)
    
    
#OUTRA MANEIRA DE FAZER O PUT


    if request.method == 'PUT':
        
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


# CRIANDO O CRUD
    
@api_view(['GET','POST','PUT','DELETE'])

def user_manager(request):
    
    if request.method == 'GET':
        
        try:
            if request.GET['user'] :      #check if there is a get paramet callled 'user' (/?user=xxxx)
                
                user_nickname = request.GET['user']
                
                try:
                    
                    user = User.objects.get(pk=user_nickname)
                    
                except:
                    
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                
                serializer = UserSerializer(user)
                
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
# CRIANDO DADOS
    
    if request.method == 'POST':
        
        new_user = request.data
        
        serializer = UserSerializer(data=new_user)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
        
# EDITANDO DADOS

    if request.method == 'PUT':
        
        nickname = request.data['user_nickname']
        
        try:
        
            update_user = User.objects.get(pk=nickname)
            
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        print(request.data)
        
        serializer = UserSerializer(update_user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':
        
        try:
        
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
            
            user_to_delete.delete()
            
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

@extend_schema(request=PostSerializer) # Isso diz ao Swagger para mostrar os campos do Post
@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            # Aqui precisamos dizer quem é o autor do post manualmente
            # assumindo que o nickname vem no corpo do request
            nickname = request.data.get('autor_nickname')
            try:
                autor = User.objects.get(pk=nickname)
                serializer.save(autor=autor)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)