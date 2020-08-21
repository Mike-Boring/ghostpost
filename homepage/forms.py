from django import forms
from homepage.models import BoastsRoasts


POST_CHOICES = [
    ('boast', 'Boast'),
    ('roast', 'Roast'),
]


class AddPostForm(forms.Form):
    boasts = forms.CharField(
        label='Post type: ', widget=forms.Select(choices=POST_CHOICES))
    post_text = forms.CharField(max_length=240)
