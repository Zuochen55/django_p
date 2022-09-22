from django import forms
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class UserModleForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart_id"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

class VipModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label = "mobile",
        validators=[ RegexValidator(r'^1[3-9]\d{9}$', 'wrong number')])

    class Meta:
        model = models.VipNumber
        fields = ["mobile", "price", "level", "status"]
        # fields = "__all__"
        # exclude = ["mobile"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        exists = models.VipNumber.objects.filter(mobile=text_mobile).exists()

        if exists:
            raise ValidationError("The number already exists")
        return text_mobile

class VipEditModelForm(forms.ModelForm):
    mobile = forms.CharField(
        label = "mobile",
        validators=[ RegexValidator(r'^1[3-9]\d{9}$', 'wrong number')])

    class Meta:
        model = models.VipNumber
        fields = "__all__"
        # exclude = ["mobile"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}

    def clean_mobile(self):
        text_mobile = self.cleaned_data["mobile"]
        print(self.instance.pk)
        exists = models.VipNumber.objects.exclude(id=self.instance.pk).filter(mobile=text_mobile).exists()

        if exists:
            raise ValidationError("The number already exists")
        return text_mobile