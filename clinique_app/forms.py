from django import forms


class UpForm(forms.Form):
    """
    Класс формы на главной странице сайта
    """
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'ФИО*', 'type': 'text'})
                           )
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                   attrs={'placeholder': 'Телефон*', 'type': 'text'})
                               )
    email = forms.EmailField(label='', max_length=128,
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'E-mail', 'type': 'email'})
                             )

    date = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Дата', 'data-provide': 'datepicker'}
                           ))
    service = forms.CharField(label='', max_length=128,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Услуга'}
                              ))


class PricesForm(forms.Form):
    """
    Класс формы на главной странице сайта
    """
    name = forms.CharField(label='', max_length=128,
                           widget=forms.TextInput(
                               attrs={'placeholder': 'ФИО*', 'type': 'text'})
                           )
    phone = forms.IntegerField(label='',
                               widget=forms.NumberInput(
                                   attrs={'placeholder': 'Телефон*', 'type': 'text'})
                               )
    email = forms.EmailField(label='', max_length=128,
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'E-mail', 'type': 'email'})
                             )
