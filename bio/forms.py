from django import forms
from .models import BioPageContent


class BioForm(forms.ModelForm):
    """
    ProductForm
    Attributes:
        *image: Represents an add image input
    Sub-classes:
        *Meta: Represent related model and form fields
               caught from related model.
    Methods:
        *__init__: Add categories friendly name to categories list.
    """

    class Meta:
        """
        Meta
        Attributes:
            *Model: Model related to the form ;
            *fields: Representation of the fields in the form
                     caught from related model.
        """
        model = BioPageContent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Change fields label
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Título da página',
            'cover_picture': 'Foto de capa',
            'first_text': 'Primeiro texto',
            'second_photo': 'Segunda foto',
            'second_text': 'Segundo texto',
        }

        label_fields = ['title', 'cover_picture', 'first_text',
                        'second_photo', 'second_text']

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder

            if field in label_fields:
                self.fields[field].label = placeholder
            else:
                self.fields[field].label = False
