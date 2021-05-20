from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UsersTests(APITestCase):

    def test_users_list(self):
        """
        Ensure we can get user list.
        """
        # arrange
        user_data: str = '1'
        user: User = User.objects.create(
            username=user_data, password=user_data, is_staff=True)

        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        # act
        client: APIClient = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = client.get('/api/users/')

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['username'], user_data)

    def test_retrieve_current_with_token(self):
        """
        Ensure we can get current user.
        """
        # arrange
        user_data: str = '1'
        user: User = User.objects.create(username=user_data, password=user_data)

        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        # act
        client: APIClient = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = client.get(f'/api/users/{user.id}/')

        # assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], user_data)

    def test_retrieve_not_current_with_token(self):
        """
        Ensure we can not get not current user.
        """
        # arrange
        user1_data: str = '1'
        user1: User = User.objects.create(username=user1_data, password=user1_data)

        refresh_token = RefreshToken.for_user(user1)
        access_token = refresh_token.access_token

        user2_data: str = '2'
        user2: User = User.objects.create(username=user2_data, password=user2_data)

        # act
        client: APIClient = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = client.get(f'/api/users/{user2.id}/')

        # assert
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
