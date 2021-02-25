from django.db import models
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File

def compress(image):
    basewidth = 700
    im = Image.open(image)
    wpercent = (basewidth / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((basewidth, hsize), Image.ANTIALIAS)
    im_io = BytesIO()
    im.save(im_io, 'PNG', optimize=True)
    new_image = File(im_io, name=image.name)
    return new_image

class Direction(models.Model):
    title = models.CharField(max_length=30)
    importance = models.IntegerField(blank=True)


    def __str__(self):
        return self.title


class Grade(models.Model):
    title = models.CharField(max_length=100)
    Direction = models.ForeignKey(Direction, related_name='grades', on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    img = models.ImageField(blank=True)
    position = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        new_image = compress(self.img)
        self.img = new_image
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
