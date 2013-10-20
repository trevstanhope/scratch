// displaying.rs

fn main() {
  let mystery_object = ();
  let val = 43;
  let sign = signum(val);
  println(fmt!("%s is %d", "the value", val));
  println(fmt!("what is this thing: %?", mystery_object));
  println(fmt!("its sign is: %?", sign));
}

// Determine sign of number
fn signum(x: int) -> int {
  if x < 0 { -1 }
  else if x > 0 { 1 }
  else { return 0 }
}
