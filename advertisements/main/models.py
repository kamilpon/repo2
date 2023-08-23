rom django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.forms import ModelForm
from django.core.exceptions import ValidationError

User = get_user_model()

class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'

class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),

class AdForm(ModelForm):
    class Meta:
        model = Ad
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            }

        def clean_title(self):
            title = self.cleaned_data.get('title')
            if title.startswith('?'):
                raise ValidationError("Заголовок не может начинаться с вопросительного знака")
            return title
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Отметьте если торг уместен')
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisements/')

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_dt.date() == timezone.now().date():
            created_time = self.created_dt.time().strftime("%H:%M:%S")
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_dt.strftime("%d.%m.%Y в %H:%M:%S ")

    @admin.display(description='дата создания')
    def updated_date(self):
        from django.utils import timezone, html
        if self.updated_dt.date() == timezone.now().date():
            created_time = self.updated_dt.time().strftime("%H:%M:%S")
            return html.format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_dt.strftime("%d.%m.%Y в %H:%M:%S ")

    @admin.display(description='Thumbnail')
    def thumbnail_image(self):
        return html.format_html('<img src="{}" width="50" height="50" />', self.image.url)



