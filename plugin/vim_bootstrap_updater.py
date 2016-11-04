import os
try:
    import urllib2
    import urllib
except ImportError:
    import urllib.request as urllib2
    import urllib.parse as urllib


def vimrc_path(editor):
    return os.path.expanduser('~/.%src' % editor)


def _generate_vimrc(editor, langs):
    params = [('langs', l.strip()) for l in langs]
    params.append(('editor', editor))
    data = urllib.urlencode(params)
    resp = urllib2.urlopen("https://vim-bootstrap.com/generate.vim",
                           data.encode('utf-8'))
    return resp.read()


def get_available_langs():
    resp = urllib2.urlopen("https://vim-bootstrap.com/langs")
    return resp.read().decode('utf-8')


def update(vimrc, editor, langs):
    content = _generate_vimrc(editor, langs).decode('utf-8')
    vimrc = os.path.expanduser(vimrc)

    with open(vimrc, 'w') as fh:
        fh.write(content)

    return content
