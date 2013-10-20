use std::float;

fn main() {

  // a structure object
  struct Point { x: float, y: float }

  // enum objects cannot share the same name (even in different enums)
  // an enum is a list that can be iterated
  enum Shape1 {
    Circle1(Point, float),
    Rectangle1(Point, Point)
  }
  
  enum Shape2 {
      Circle2 { center: Point, radius: float },
      Rectangle2 { top_left: Point, bottom_right: Point }
  }

  enum Direction {
    North,
    East,
    South,
    West
  }

  enum Color {
    Red = 0xff0000,
    Green = 0x00ff00,
    Blue = 0x0000ff
  }

  /* --- functions inside a function --- */
  // needs Shape struct defined in container function
  fn area1(sh: Shape1) -> float {
    match sh {
      Circle1(_, size) => float::consts::pi * size * size,
      Rectangle1(Point { x, y }, Point { x: x2, y: y2 }) => (x2 - x) * (y2 - y)
    }
  }

  // Takes Direction enum, returns Point
  fn point_from_direction(dir: Direction) -> Point {
    match dir {
      North => Point { x:  0f, y:  1f }, // 0 float, 1 float
      East  => Point { x:  1f, y:  0f }, // 1 float, 0 float
      South => Point { x:  0f, y: -1f }, // 0 float, -1 float
      West  => Point { x: -1f, y:  0f } // -1 float, 0 float
    }
  }
  
  // Takes float, returns float
  fn square(x: float) -> float { x * x }

  fn area(sh: Shape2) -> float {
    match sh {
      Circle2 { radius: radius, _ } => float::consts::pi * square(radius),
      Rectangle2 { top_left: top_left, bottom_right: bottom_right } => {
        (bottom_right.x - top_left.x) * (bottom_right.y - top_left.y)
        }
    }
  }
}
