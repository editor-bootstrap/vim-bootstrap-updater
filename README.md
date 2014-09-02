# vim-bootstrap-updater

## Status

This is a proof of concept!

## Installation

- `vim-boostsrap` is a prereq. Go [here](http://vim-bootstrap.appspot.com/) first.
- `vim-bootstrap` uses NeoBundle so:
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/sherzberg/vim-bootstrap-updater'` to `.vimrc.local`
  - Run `:NeoBundleInstall`

## Usage

Add something like `:let vim_bootstrap_langs = "python,ruby,html,javascript"` in side of your
`.vimrc.local` file.

Next, while in `vim`, just execute `:VimBootstrapUpdate`

## License

See `LICENSE`

## Thanks

This plugin was started using the awesome [vim-plugin-starter-kit](https://github.com/JarrodCTaylor/vim-plugin-starter-kit) written by [JarrodCTaylor](https://github.com/JarrodCTaylor).

