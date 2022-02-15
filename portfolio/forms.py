from django import forms
from .models import Album, AlbumPhoto


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = '__all__'

    photos = forms.ImageField(label='Photos', required=False, widget=forms.FileInput(attrs={'multiple': True}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     categories = Category.objects.all()
    #     friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

    #     self.fields['category'].choices = friendly_names
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'border-black rounded-0'