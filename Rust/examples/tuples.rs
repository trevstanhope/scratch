fn main() {
  
  // tuple
  let mytup: (int, int, float) = (10, 20, 30.0);
  match mytup {
    (a, b, c) => info!(a + b + (c as int))
  }
  
  // tuple-struct
  struct MyTup(int, int, float);
  let mytup: MyTup = MyTup(10, 20, 30.0);
  match mytup {
    MyTup(a, b, c) => info!(a + b + (c as int))
  }
  
  // newtype
  struct SomeType(int);
  let sometype_id: SomeType = SomeType(10);
  let id_int: int = *sometype_id; // extract the contents with the dereference (`*`) unary operator:
  println(fmt!("%?", id_int));

  // use for newtypes
  struct Inches(int);
  struct Centimeters(int);
}
