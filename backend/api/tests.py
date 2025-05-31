from django.test import TestCase
from django.contrib.auth.models import User

class TokenTests(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser1234',
            password='testpassword1234',
        )

    def test_token_obtain(self):
        # Obtain tokens
        response = self.client.post('/api/token/', {
            'username': self.user.username,
            'password': 'testpassword1234',
        })

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the token is present in the response
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


    def test_token_obtain_verify(self):
        # Obtain tokens
        response = self.client.post('/api/token/', {
            'username': self.user.username,
            'password': 'testpassword1234',
        })

        # Verify the token
        response = self.client.post('/api/token/verify/', {
            'token': response.data.get('access'),
        })

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)


    def test_token_obtain_refresh(self):
        # Obtain tokens
        response = self.client.post('/api/token/', {
            'username': self.user.username,
            'password': 'testpassword1234',
        })

        # Refresh the token
        response = self.client.post('/api/token/refresh/', {
            'refresh': response.data.get('refresh'),
        })

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)

        # Check if the new access token is present in the response
        self.assertIn('access', response.data)

    def test_token_obtain_refresh_verify(self):
        # Obtain tokens
        response = self.client.post('/api/token/', {
            'username': self.user.username,
            'password': 'testpassword1234',
        })

        # Refresh the token
        response = self.client.post('/api/token/refresh/', {
            'refresh': response.data.get('refresh'),
        })

        # Verify the token
        response = self.client.post('/api/token/verify/', {
            'token': response.data.get('access'),
        })

        # Check if the response is successful
        self.assertEqual(response.status_code, 200)




