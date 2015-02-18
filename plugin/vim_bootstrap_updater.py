import os
import urllib
import urllib2


def vimrc_path():
    return os.path.expanduser('~/.vimrc')


def _generate_vimrc(langs):
    params = urllib.urlencode([('langs', l.strip()) for l in langs])
    resp = urllib2.urlopen("https://vim-bootstrap.appspot.com/generate.vim",
                           params)
    return resp.read()


def get_available_langs():
    resp = urllib2.urlopen("https://vim-bootstrap.appspot.com/langs")
    return resp.read()


def update(langs):
    content = _generate_vimrc(langs)

    with open(vimrc_path(), 'w') as fh:
        fh.write(str(content))

    return content

