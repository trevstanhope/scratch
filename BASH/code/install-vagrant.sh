#!/bin/sh
bash < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer )
'[[ -s "$HOME/.rvm/scripts/rvm" ]]' && . "$HOME/.rvm/scripts/rvm"
rvm pkg install openssl
rvm pkg install zlib
rvm install 1.9.2 --with-openssl-dir=$rvm_path/usr --with-zlib-dir=$rvm_path/usr
rvm --default 1.9.2
gem install vagrant
wget http://download.virtualbox.org/virtualbox/4.1.6/virtualbox-4.1_4.1.6-74727~Ubuntu~lucid_i386.deb
dpkg -i virtualbox*.deb
