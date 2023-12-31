from django.contrib import admin
from .models import Advertisement
from django.contrib.auth.views import LoginView

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at_with_color')

    list_filter = ['auction', 'created_dt']

    actions = ['make_auction_as_false']

    def updated_at_with_color(self, obj):
        if obj.updated_at.date() == timezone.now().date():
            return "<span style='color: red;'>Сегодня в %s</span>" % obj.updated_at.time().strftime("%H:%M")
        return obj.updated_at

    updated_at_with_color.allow_tags = True
    updated_at_with_color.short_description = 'Последнее обновление'

from django.db import models
from django.conf import settings

class Advertisement(models.Model):
    image = models.ImageField(upload_to='advertisements/')

    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return settings.STATIC_URL + 'img/pic.png'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),


admin.site.register(Advertisement, AdvertisementAdmin)

