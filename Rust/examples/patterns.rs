// match structures
fn main() {

  // some number
  let val1 = -1;
  let val2 = 0;

  // match structure without {}
  match val1 {
    0     => println("zero"),
    1 | 2 => println("one or two"),
    3..10 => println("three to ten"),
    _     => println("something else")
  }

  // match structure with {}
  match val2 {
    0 => { println("zero") }
    _ => { println("something else") }
  }
}
