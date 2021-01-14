from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

#def get_deleted_user():
    #return get_user_model().objects.get_or_create(username='deleted')[0]

class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, first_name, password, **other_fields):
        
        if not email:
            raise ValueError(_('You must provide an email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, username, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff=True'))
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must be assigned to is_superuser=True'))

        self.create_user(email, username, first_name, password, **other_fields)

class ThreadUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-is_staff',)

class Thread (models.Model):
    
    STYLES = (
        ('embroidery floss', 'Embroidery Floss'),
        ('craft cord', 'Craft Cord'),
        ('waxed cord', 'Waxed Cord'),
    )

    brand = models.CharField(max_length=200)
    style = models.CharField(max_length=200, choices=STYLES)
    #TODO make this validate numbers above 0
    id_number = models.CharField(max_length=20)
    color_name = models.CharField(max_length=250, null=True)
    added_by = models.ForeignKey(ThreadUser, on_delete=models.CASCADE)
    objects = models.Manager() #default manager

    class Meta:
        ordering = ('brand',)

    def __str__(self):
        return ('{0} {1} #{2}: {3}'.format(self.brand, self.style, self.id_number, self.color_name))    


class OwnedThread (models.Model):
    owned_thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    owned_by = models.ForeignKey(ThreadUser, on_delete=models.CASCADE)
    length_owned = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('owned_by',)
    
    def __str__(self):
        return self.owned_thread.__str__()
 
class Collection (models.Model):   

    #get only public collections
    class PublicManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='public')

    STATUS = (
        ('public', 'Public'),
        ('private', 'Private'),
    )

    #TODO at some point, create a way to generate a different slug 
    #without having to deal with all this weirdness (try to make one based on title, otherwise generate a random one)
    #generate based on id number in the database?
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.CharField(max_length=400)
    added_by = models.ForeignKey(ThreadUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS)
    threads = models.ManyToManyField(Thread)
    objects = models.Manager() #default manager
    public_manager = PublicManager()

    def get_absolute_url(self):
        return reverse('thread:collection_single', args=[self.slug])
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)     
