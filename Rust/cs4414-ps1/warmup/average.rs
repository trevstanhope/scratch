/*
  Average
*/

use std::{os, uint}; // list of modules to use from crate 'std'

fn main() {
  let args: ~[~str] = os::args(); // get args
  let mut i = 1;
  let mut sum = 0;
  let length = args.len();
  let mut valid = 0;
  while i < length {
    // from_str() returns an Option, which is more or less an error statement
    // if there is nothing in the option, then there was an error
    // else there is was no error
    if uint::from_str(args[i]).is_none() { // unwrap the Option, which may fail
      println(fmt!("That isn't a number: %s", args[i]));
    }
    else {
      sum += uint::from_str(args[i]).unwrap(); // unwrap the option
      valid += 1;
    }
    i += 1;
  }
  
  /* re-cast as float */
  let sum: float = sum as float;
  let numbers: float = valid as float; // length of args vector is 1 greater than input args
  let average: float = sum/numbers;
  println(fmt!("sum: %?", sum));
  println(fmt!("average: %?", average))
}
