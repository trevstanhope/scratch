/* A simple loop */

use std::int;

fn main() {
  loop {

    // Iterate
    let mut cake_amount = 8;
    while cake_amount > 0 {
        cake_amount -= 1;
    }

    // New classic loop
    let mut x = 5;
    loop {
      x += x - 3;
      if x % 5 == 0 { break; }
      println(int::to_str(x));
    }
  }
}
