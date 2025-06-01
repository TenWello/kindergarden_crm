from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, username, full_name, email, password=None, role=3, status=1):
        if not email:
            raise ValueError("Email required")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            full_name=full_name,
            email=email,
            role=role,
            status=status,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, email, password=None):
        user = self.create_user(
            username=username,
            full_name=full_name,
            email=email,
            password=password,
            role=1,     # 1 - Admin
            status=1    # 1 - Working
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_ADMIN = 1
    ROLE_CHEF = 2
    ROLE_MANAGER = 3

    ROLE_TYPE = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_CHEF, 'Cheef'),
        (ROLE_MANAGER, 'Manager'),
    ]
    STATUS_TYPE = [
        (1, 'Working'),
        (2, 'Lay Off'),
        (3, 'On Vacation'),
        (4, 'On Probation'),
    ]

    username = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.PositiveSmallIntegerField(choices=ROLE_TYPE, default=ROLE_CHEF)
    status = models.PositiveSmallIntegerField(choices=STATUS_TYPE, default=1)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    objects = UserManager()

    def __str__(self):
        return f"{self.full_name} ({self.get_role_display()})"

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_chef(self):
        return self.role == self.ROLE_CHEF

    @property
    def is_manager(self):
        return self.role == self.ROLE_MANAGER
