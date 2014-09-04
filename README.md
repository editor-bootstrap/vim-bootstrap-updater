[![Build Status](https://travis-ci.org/sherzberg/vim-bootstrap-updater.svg?branch=master)](https://travis-ci.org/sherzberg/vim-bootstrap-updater)
[![Coverage Status](https://coveralls.io/repos/sherzberg/vim-bootstrap-updater/badge.png)](https://coveralls.io/r/sherzberg/vim-bootstrap-updater)

# vim-bootstrap-updater

## Status

This is a proof of concept!

## Installation

- `vim-boostsrap` is a prereq. Go [here](http://vim-bootstrap.appspot.com/) first.
- `vim-bootstrap` uses NeoBundle so:
  - Add `NeoBundle 'https://github.com/sherzberg/vim-bootstrap-updater'` to `.vimrc.local`
- Run `:NeoBundleInstall`

## Usage

Add something like `:let vim_bootstrap_langs = "python,ruby,html,javascript"` in side of your
`.vimrc.local` file.

Next, while in `vim`, just execute `:VimBootstrapUpdate`

## License

See [LICENSE](/LICENSE)

## Thanks

This plugin was started using the awesome [vim-plugin-starter-kit](https://github.com/JarrodCTaylor/vim-plugin-starter-kit) written by [JarrodCTaylor](https://github.com/JarrodCTaylor).

