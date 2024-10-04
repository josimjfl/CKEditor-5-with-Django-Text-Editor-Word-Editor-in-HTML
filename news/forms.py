
from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Article  # Ensure that the model is properly referenced here
        fields = ("title", "text")
        widgets = {
            'text': CKEditor5Widget(config_name='custom'),  # Using the 'default' config
        }
