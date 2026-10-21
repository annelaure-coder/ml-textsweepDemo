from django import forms


class CleanTextForm(forms.Form):
    text = forms.CharField(
        label="Text to clean",
        required=True,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "id": "id_text",
                "rows": 8,
                "placeholder": "Paste messy text here…",
            }
        ),
        error_messages={"required": "Please enter some text to clean."},
    )
