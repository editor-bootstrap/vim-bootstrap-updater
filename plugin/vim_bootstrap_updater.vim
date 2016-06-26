" --------------------------------
" Add our plugin to the path
" --------------------------------
if has('python3')
	let g:pyt='python3'
else
	let g:pyt='python'
endif

exec g:pyt . " import sys"
exec g:pyt . " import os"
exec g:pyt . " import vim"
exec g:pyt . " sys.path.append(vim.eval('expand(\"<sfile>:h\")'))"


" --------------------------------
"  Function(s)
"  TODO: Need to unify the code and take the if of execution
" --------------------------------
function! VimBootstrapUpdate()
if has('python3')
python3 << endOfPython

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
	print('{} succesfully updated'.format(vimrc))
except Exception as e:
	print('error to generate {}'.format(vimrc))
	print(e)

endOfPython
else
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
	print '{0} succesfully updated'.format(vimrc)
except Exception as e:
	print 'error to generate {0}'.format(vimrc)
	print e

endOfPython
endif
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
