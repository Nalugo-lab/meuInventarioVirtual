from django.conf import settings
from django.db import models
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils import timezone


from django.db import models
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USER_STATUS = [
        (1, "Account created"),
        (2, "Active account"),
        (3, "Active"),
        (4, "Disabled")
    ]

    username = None
    name = models.CharField(("name"), max_length=150, blank=True)
    surname = models.CharField(("surname"), max_length=150, blank=True)
    email = models.EmailField(("email address"), unique=True)
    cellphone_number = models.CharField(max_length=11)
    is_staff = models.BooleanField(
        ("staff status"),
        default=False,
        help_text=(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    email_verified = models.BooleanField(default=False)
    account_status = models.IntegerField(choices=USER_STATUS, default=1)
    datetime_joined = models.DateTimeField(("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def clean(self):
        super().clean()
        self.email = self.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()


class Client(models.Model):

    name = models.CharField(("name"), max_length=150, blank=True)
    surname = models.CharField(("surname"), max_length=150, blank=True)
    email = models.EmailField(("email address"), unique=True)
    cellphone_number = models.CharField(unique=True, max_length=11)
    datetime_joined = models.DateTimeField(("date joined"), default=timezone.now)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Criador"), on_delete=models.PROTECT)