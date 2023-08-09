from django.contrib import admin
from .models import Advertisement


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


admin.site.register(Advertisement, AdvertisementAdmin)