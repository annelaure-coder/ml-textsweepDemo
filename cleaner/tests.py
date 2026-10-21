from django.test import TestCase
from django.urls import reverse

from textsweep import clean_text

from .models import CleaningRecord
from .services import build_stats, count_words, process_text


class ServiceTests(TestCase):
    def test_clean_text_example(self):
        sample = "Check out https://example.com!!! 🎉 It's <b>GREAT</b>."
        self.assertEqual(clean_text(sample), "check out its great")

    def test_count_words_and_stats(self):
        original = "Hello  world!!"
        cleaned = "hello world"
        self.assertEqual(count_words(original), 2)
        self.assertEqual(
            build_stats(original, cleaned),
            {
                "char_count_before": len(original),
                "char_count_after": len(cleaned),
                "word_count_before": 2,
                "word_count_after": 2,
            },
        )

    def test_process_text_saves_history(self):
        result = process_text("HTML <b>OK</b> https://x.test")
        self.assertEqual(result["original"], "HTML <b>OK</b> https://x.test")
        self.assertEqual(result["cleaned"], "html ok")
        self.assertEqual(CleaningRecord.objects.count(), 1)
        record = CleaningRecord.objects.get()
        self.assertEqual(record.raw_text, result["original"])
        self.assertEqual(record.cleaned_text, result["cleaned"])
        self.assertIn("char_count_before", result["stats"])


class FormViewTests(TestCase):
    def test_home_get(self):
        response = self.client.get(reverse("cleaner:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clean")
        self.assertContains(response, 'id="id_text"')

    def test_home_post_cleans_and_saves(self):
        response = self.client.post(
            reverse("cleaner:home"),
            {"text": "Check out https://example.com!!! 🎉 It's <b>GREAT</b>."},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "check out its great")
        self.assertEqual(CleaningRecord.objects.count(), 1)

    def test_home_post_empty_does_not_save(self):
        response = self.client.post(reverse("cleaner:home"), {"text": "   "})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CleaningRecord.objects.count(), 0)

    def test_history_lists_newest_first(self):
        first = CleaningRecord.objects.create(raw_text="one", cleaned_text="one")
        second = CleaningRecord.objects.create(raw_text="two", cleaned_text="two")
        response = self.client.get(reverse("cleaner:history"))
        self.assertEqual(response.status_code, 200)
        records = list(response.context["records"])
        self.assertEqual(records[0].pk, second.pk)
        self.assertEqual(records[1].pk, first.pk)


class ApiTests(TestCase):
    def test_api_clean_success(self):
        response = self.client.post(
            reverse("cleaner:api_clean"),
            data='{"text": "Visit https://example.com NOW!!!"}',
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["original"], "Visit https://example.com NOW!!!")
        self.assertEqual(body["cleaned"], "visit now")
        self.assertEqual(body["stats"]["word_count_before"], 3)
        self.assertEqual(CleaningRecord.objects.count(), 1)

    def test_api_missing_text_returns_400(self):
        response = self.client.post(
            reverse("cleaner:api_clean"),
            data="{}",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("text", response.json()["error"].lower())
        self.assertEqual(CleaningRecord.objects.count(), 0)

    def test_api_empty_text_returns_400(self):
        response = self.client.post(
            reverse("cleaner:api_clean"),
            data='{"text": "   "}',
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(CleaningRecord.objects.count(), 0)

    def test_api_invalid_json_returns_400(self):
        response = self.client.post(
            reverse("cleaner:api_clean"),
            data="not-json",
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 400)
