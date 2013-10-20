use std::float;

fn main() {
  let val1 = 4;
  let val2 = 5;
  let val3 = (1.0,2.0);
  let mut res1;
  let mut res2;
  let mut res3;
  res1 = is_four(val1);
  res2 = is_four(val2);
  res3 = angle(val3);
  println(fmt!("%?", res1));
  println(fmt!("%?",res2));
  println(fmt!("%?",res3));
}

// Compare x to 4
fn is_four(x: int) -> bool {
  // No need for a return statement. The result of the expression
  // is used as the return value.
  x == 4
}

// Compute angle for two floats (x,y)
fn angle(vector: (float, float)) -> float {
  let pi = float::consts::pi;
  match vector {
    (0f, y) if y < 0f => 1.5 * pi,
    (0f, y) => 0.5 * pi,
    (x, y) => float::atan(y / x)
  }
}
