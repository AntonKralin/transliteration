from django import forms

class TextForm(forms.Form):
    text = forms.CharField(label="текст", 
                           widget=forms.TextInput(attrs={'placeholder': 'Введите текст на русском'}),
                           required=True,
                           help_text="Русские буквы транслителируются в английские")