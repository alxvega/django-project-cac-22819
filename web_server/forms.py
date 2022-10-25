from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True, min_length=4, max_length=10, widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'Username'
        }))

    password = forms.CharField(required=True, min_length=8, max_length=12, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'placeholder': 'Password'
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@example.com'
    }))
