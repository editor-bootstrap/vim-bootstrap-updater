" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! VimBootstrapUpdate()
python << endOfPython

from vim_bootstrap_updater import update, get_available_langs

try:
	# read the vim_bootstrap_langs and generate the list
	# if this variable doens't exist it will generate a 
	# list with all available languages
	langs = vim.eval('g:vim_bootstrap_langs').split(',')
except:
	langs = get_available_langs().split(',')

try:
	update(langs)
	print '~/.vimrc succesfully updated'
except Exception as e:
	print 'error to generate .vimrc'
	print e

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
