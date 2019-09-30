from django import forms


class AdventureForm(forms.Form):
    title = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Give your adventure a name"
        })
    )
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Give a brief description of the adventures content"
        })
    )
