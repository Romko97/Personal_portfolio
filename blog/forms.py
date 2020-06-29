from django import forms

class CommentForm(forms.Form):
    author = forms.CharFields(
        max_length=60
        widget = forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Your Name"
        })
    )
    body=forms.CharField(
        widget=forms.Textarea(attrs={
            "class":"form-control",
            "placeholder":"Roman says 'Leave a comment!'"
        })
    )