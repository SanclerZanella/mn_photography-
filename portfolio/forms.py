from django import forms
from .models import Album, Category


class AlbumForm(forms.ModelForm):
    '''
    New album form
    '''

    class Meta:
        '''
        Change date format
        '''
        model = Album
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    photos = forms.ImageField(label='Photos', required=False, widget=forms.FileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        placeholders = {
            'category': 'Categoria*',
            'title': 'Título',
            'pre_desc': 'Pré descrição',
            'date': 'Data do evento',
            'place': 'Lugar do Evento',
            'cover': 'Foto de capa*',
            'description': 'Descrição do evento',
            'photos': 'Fotos*',
        }

        label_fields = ['category', 'title', 'pre_desc', 'date', 'place', 'cover', 'description', 'photos']

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['required'] = 'required'

            if field in label_fields:
                self.fields[field].label = placeholder
            else:
                self.fields[field].label = False
