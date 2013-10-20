/*
  Echo
*/
use std::{os, uint}; // use OS input

fn main() {
  let args: ~[~str] = os::args(); // get args
  println(fmt!("%?",args)); // print args
}
