from django import forms
from django.core.exceptions import ValidationError

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    # Custom validation to ensure passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:

            self.add_error('password', 'Passwords do not match.')
            self.add_error('confirm_password', 'Passwords do not match.')
            # Clear only the password fields
            self.data = self.data.copy()
            self.data['password'] = ''
            self.data['confirm_password'] = ''
        return cleaned_data
        
    
class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
