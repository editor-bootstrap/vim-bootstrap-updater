" --------------------------------
"  Function(s)
" --------------------------------
function! VimBootstrapUpdate()
   let langs = join(split(g:vim_bootstrap_langs, ','), '&langs=')
   let frams = join(split(g:vim_bootstrap_frams, ','), '&frameworks=')
   let editor = g:vim_bootstrap_editor
   let theme = g:vim_bootstrap_theme
   let path = $MYVIMRC
   let data = 'langs='.langs.'&editor='.editor.'&theme='.theme.'&frameworks='.frams
   silent exec '!curl -fLso '.path.' https://vim-bootstrap.com/generate.vim --data "'.data.'"' | redr!
   echo path.' sucesfully updated! '
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! VimBootstrapUpdate call VimBootstrapUpdate()
