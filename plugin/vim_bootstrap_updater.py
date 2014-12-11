import os

from httplib import HTTPConnection


def vimrc_path():
    return os.path.expanduser('~/.vimrc')


def _generate_params(langs):
    params = '&'.join(['langs={}'.format(lang.strip()) for lang in langs])
    return params


def _generate_vimrc(langs):
    params = _generate_params(langs)

    conn = HTTPConnection('vim-bootstrap.appspot.com')
    conn.request('POST', '/generate.vim', params, {})

    response = conn.getresponse()

    if response.status is not 200:
        raise Exception()

    return response.read()


def get_available_langs():
    conn = HTTPConnection('vim-bootstrap.appspot.com')
    conn.request('GET', '/langs')

    response = conn.getresponse()

    if response.status is not 200:
        raise Exception()

    return response.read()
        

def update(langs):
    content = _generate_vimrc(langs)

    with open(vimrc_path(), 'w') as fh:
        fh.write(str(content))

    return content

