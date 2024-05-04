from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.tests.factories import CustomUserFactory


class CustomUserUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUserFactory(
            with_first_name=True,
            with_last_name=True,
            with_speciality=True,
            with_skills=True,
            with_description=True,
            with_country=True,
            with_city=True,
            with_phone=True,
        )

    def given_user_logged_in(self):
        url = reverse("account_login")
        self.client.post(
            url,
            {"login": self.user.email, "password": CustomUserFactory.password},
            follow=True,
        )

    def test_profile_update_view_302_for_anonymous(self):
        url = reverse("users:update", kwargs={"pk": self.user.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_update_view_opens_with_login(self):
        self.given_user_logged_in()

        url = reverse("users:update", kwargs={"pk": self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
