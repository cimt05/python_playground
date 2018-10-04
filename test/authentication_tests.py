from unittest import TestCase
from mock import patch
import project1.authentication as auth

class StandAloneTests(TestCase):

    @patch('__builtin__.open')
    def test_login_success(self, mock_open):
        mock_open.return_value.read.return_value = 'george|bosco\n'
        self.assertTrue(auth.login('george', 'bosco'))

    @patch('__builtin__.open')
    def test_login_bad_creds(self, mock_open):
        mock_open.return_value.read.return_value = 'george|bosco\n'
        self.assertFalse(auth.login('george', 'marbleRye'))

    @patch('__builtin__.open')
    def test_login_error(self, mock_open):
        mock_open.side_effect = IOError()
        self.assertFalse(auth.login('george', 'bosco'))

    def test_logout(self):
        """Test the logout functio...badly."""
        self.assertEqual(0, 1)
