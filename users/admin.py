# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from users.models import User
from django import forms

class User_creation_form( UserCreationForm ):
	"""
	Un formulario para crear los usuarios. Incluye todos los campos requeridos
	"""
	password1 = forms.CharField( label='Password', widget=forms.PasswordInput )
	password2 = forms.CharField( label='Password Confirmation',
			widget=forms.PasswordInput )
	generate_token = forms.BooleanField()

	class Meta:
		model = User
		fields = ( 'username', 'email', 'first_name', 'last_name' )

	def clean_username( self ):
		"""
		Revisa si el nombre de usuario no esta registrado
		"""
		username = self.cleaned_data[ "username" ]

		try:
			User._default_manager.get( username = username )
		except User.DoesNotExist:
			return username
		raise forms.ValidationError( self.error_messages[ 'duplicate_username' ] )

	def clean_password2( self ):
		"""
		Revisa si las dos contrasenas concuerdan
		"""
		password1 = self.cleaned_data.get( "password1" )
		password2 = self.cleaned_data.get( "password2" )

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError( "Passwords do not match." )
		return password2

	def save( self, commit=True ):
		"""
		Guarda el usuario que se registro con el formulario
		"""
		user = super( UserCreationForm, self ).save( commit=False )
		user.set_password( self.cleaned_data[ "password1" ] )
		if commit:
			user.save()
		return user


class User_change_form( UserChangeForm ):
	#TODO: traducir esta linea
	password = ReadOnlyPasswordHashField( label="password",
		help_text="""Raw passwords are not stored, so there is no way to see this
		user's password, but you can change the password using <a href=\"password/\">
		this form</a>.""" )

	class Meta( UserChangeForm.Meta ):
		model = User
		fields = ( 'username', 'email', 'password', 'first_name', 'last_name',
				'is_active', 'is_staff', 'is_superuser', 'user_permissions', )

	def clean_password( self ):
		"""
		Independientemete de los que ponga en el campo regresa el valor inicial
		"""
		return self.initial[ 'password' ]


class User_admin( UserAdmin ):
	"""
	Administrador custom para el modelo de Users
	"""
	form = User_change_form
	add_form = User_creation_form

	list_display = ( 'username', 'email', 'is_staff', 'is_superuser' )
	list_filter = ( 'is_superuser', )

	fieldsets = (
		(
			None, {
				'fields': (
					'username', 'email', 'password', 'first_name',
					'last_name',
				)
			}
		),
		(
			'Permissions', {
				'fields': (
					'is_active', 'is_staff'
				)
			}
		),
	)

	list_display = ( 'username', 'email', 'is_active', 'is_staff' )

	add_fieldsets = (
		( None, {
				'classes': ( 'wide', ),
				'fields': ( 'username', 'email', 'password1', 'password2',
					'first_name', 'last_name', 'is_staff', )
			}
		),
	)

	search_fields = ( 'email', 'username', 'first_name', 'last_name' )
	ordering = ( 'username', 'email' )
	filter_horizontal = ()

admin.site.register( User, User_admin)
