import os
try:
    import urllib2
    import urllib
except ImportError:
    import urllib.request as urllib2
    import urllib.parse as urllib


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 '
    'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;'
    'q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def vimrc_path(editor):
    return os.path.expanduser('~/.%src' % editor)


def _generate_vimrc(editor, langs):
    params = [('langs', l.strip()) for l in langs]
    params.append(('editor', editor))
    data = urllib.urlencode(params)
    URL = "https://vim-bootstrap.com/generate.vim"
    req = urllib2.Request(URL, headers=HEADERS)
    resp = urllib2.urlopen(req, data.encode('utf-8'))
    return resp.read()


def get_available_langs():
    URL = "https://vim-bootstrap.com/langs"
    req = urllib2.Request(URL, headers=HEADERS)
    resp = urllib2.urlopen(req)
    return resp.read().decode('utf-8')


def update(vimrc, editor, langs):
    content = _generate_vimrc(editor, langs).decode('utf-8')
    vimrc = os.path.expanduser(vimrc)

    with open(vimrc, 'w') as fh:
        fh.write(content)

    return content
