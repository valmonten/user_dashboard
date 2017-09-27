from django import forms

class Message_Form(forms.Form):
    msg = forms.CharField(label="", widget=forms.Textarea)

class Comment_Form(forms.Form):
    cmt = forms.CharField(label="", max_length=255)

class Edit(forms.Form):
    email = forms.EmailField(label="Email", max_length=50)
    fname = forms.CharField(label='First Name', max_length=50)
    lname = forms.CharField(label='Last Name', max_length=50)

class Change_Pw(forms.Form):
    new_pw = forms.CharField(widget=forms.PasswordInput, min_length=8)
    pw_conf = forms.CharField(widget=forms.PasswordInput)