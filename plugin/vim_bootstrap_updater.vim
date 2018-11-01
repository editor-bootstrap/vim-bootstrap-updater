" --------------------------------
"  Function(s)
" --------------------------------
function! VimBootstrapUpdate()
   let langs = join(split(g:vim_bootstrap_langs, ','), '&langs=')
   let editor = g:vim_bootstrap_editor
   let path = $MYVIMRC
   let data = 'langs='.langs.'&editor='.editor
   silent exec '!curl -fLso '.path.' http://vim-bootstrap.com/generate.vim --data "'.data.'"' | redr!
   echo path.' sucesfully updated! '
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
