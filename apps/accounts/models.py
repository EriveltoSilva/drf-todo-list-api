import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    slug = models.SlugField(unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs) -> None:
        email_username = self.email.split('@')
        if not self.first_name:
            self.first_name = email_username[0]

        if not self.slug:
            self.slug = slugify(email_username)
        if not self.username:
            self.username = email_username

        return super(User, self).save(*args, **kwargs)


class Profile(models.Model):
    GENDER = (("MASCULINO", "MASCULINO"), ("FEMININO", "FEMININO"),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default=GENDER[0])
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="profile", blank=True)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        ordering = ["user"]

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return self.user.get_full_name()

    def imageURL(self):
        try:
            url = self.image.url
        except ValueError:
            url = "/static/assets/images/user.png"
        return url
