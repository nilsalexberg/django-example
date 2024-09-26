from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

# Model category: name
class Category(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

# model Author: user, bio
class Author(models.Model):
  user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
  bio = models.TextField()

  def __str__(self):
    return self.user.username

# model Post: title, content, category, author, created_at
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  slug = models.SlugField(max_length=100, blank=True, null=True)

  def __str__(self):
    return self.title

  # auto slug on save
  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

# model comment: content, post, created_at
class Comment(models.Model):
  content = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content