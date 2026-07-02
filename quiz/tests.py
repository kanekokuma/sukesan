from django.test import SimpleTestCase
from django.urls import reverse


class QuizPageTests(SimpleTestCase):
    def test_index_page(self):
        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "スケさんクイズ！")
        self.assertContains(response, "すたーと")

    def test_quiz_page(self):
        response = self.client.get(reverse("quiz"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "スケさんは39歳である！")
        self.assertContains(response, reverse("correct"))
        self.assertContains(response, reverse("wrong"))

    def test_result_pages_return_to_index_after_three_seconds(self):
        for name, message in (("correct", "正解！"), ("wrong", "不正解！")):
            with self.subTest(name=name):
                response = self.client.get(reverse(name))

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, message)
                self.assertContains(response, '<meta http-equiv="refresh" content="3; url=/">')
