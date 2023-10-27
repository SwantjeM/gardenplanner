from django import forms


class DateFilterForm(forms.Form):
    date = forms.DateField(
        label="Select a Date",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
