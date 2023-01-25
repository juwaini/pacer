from django.contrib import admin

from score.models import Score


class ScoreAdmin(admin.ModelAdmin):
    model = Score
    list_display = 'user_id', 'score',  'last_check'


admin.site.register(Score, ScoreAdmin)
