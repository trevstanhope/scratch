#!/bin/sh
# Copies and archives important system files.
# Trevor Stanhope
DIR_NAME='USER_BACKUP'
mkdir $DIR_NAME
cd $DIR_NAME

# Directories to backup
cp -r $HOME/.ssh/* .
cp -r $HOME/lib*/ .
cp -r $HOME/loc*/ .
cp -r $HOME/scr*/ .

# Files to backup
cp /etc/apt/sources.list .
cp /etc/hosts .
cp $HOME/.gitconfig . 
cp $HOME/.profile . 
cp $HOME/.bashrc .
cp $HOME/.xinitrc .

