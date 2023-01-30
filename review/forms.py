from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Form for leaving rating and review """
    error_css_class = 'erorr-field'
    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = forms.ChoiceField(
        choices=RATING,
        widget=forms.RadioSelect(
            attrs={'class': 'form-check-inline ', 'style': 'list-style:none'},
            )
        )

    class Meta:
        model = Review
        fields = ['rating', 'body']
        labels = {'body': 'Please Write Your Review '}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
