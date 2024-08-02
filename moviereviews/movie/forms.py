from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'}
        )

    class Meta:
        model = Review
        fields = ['title', 'watchAgain']
