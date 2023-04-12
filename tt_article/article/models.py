from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SUBSCRIBER = 'subscriber'
    AUTHOR = 'author'
    USERS_ROLE =(
        (SUBSCRIBER, 'подписчик'),
        (AUTHOR, 'Автор'),
    )
    email = models.EmailField(
        'Электронная почта', unique=True, blank=False, max_length=254
    )
    role = models.CharField(
        'Роль', max_length=50, choices=USERS_ROLE, default='subscriber'
    )

    @property
    def is_subscriber(self):
        return self.role == 'subscriber'
    
    @property
    def is_author(self):
        return self.role == "admin"

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField('Pub date', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles'
    )
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.title


