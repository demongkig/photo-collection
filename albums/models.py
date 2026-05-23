from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import cloudinary.uploader

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
    
@receiver(pre_delete, sender=Album)
def delete_cloudinary_image(sender, instance, **kwargs):
    if instance.cover_image:
        try:
            # 1. Try extracting the target ID directly if it's a CloudinaryField
            if hasattr(instance.cover_image, 'public_id'):
                target_id = instance.cover_image.public_id
            else:
                # 2. If it's a regular file field, get its string name and clean it up
                # This strips away the extension (like .jpg) which Cloudinary doesn't want
                file_path = str(instance.cover_image)
                target_id = file_path.split('.')[0] if '.' in file_path else file_path
            
            # Send the exact clean reference ID to Cloudinary to drop the file
            cloudinary.uploader.destroy(target_id)
            print(f"Successfully deleted Cloudinary file: {target_id}")
            
        except Exception as e:
            # Keeps the app from crashing if a file path is missing on the cloud
            print(f"Cloudinary file deletion skipped or failed: {e}")