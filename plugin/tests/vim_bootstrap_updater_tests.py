import unittest
import mock
import urllib2
import vim_bootstrap_updater as sut


class VimBootstrapUpdaterTests(unittest.TestCase):

    @mock.patch('vim_bootstrap_updater.urllib2.urlopen')
    @mock.patch('vim_bootstrap_updater.vimrc_path', return_value='/tmp/.vimrc')
    def test_generate_vimrc_200(self, mock_VIMRC_PATH, mock_urlopen):
        mock_response = mock.MagicMock()
        mock_response.code = 200
        mock_response.read.return_value = 'fake response'
        mock_urlopen.return_value = mock_response

        result = sut._generate_vimrc('nvim', ['hy', 'closure'])

        self.assertEqual(mock_urlopen.call_args, mock.call(
            'https://vim-bootstrap.appspot.com/generate.vim',
            'langs=hy&langs=closure&editor=nvim'))
        self.assertEqual('fake response', result)

    @mock.patch('vim_bootstrap_updater.urllib2.urlopen')
    @mock.patch('vim_bootstrap_updater.vimrc_path', return_value='/tmp/.vimrc')
    def test_generate_vimrc_NOT_200(self, mock_VIMRC_PATH, mock_urlopen):
        mock_urlopen.side_effect = urllib2.HTTPError(
            url="https://vim-bootstrap.appspot.com/generate.vim",
            code=404, msg="Not Found", hdrs=None, fp=None)

        with self.assertRaises(urllib2.HTTPError):
            sut._generate_vimrc('vim', ['hy'])

    @mock.patch('vim_bootstrap_updater._generate_vimrc', return_value='fake vimrc')
    def test_update(self, mock_generate_vimrc):
        result = sut.update('/tmp/.vimrc', 'vim', ['hy'])

        self.assertEqual('fake vimrc', result)

        with open('/tmp/.vimrc', 'r') as fh:
            content = fh.read()
            self.assertEqual('fake vimrc', content)
