from django.db import models
# from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128, default="Title")
    author = models.CharField(max_length=256, default="Author")
    link = models.URLField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-creation_date"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    # def get_absolute_url(self):
    #     return reverse('posts:post', kwargs={'id': self.id})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=128, default="comment author")
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"{self.author} {self.post.title}"

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
