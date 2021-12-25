from django import forms

from polls.models import Person         # noqa: F401


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


class TriangleForm(forms.Form):
    a = forms.FloatField(label='Cathetus a',  # min_value=0.01,
                         widget=forms.TextInput(attrs={'placeholder': 'Number > 0'}))
    b = forms.FloatField(label='Cathetus b',  # min_value=0.01,
                         widget=forms.TextInput(attrs={'placeholder': 'Number > 0'}))

    def clean_a(self):
        a = self.cleaned_data.get('a')
        if a <= 0:
            raise forms.ValidationError("Cathetus a can't be less then 0")
        return a

    def clean_b(self):
        b = self.cleaned_data.get('b')
        if b <= 0:
            raise forms.ValidationError("Cathetus b can't be less then 0")
        return b

    # def clean(self):
    #     cleaned_data = super().clean()
    #     a = cleaned_data.get('a')
    #     b = cleaned_data['b']
    #     if a <= 0 or b <= 0:
    #         raise forms.ValidationError("Cathetus can't be less then 0")
    #
    #   ^
    #   |
    #    \
    #      ----  Всё поправил


# class PersonForm(forms.ModelForm):  # Специально для instance
#     class Meta:
#         model = Person
#         fields = ['first_name', 'last_name', 'email']
