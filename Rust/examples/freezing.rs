// Borrowing an immutable pointer to an object freezes it and prevents mutation.
// `Owned` objects have freezing enforced statically at compile-time.

fn main() {

  // x is now unfrozen
  let mut x = 5;
  {
    let y = &x; // x is now frozen, it cannot be modified
  }
  // x is now unfrozen
  
  let x = @mut 5;
  let y = x;
  {
    let z = &*y; // the managed box is now frozen
    // modifying it through x or y will cause a task failure
  }
  // the box is now unfrozen again

}
