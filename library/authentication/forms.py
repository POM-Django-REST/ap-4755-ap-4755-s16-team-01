from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )


class RegisterForm(forms.Form):

    email = forms.EmailField()

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    first_name = forms.CharField(
        required=False
    )

    last_name = forms.CharField(
        required=False
    )

    role = forms.ChoiceField(
        choices=[
            (0, "Звичайний користувач"),
            (1, "Бібліотекар"),
        ]
    )
