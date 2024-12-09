from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={})
    )

    class Meta:
        model = ArticleImage
        fields = '__all__'  # Ensure this is a list or string '__all__' without quotes
