# vim-bootstrap-updater

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/sherzberg/vim-bootstrap-updater ~/.vim/bundle/vim-bootstrap-updater`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/sherzberg/vim-bootstrap-updater'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/sherzberg/vim-bootstrap-updater'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/sherzberg/vim-bootstrap-updater'` to .vimrc
  - Run `:PlugInstall`

## Status

This is a proof of concept!

## Usage

`vim-boostsrap` is a prereq. Go [here](http://vim-bootstrap.appspot.com/) first.

Add something like `:let vim_bootstrap_langs = "python,ruby,html,javascript"` in side of your
`.vimrc.local` file.

Next, while in `vim`, just execute `:VimBootstrapUpdate`

## License

See `LICENSE`
