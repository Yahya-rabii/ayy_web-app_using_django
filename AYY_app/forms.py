from django import forms
from AYY_app.models import User


# Create your forms here.

class NewUserForm(forms.Form):

    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=255)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with that email already exists")
        return email

    def save(self):

        User.objects.create(firstname=self.cleaned_data['firstname'],
                            lastname=self.cleaned_data['lastname'],
                            email=self.cleaned_data['email'],
                            password=self.cleaned_data['password'])

        print(self.cleaned_data)

    class Meta:
        model = User
        fields = ("firstname", "lastname", "email", "password")
