from django import forms


class RatingForm(forms.Form):
    score = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        coerce=int,
        widget=forms.RadioSelect,
    )
    body = forms.CharField(
        label="Review (optional)",
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
    )