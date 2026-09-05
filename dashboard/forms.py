from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password


class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        )
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:

                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user


# ============================================================
# ADMIN WORKER REGISTRATION FORM
# ============================================================

class WorkerRegistrationForm(forms.Form):

    # -------------------------
    # Login Account Information
    # -------------------------

    username = forms.CharField(
        max_length=150,
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter worker username",
            }
        ),
    )

    email = forms.EmailField(
        required=False,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter worker email",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter password",
            }
        ),
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm password",
            }
        ),
    )

    # -------------------------
    # Worker Information
    # -------------------------

    worker_id = forms.CharField(
        max_length=50,
        label="Worker ID",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Example: JH-W-001",
            }
        ),
    )

    full_name = forms.CharField(
        max_length=150,
        label="Full Name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter worker full name",
            }
        ),
    )

    phone = forms.CharField(
        max_length=20,
        required=False,
        label="Phone Number",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter phone number",
            }
        ),
    )

    organization = forms.CharField(
        max_length=150,
        required=False,
        label="Organization",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Mine / Company / Organization",
            }
        ),
    )

    sector = forms.CharField(
        max_length=100,
        required=False,
        label="Sector",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Example: Mining",
            }
        ),
    )

    language = forms.ChoiceField(
        label="Preferred Language",
        choices=[
            ("en", "English"),
            ("hi", "Hindi"),
            ("sat", "Santali"),
        ],
        initial="en",
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    # -------------------------
    # Validation
    # -------------------------

    def clean_username(self):

        username = self.cleaned_data["username"].strip()

        if User.objects.filter(
            username__iexact=username
        ).exists():

            raise forms.ValidationError(
                "This username is already registered."
            )

        return username

    def clean_worker_id(self):

        from .models import Worker

        worker_id = self.cleaned_data["worker_id"].strip()

        if Worker.objects.filter(
            worker_id__iexact=worker_id
        ).exists():

            raise forms.ValidationError(
                "This Worker ID is already registered."
            )

        return worker_id

    def clean_password(self):

        password = self.cleaned_data.get("password")

        if password:

            validate_password(password)

        return password

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get(
            "confirm_password"
        )

        if password and confirm_password:

            if password != confirm_password:

                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data