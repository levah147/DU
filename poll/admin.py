from django.contrib import admin
from .models import Candidate, Position,ControlVote, comment,Profile

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('position',)
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)

admin.site.register(ControlVote)
admin.site.register(comment)
admin.site.register(Profile)
