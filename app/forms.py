from django import forms


class UserForm(forms.Form):
    name= forms.CharField()
    phone = forms.IntegerField()


class RegForm(forms.Form):
    name= forms.CharField()
    phone = forms.IntegerField()
    age = forms.IntegerField()
    adress = forms.CharField()


class CrudForm(forms.Form):
    phone_number = forms.CharField()
    create_timestamp = forms.CharField()
    update_timestamp = forms.CharField()
    created_by = forms.CharField()


class UpdateForm(forms.Form):
    phone_number = forms.CharField()
    create_timestamp = forms.CharField()
    update_timestamp = forms.CharField()
    created_by = forms.CharField()




    
