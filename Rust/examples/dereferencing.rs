fn main() {
  
  // Rust uses the unary star operator (`*`) to access the contents of a
  // box or pointer, similarly to C.
  let managed = @10;
  let owned = ~20;
  let borrowed = &30;
  let sum = *managed + *owned + *borrowed;

  // Dereferenced mutable pointers may appear on the left hand side of
  // assignments. Such an assignment modifies the value that the pointer
  // points to.
  let managed = @mut 10;
  let mut owned = ~20;
  let mut value = 30;
  let borrowed = &mut value;
  *managed = *owned + 10;
  *owned = *borrowed + 100;
  *borrowed = *managed + 1000;

  // Pointers have high operator precedence, but lower precedence than the
  // dot operator used for field and method access. This precedence order
  // can sometimes make code awkward and parenthesis-filled.
  struct Point { x: float, y: float }
  enum Shape { Rectangle(Point, Point) }
  impl Shape { fn area(&self) -> int { 0 } }
  let start = @Point { x: 10f, y: 20f };
  let end = ~Point { x: (*start).x + 100f, y: (*start).y + 100f };
  let rect = &Rectangle(*start, *end);
  let area = (*rect).area();

  // To combat this ugliness the dot operator applies _automatic pointer
  // dereferencing_ to the receiver (the value on the left-hand side of the
  // dot), so in most cases, explicitly dereferencing the receiver is not necessary.
  struct Point { x: float, y: float }
  enum Shape { Rectangle(Point, Point) }
  impl Shape { fn area(&self) -> int { 0 } }
  let start = @Point { x: 10f, y: 20f };
  let end = ~Point { x: start.x + 100f, y: start.y + 100f };
  let rect = &Rectangle(*start, *end);
  let area = rect.area();

  // You can write an expression that dereferences any number of pointers
  // automatically. For example, if you feel inclined, you could write
  // something silly like
  struct Point { x: float, y: float }
  let point = &@~Point { x: 10f, y: 20f };
  println(fmt!("%f", point.x));

}
