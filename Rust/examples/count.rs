// not using a variable throws warning

fn main() {
  let hi = "hi";
  let mut count = 0;

  while count < 10 {
      println(fmt!("%? count: %? ", hi, count));
      count += 1;
  }
}
