from django.db import models


class CleaningRecord(models.Model):
    raw_text = models.TextField()
    cleaned_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        preview = self.raw_text[:40].replace("\n", " ")
        return f"{self.created_at:%Y-%m-%d %H:%M} — {preview}"
