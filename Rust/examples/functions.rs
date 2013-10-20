fn main() {

  // arguments are a list of expression:type pairs
  // -> points to the return type
  fn line1(a: int, b: int, x: int) -> int {
    return a * x + b;
  }

  // arguments are a list of expression:type pairs
  // -> points to the return type
  fn line2(a: int, b: int, x: int) -> int {
    a * x + b
  }

  // fails to return because there is a semicolon and no return...
  fn line3(a: int, b: int, x: int) -> ()  { a * x + b; }

  fn do_nothing_the_hard_way() -> () {
    return ();
  }

  fn do_nothing_the_easy_way() {}
  
  assert!(8 == line(5, 3, 1));
  assert!(() == oops(5, 3, 1));
  
  // pattern match argument, only return the head
  fn first((value, _): (int, float)) -> int { value }

}
