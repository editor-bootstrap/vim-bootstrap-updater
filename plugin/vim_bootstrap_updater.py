import os
import urllib
import urllib2


def vimrc_path(editor):
    return os.path.expanduser('~/.%src' % editor)


def _generate_vimrc(editor, langs):
    params = [('langs', l.strip()) for l in langs]
    params.append(('editor', editor))
    data = urllib.urlencode(params)
    resp = urllib2.urlopen("https://vim-bootstrap.appspot.com/generate.vim",
                           data)
    return resp.read()


def get_available_langs():
    resp = urllib2.urlopen("https://vim-bootstrap.appspot.com/langs")
    return resp.read()


def update(vimrc, editor, langs):
    content = _generate_vimrc(editor, langs)
    vimrc = os.path.expanduser(vimrc)

    with open(vimrc, 'w') as fh:
        fh.write(str(content))

    return content

