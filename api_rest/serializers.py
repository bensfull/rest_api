from rest_framework import serializers


from .models import User, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'autor', 'titulo', 'conteudo', 'data_criacao']

class UserSerializer(serializers.ModelSerializer):
    
    meus_posts = PostSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        
