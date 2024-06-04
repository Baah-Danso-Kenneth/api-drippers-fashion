from django.db import models

from apps.profiles.models import Category
from apps.sharedApps import TimeStampedModel
from django.contrib.auth import get_user_model


User = get_user_model()

class Styles(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="styles")
    title = models.CharField(max_length=100)
    style_image = models.ImageField(upload_to='style_images/')

    def __str__(self):
        return f"Style type is {self.title} and category {self.category}"


class FashionInspo(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    styles = models.ForeignKey(Styles, on_delete=models.CASCADE)
    images = models.ManyToManyField('FashionInspoImage')
    tags = models.CharField(max_length=200, blank=True)
    source_link = models.URLField(blank=True, null=True)

    @property
    def likes(self):
        return f"{self.likes.count()}"
    
    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exist():
            return ratings.aggregate(models.Avg('value'))['value__avg']
        return 0
    

class FashionInspoImage(models.Model):
    front_image = models.ImageField(upload_to="fashion_inspo_images/", default="fashion_inspo_images/default_front.png")
    back_image = models.ImageField(upload_to="fashion_inspo_images/", default="fashion_inspo_images/default_back.png")
    caption = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"Image {self.id} from Fashion Inspo"


class Comment(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user.first_name} on {self.created_at}"

class UserFashionInspoInteraction(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fashion_inspo = models.ForeignKey(FashionInspo, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'fashion_inspo')  


class Like(UserFashionInspoInteraction):
    likes = models.ForeignKey(FashionInspo, on_delete=models.CASCADE, related_name='likes')


class Rating(UserFashionInspoInteraction):
    ratings = models.ForeignKey(FashionInspo, on_delete=models.CASCADE, related_name='ratings')
    value = models.PositiveSmallIntegerField()

