from django import forms
from .models import InRecord, OutRecord, Org, Actor

class inRecForm(forms.Form):
    rec_num = forms.CharField(label='№ Вх. Док.', widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '\d+(-\d+)?'}), max_length=50)
    rec_org = forms.ModelChoiceField(queryset=Org.objects.all(), widget=forms.Select(attrs={'class':'form-control selectpicker', 'data-live-search': 'true' }), empty_label=None, label='Корреспондент')
    out_num = forms.CharField(label='№ исх. корреспондента', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    out_date = forms.DateField(label='Дата исх. корр.', widget=forms.DateInput(attrs={'class': 'form-control'}))
    rec_desc = forms.CharField(label='Краткое содержание', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    rec_actor = forms.ModelChoiceField(queryset=Actor.objects.filter(is_active=True), widget=forms.Select(attrs={'class':'form-control selectpicker'}), empty_label="б/и", label='Исполнитель', required=False)    
    control_date = forms.DateField(label='Дата исполнения', widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)
    rec_deal = forms.IntegerField(label="№ дела", widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    action_date = forms.DateField(label='Исполнено', widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)

class markDoneForm(forms.Form):
    rec_actor = forms.ModelChoiceField(queryset=Actor.objects.filter(is_active=True), widget=forms.Select(attrs={'class':'form-control selectpicker'}), empty_label="б/и", label='Исполнитель', required=False)    
    control_date = forms.DateField(label='Дата исполнения', widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)
    action_date = forms.DateField(label='Исполнено', widget=forms.DateInput(attrs={'class': 'form-control'}), required=False)

class actorsForm(forms.Form):
    act_name = forms.CharField(label='Имя', max_length=200)
    act_surname = forms.CharField(label='Фамилия', max_length=200)
    is_active = forms.BooleanField(label='активен')
