from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='Recipient email', help_text="Can't ends with 'test.com'")
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email.endswith("@test.com"):
            raise forms.ValidationError("Email can't ends with 'test.com'")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        subject = cleaned_data['subject']
        if email == subject:
            raise forms.ValidationError("Email can't be same as subject")