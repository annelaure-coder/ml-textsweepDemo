from textsweep import clean_text as textsweep_clean

from .models import CleaningRecord


def count_words(text: str) -> int:
    return len(text.split()) if text and text.strip() else 0


def build_stats(original: str, cleaned: str) -> dict:
    return {
        "char_count_before": len(original),
        "char_count_after": len(cleaned),
        "word_count_before": count_words(original),
        "word_count_after": count_words(cleaned),
    }


def process_text(text: str) -> dict:
    """Clean text with textsweep, persist history, and return original/cleaned/stats."""
    original = text
    cleaned = textsweep_clean(original)
    CleaningRecord.objects.create(raw_text=original, cleaned_text=cleaned)
    return {
        "original": original,
        "cleaned": cleaned,
        "stats": build_stats(original, cleaned),
    }
