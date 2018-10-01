from unittest import TestCase
from unittest.mock import patch
import project1.authentication as auth

class StandAloneTests(TestCase):

    @patch('builtins.open')
    def test_login_success(self, mock_open):
        mock_open.return_value.read.return_value = 'george|bosco\n'
        self.assertTrue(auth.login('george', 'bosco'))

    @patch('builtins.open')
    def test_login_bad_creds(self, mock_open):
        mock_open.return_value.read.return_value = 'george|bosco\n'
        self.assertFalse(auth.login('george', 'marbleRye'))

    @patch('builtins.open')
    def test_login_error(self, mock_open):
        mock_open.side_effect = IOError()
        self.assertFalse(auth.login('george', 'bosco'))