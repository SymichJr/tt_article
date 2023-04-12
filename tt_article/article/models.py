from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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


