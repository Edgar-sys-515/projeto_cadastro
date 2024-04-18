from django.forms import ModelForm
from .models import Investimento # aqui se importa as classes que estao em models, banco de dados



class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__' # os campos que estao exibidos sao all, poderia ser alguns caso queira, tem q passar como lista
        #fields = ['valor']