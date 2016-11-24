import os
try:
    import urllib2
    import urllib
except ImportError:
    import urllib.request as urllib2
    import urllib.parse as urllib

HEADERS = {
    'User-Agent': 'Mozilla/5.0',
}


def _generate_vimrc(editor, langs):
    '''Generate a config file.

    Generate a config file based on your editor and choosen languages.
    '''
    params = [('langs', l.strip()) for l in langs]
    params.append(('editor', editor))
    data = urllib.urlencode(params)
    URL = "https://vim-bootstrap.com/generate.vim"
    req = urllib2.Request(URL, headers=HEADERS)
    resp = urllib2.urlopen(req, data.encode('utf-8'))
    return resp.read().decode('utf-8')


def get_available_langs():
    '''Get vim-bootstrap available languages'''
    URL = "https://vim-bootstrap.com/langs"
    req = urllib2.Request(URL, headers=HEADERS)
    resp = urllib2.urlopen(req)
    return resp.read().decode('utf-8')


def update(vimrc, editor, langs):
    '''Overwrite vim/nvim config file with new configs.

    Overwrite vim/nvimrc config file based on your choosen languages.
    '''
    content = _generate_vimrc(editor, langs)
    vimrc = os.path.expanduser(vimrc)

    with open(vimrc, 'wb') as fh:
        fh.write(content.encode('utf-8'))

    return content
