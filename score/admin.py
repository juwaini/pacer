from django.contrib import admin

from score.models import Score


class ScoreAdmin(admin.ModelAdmin):
    model = Score
    # list_display = '__all__'


admin.site.register(Score, ScoreAdmin)
