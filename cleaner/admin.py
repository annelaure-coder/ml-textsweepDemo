from django.contrib import admin

from .models import CleaningRecord


@admin.register(CleaningRecord)
class CleaningRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "short_raw", "short_cleaned")
    list_filter = ("created_at",)
    search_fields = ("raw_text", "cleaned_text")
    readonly_fields = ("raw_text", "cleaned_text", "created_at")
    ordering = ("-created_at",)

    @admin.display(description="Raw")
    def short_raw(self, obj):
        return obj.raw_text[:80]

    @admin.display(description="Cleaned")
    def short_cleaned(self, obj):
        return obj.cleaned_text[:80]
