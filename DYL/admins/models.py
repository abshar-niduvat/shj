from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class MyAccountManager(BaseUserManager):
	def create_user(self, username, name, password=None):
		if not username:
			raise ValueError('Users must have an Usernumber')
		if not name:
			raise ValueError('Users must have a Name')

		user = self.model(
			username=username,
			name=name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, name, password):
		user = self.create_user(
			username=username,
			password=password,
			name=name,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	username 				= models.CharField(verbose_name="Username", max_length=100, unique=True)
	name 				    = models.CharField(max_length=30)
	type 					= models.CharField(max_length=50)
	unit				= models.CharField(max_length=50)
	cluster				= models.CharField(max_length=50)
	zone				= models.CharField(max_length=50)
	phone					= models.CharField(max_length=50)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['name']

	objects = MyAccountManager()

	def __str__(self):
		return self.name

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True



from django.db import models

# Create your models here.
