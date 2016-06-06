" --------------------------------
" Add our plugin to the path
" --------------------------------
if has('python3')
	python3 import sys
	python3 import os
	python3 import vim
	python3 sys.path.append(vim.eval('expand("<sfile>:h")'))
else
	python import sys
	python import os
	python import vim
	python sys.path.append(vim.eval('expand("<sfile>:h")'))
endif

" --------------------------------
"  Function(s)
" --------------------------------
function! VimBootstrapUpdate()
python << endOfPython

from vim_bootstrap_updater import update, get_available_langs

def vim_eval(var, default=None):
	try:
		return vim.eval(var)
	except:
		return default

langs = vim_eval('g:vim_bootstrap_langs', get_available_langs()).split(',')
runtime = os.path.basename(os.environ.get('VIM', 'vim'))
editor = vim_eval('g:vim_bootstrap_editor', runtime)
vimrc = os.environ.get('MYVIMRC', '~/.%src' % editor)

try:
	update(vimrc, editor, langs)
	print '%s succesfully updated' % vimrc
except Exception as e:
	print 'error to generate %s' % vimrc
	print e

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
