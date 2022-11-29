# 파일 이름은 다른 이름으로 해도 괜찮다.
# import할 때 파일이름을 잘 맞춰주면 된다.

from django.forms import ModelForm
from community.models import Article

class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'title', 'contents', 'url', 'email'] 