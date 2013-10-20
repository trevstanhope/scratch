fn main() {
  {
    // an integer allocated on the heap
    let y = ~10;
  }

  // the struct owns the objects contained in the `x` and `y` fields
  // when `a` goes out of scope, the destructor for the `~int` in the struct's
  // field is called
  struct Foo { x: int, y: ~int }

  {
    // `a` is the owner of the struct, and thus the owner of the struct's fields
    let a = Foo { x: 5, y: ~10 };
  }

  // `b` is mutable, and the mutability is inherited by the objects it owns
  let mut b = Foo { x: 5, y: ~10 };
  b.x = 10;

}
