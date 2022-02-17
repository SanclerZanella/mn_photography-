from django import forms
from .models import Album, Category


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'date': forms.DateInput()
        }

    photos = forms.ImageField(label='Photos', required=False, widget=forms.FileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
