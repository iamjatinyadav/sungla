from django import forms

"""
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

"""


class ContactForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'contactus'}))
    phone = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    message = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.isalpha():
            raise forms.ValidationError("name only in alphabetic")
        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.isdigit():
            raise forms.ValidationError("phone number is only numeric")

        if len(phone) > 10:
            raise forms.ValidationError(f"phone number maximum have 10 number. you use {len(phone)} numbers.")
        return phone

    def clean_message(self):
        message = self.cleaned_data["message"]

        if len(message) < 5:
            raise forms.ValidationError("minimum use 5 characters")
        return message

