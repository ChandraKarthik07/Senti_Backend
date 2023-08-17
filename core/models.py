


from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
import uuid
import pytz
# from viewflow.fields import CompositeKey
from oauth2_provider.models import AbstractApplication

class CustomUserManager(UserManager):
    pass

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email=models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message="Phone number must be entered in the form of +919999999999.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    # otp = models.CharField(max_length=6, null=True, blank=True)

    objects = CustomUserManager()
    # USERNAME_FIELD="email"
    # REQUIRED_FIELDS=[]

    def __str__(self):
        return f"{self.username}-{self.id}"
    class meta:
        db_table = 'User'


User._meta.get_field('groups').remote_field.related_name = 'user_replica_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_replica_permissions'



class CustomApplication(AbstractApplication):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
