/*
An owned box (`~`) is a uniquely owned allocation on the heap. It inherits the
mutability and lifetime of the owner as it would if there was no box:
*/

fn main() {

  let x = 5; // immutable
  let mut y = 5; // mutable
  y += 2;
  println(fmt!("%?",y));

  let x = ~5; // immutable
  let mut y = ~5; // mutable
  *y += 2; // the * operator is needed to access the contained value
  println(fmt!("%?",y));

  // should fail to compile
//  struct Foo {
//    child: Option<Foo>
//  }
  
  // will compile
  struct Foo {
    child: Option<~Foo>
  }

  // @ symbolizes a managed box
  let a = @5; // immutable
  let mut b = @5; // mutable variable, immutable box
  let c = @mut 5; // immutable variable, mutable box
  b = @10;
  *c = 10;

  let mut d = @mut 5; // mutable variable, mutable box
  *d += 5;
  d = @mut 15;

  let a = @1; // immutable box
  let b = @mut 2; // mutable box
  let mut c: @int; // declare a variable with type managed immutable int
  let mut d: @mut int; // and one of type managed mutable int
  c = a; // box type is the same, okay
  d = b; // box type is the same, okay

}
