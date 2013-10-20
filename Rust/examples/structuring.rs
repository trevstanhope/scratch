fn main() {
  struct Point {
    x: float,
    y: float
  }

  let mut mypoint = Point { x: 1.0, y: 1.0 };
  let mut origin = Point { x: 0.0, y: 0.0 };  // 
  mypoint.y += 1.0; // mypoint is mutable, and its fields as well
  origin.y += 1.0; // ERROR: assigning to immutable field if not mutable

  println("Match x and y");
  match mypoint {
    Point { x: 0.0, y: yy } => { println(yy.to_str());                     }
    Point { x: xx,  y: yy } => { println(xx.to_str() + " " + yy.to_str()); }
  }

  println("Match x-value");
  match mypoint {
    Point { x, _ } => { println(x.to_str()) } // x.to_str() is impt. float -> string op.
  }
}
