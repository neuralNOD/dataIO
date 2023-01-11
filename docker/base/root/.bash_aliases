# bash aliases to make life easier!
# the file is included in ~/.zshrc or ~/.bashrc to be recognized
# https://gitlab.com/ZenithClown/computer-configurations-and-setups/-/tree/master/Mint-20#bashrc-configurations

system-upgrade() {
  # update all the available packages and
  # also upgrades the packages after confirmation
  sudo apt update
  sudo apt upgrade
}

apt-clean() {
  # remove optional packages and cache from apt
  # https://askubuntu.com/a/172516/521338
  sudo apt autoremove
  sudo apt autoclean
}

# git aliases are now configured using `.gitconfig` files
# thus previously used commands are now replaced using aliases
# use the `git` alias `g` followed by aliases defined under `.gitconfig/[alias]`
# example: initialize a directory with `g i`
alias g='git'

# list of other command aliases are defined below
alias ls='ls -lah --color=auto'
alias ll='ls -alF --color=auto'
alias os='lsb_release -a'

# lets forget the confusion b/w `md` and `mkdir` war of windows/linus
alias md='mkdir'
