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
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}), max_length=200)
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}), max_length=200)
    is_active = forms.BooleanField(label='активен', required=False)
    pk = forms.IntegerField(widget = forms.HiddenInput(), required = False)

class orgsForm(forms.Form):
    org_name = forms.CharField(label='Название организации', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название организации'}), max_length=200)
    pk = forms.IntegerField(widget = forms.HiddenInput(), required = False)

#test3
