from django.db import models

class User(models.Model):
    user_nickname = models.CharField(max_length=100, primary_key=True, default='')
    user_name =  models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default= 1)
    
    def __str__(self):
        return f'Nickname: {self.user_nickname} | Email: {self.user_email}'
    

# O novo modelo de Post

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    # LIGAÇÃO: Cada post precisa de um autor (User)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meus_posts')

    def __str__(self):
        return self.titulo
