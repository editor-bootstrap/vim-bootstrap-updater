" --------------------------------
"  Function(s)
" --------------------------------
function! VimBootstrapUpdate()
   let langs = join(split(g:vim_bootstrap_langs, ","), "\&langs=")
   let editor = g:vim_bootstrap_editor
   let path = $MYVIMRC
   let data = 'langs='.langs.'\&editor='.editor
   execute '!\curl -fLo '.path.' http://vim-bootstrap.com/generate.vim --data '.data
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
