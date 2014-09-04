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

from vim_bootstrap_updater import update

langs = vim.eval('g:vim_bootstrap_langs').split(',')
response, content = update(langs)

print response

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
