import unittest
from mock import patch, PropertyMock, MagicMock
import vim_bootstrap_updater as sut


class VimBootstrapUpdaterTests(unittest.TestCase):

    def test_generate_params(self):
        langs = 'hy clojure'.split()
        result = sut._generate_params(langs)

        self.assertEqual('langs=hy&langs=clojure', result)

    @patch('vim_bootstrap_updater.HTTPConnection')
    @patch('vim_bootstrap_updater.vimrc_path', return_value='/tmp/.vimrc')
    @patch('vim_bootstrap_updater._generate_params', return_value='langs=hy')
    def test_generate_vimrc_200(self, mock_generate_params, mock_VIMRC_PATH, mock_HTTPConnection):
        mock_conn = MagicMock()
        mock_HTTPConnection.return_value = mock_conn
        mock_response = MagicMock()
        type(mock_response).status = PropertyMock(return_value=200)
        mock_response.read.return_value = 'fake response'

        mock_conn.getresponse.return_value = mock_response

        result = sut._generate_vimrc(['hy'])

        self.assertEqual('fake response', result)

    @patch('vim_bootstrap_updater.HTTPConnection')
    @patch('vim_bootstrap_updater.vimrc_path', return_value='/tmp/.vimrc')
    @patch('vim_bootstrap_updater._generate_params', return_value='langs=hy')
    def test_generate_vimrc_NOT_200(self, mock_generate_params, mock_VIMRC_PATH, mock_HTTPConnection):
        mock_conn = MagicMock()
        mock_HTTPConnection.return_value = mock_conn
        mock_response = MagicMock()
        type(mock_response).status = PropertyMock(return_value=404)
        mock_response.read.return_value = 'fake response'

        mock_conn.getresponse.return_value = mock_response

        with self.assertRaises(Exception):
            sut._generate_vimrc(['hy'])

    @patch('vim_bootstrap_updater.vimrc_path', return_value='/tmp/.vimrc')
    @patch('vim_bootstrap_updater._generate_vimrc', return_value='fake vimrc')
    def test_update(self, mock_generate_vimrc, mock_vimrc_path):
        result = sut.update(['hy'])

        self.assertEqual('fake vimrc', result)

        with open('/tmp/.vimrc', 'r') as fh:
            content = fh.read()
            self.assertEqual('fake vimrc', content)
