from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Explicitly use Cloudinary storage for this field
    cover_image = models.ImageField(
        upload_to='albums/',
        storage=MediaCloudinaryStorage()
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title