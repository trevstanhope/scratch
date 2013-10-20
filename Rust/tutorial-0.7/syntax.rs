/*
  Tutorail Part 3 - Syntax Basics
*/

fn main() {
  
  // Let 'word' be default type
  let word = "word";

  // let 'count' be default mutable (i.e. int)
  let mut count = 0;

  // let 'unused' be an unused variable with '_'
  let _unused = 0; // mutable unused variables will give warnings

  // set 'FACTOR' be a static float
  // floating point can be written 0.0,  1e6 or 2.1e-4
  static FACTOR: float = 57.8; // ':' is the 'set' declaration
  static ENG_FACTOR: float = 1e7;

  // let 'size' be its default type
  let _size = FACTOR * 10.0;

  // set type for size
  let _size: int = 50;

  // continously loop until break
  loop {
    // if-statements are like funtions, the result is returned
    let boolean = 
      if count == 10 {
        count -= 4;
        true // returned because no ';'
      } else if count == 7 {
        count -= 3;
        true // returned because no ';'
      } else {
        if is_four(count) {
          count -= 3;
          false // returned because no ';'
        } else {
          count += 2;
          true // returned because no ';'
        }
      };
    println(fmt!("%? %?", word, boolean));
  }
}

// Function
fn is_four(x: int) -> bool {
  x == 4 // returns bool because it is without ';'
}
