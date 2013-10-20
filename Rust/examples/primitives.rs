fn main() {
  
  // types
  let a = 1;       // a is an int
  let b = 10i;     // b is an int, due to the 'i' suffix
  let c = 100u;    // c is a uint
  let d = 1000i32; // d is an i32

  // type-casting
  let x: float = 4.0;
  let y: uint = x as uint;
  assert!(y == 4u);
}
