from django import forms

class Sign_in_forms(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=50)
    pw= forms.CharField(widget=forms.PasswordInput, min_length=8)

class Register_forms(forms.Form):
    fname = forms.CharField(label="First Name", max_length=50)
    lname = forms.CharField(label="Last Name", max_length=50)
    email = forms.EmailField(label="Email Address", max_length=50)
    pw = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
    confpw = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
