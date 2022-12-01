from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    # email 필드 추가
    email = forms.EmailField(required=True)

    class Meta:
        # 장고 제공
        model=User
        fields = ('username','email', 'password1', 'password2')