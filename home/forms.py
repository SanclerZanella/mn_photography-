from django import forms
from .models import Home_page_content


class IndexForm(forms.ModelForm):
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
        model = Home_page_content
        fields = '__all__'

    # first_testimonial_pic = forms.ImageField(required=False)
    # first_testimonial_text = forms.CharField(widget=forms.Textarea, max_length=300, required=True)
    # first_testimonial_partner1 = forms.CharField(required=True)
    # first_testimonial_partner2 = forms.CharField(required=True)

    # second_testimonial_pic = forms.ImageField(required=False)
    # second_testimonial_text = forms.CharField(widget=forms.Textarea, max_length=300, required=True)
    # second_testimonial_partner1 = forms.CharField(required=True)
    # second_testimonial_partner2 = forms.CharField(required=True)

    # third_testimonial_pic = forms.ImageField(required=False)
    # third_testimonial_text = forms.CharField(widget=forms.Textarea, max_length=300, required=True)
    # third_testimonial_partner1 = forms.CharField(required=True)
    # third_testimonial_partner2 = forms.CharField(required=True)

    # def __init__(self, *args, **kwargs):
    #     """
    #     Change fields label
    #     """

    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'carousell_photo_1': 'Primeira foto do slide',
    #         'carousell_photo_2': 'Segunda foto do slide',
    #         'carousell_photo_3': 'Terceira foto do slide',
    #         'middle_text': 'Texto do meio da página',
    #         'middle_picture': 'Foto do fotógrafo',
    #         'prew_picture': 'Foto para o link da coleção de pre-weddings',
    #         'w_picture': 'Foto para o link da coleção de casamentos',
    #         'fam_picture': 'Foto para o link da coleção de fotos de família',
    #         'first_testimonial_pic': 'Foto do primeiro testemunho',
    #         'first_testimonial_text': 'Texto do primeiro testemunho',
    #         'first_testimonial_partner1': 'Primeiro nome do primeiro testemunho',
    #         'first_testimonial_partner2': 'Segundo nome do primeiro testemunho',
    #         'second_testimonial_pic': 'Foto do segundo testemunho',
    #         'second_testimonial_text': 'Texto do segundo testemunho',
    #         'second_testimonial_partner1': 'Primeiro nome do segundo testemunho',
    #         'second_testimonial_partner2': 'Segundo nome do segundo testemunho',
    #         'third_testimonial_pic': 'Foto do terceiro testemunho',
    #         'third_testimonial_text': 'Texto do terceiro testemunho',
    #         'third_testimonial_partner1': 'Primeiro nome do terceiro testemunho',
    #         'third_testimonial_partner2': 'Segundo nome do terceiro testemunho',
    #     }

    #     label_fields = ['middle_text', 'first_testimonial_text', 'first_testimonial_partner1',
    #                     'first_testimonial_partner2', 'second_testimonial_text', 'second_testimonial_partner1',
    #                     'second_testimonial_partner2', 'third_testimonial_text', 'third_testimonial_partner1',
    #                     'third_testimonial_partner2']

    #     for field in self.fields:
    #         placeholder = placeholders[field]
    #         self.fields[field].widget.attrs['placeholder'] = placeholder

    #         if field in label_fields: 
    #             self.fields[field].label = placeholder
    #         else:
    #             self.fields[field].label = False
