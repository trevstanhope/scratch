/* Here the `&` operator is used to take the address of the variable
`on_the_stack`; this is because `on_the_stack` has the type `Point`
(that is, a struct value) and we have to take its address to get a
value. We also call this _borrowing_ the local variable
`on_the_stack`, because we are creating an alias: that is, another
route to the same data. */

/* In the case of the boxes `managed_box` and `owned_box`, however, no
explicit action is necessary. The compiler will automatically convert
a box like `@point` or `~point` to a borrowed pointer like
`&point`. This is another form of borrowing; in this case, the
contents of the managed/owned box are being lent out. */

fn main() {

  struct Point { x: float, y: float }

  let on_the_stack: Point = Point { x: 3.0, y: 4.0 };
  let managed_box: @Point = @Point { x: 5.0, y: 1.0 };
  let owned_box: ~Point = ~Point { x: 7.0, y: 9.0 };

  fn sqrt(f: float) -> float { f }

  fn compute_distance(p1: &Point, p2: &Point) -> float {
    let x_d = p1.x - p2.x;
    let y_d = p1.y - p2.y;
    sqrt(x_d * x_d + y_d * y_d)
  }

  let val1: float = compute_distance(&on_the_stack, managed_box);
  let val2: float = compute_distance(managed_box, owned_box);
  
  println(fmt!("%?, %?", val1, val2));
}
