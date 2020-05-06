from django.urls import reverse

from rest_framework.test import APITestCase


class GetAttributesTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("get-attributes")

    def test_if_endpoint_returns_bad_code_response_when_image_path_is_not_correct(self):
        image_path = "/abc/def.pdf"
        url = f"{self.url}?image_path={image_path}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)

    def test_if_endpoint_returns_correct_response_when_image_path_works(self):
        image_path = "/abc/def.jpeg"
        url = f"{self.url}?image_path={image_path}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)