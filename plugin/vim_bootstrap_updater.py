import os
import vim

from httplib2 import Http
from urllib import urlencode


def update():
    langs = vim.eval('g:vim_bootstrap_langs').split(',')

    data = []
    for lang in langs:
        data.append('langs={}'.format(lang.strip()))

    data = '&'.join(data)

    response, content = Http().request(
        'http://vim-bootstrap.appspot.com/generate.vim',
        'POST',
        data
    )

    with open(os.path.expanduser('~/.vimrc'), 'w') as fh:
        fh.write(str(content))

    return data, content
