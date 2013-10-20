/*
A vector is a contiguous section of memory containing zero or more
values of the same type. Like other types in Rust, vectors can be
stored on the stack, the local heap, or the exchange heap. Borrowed
pointers to vectors are also called 'slices'.
*/

fn main() {
  enum Crayon {
    Almond, AntiqueBrass, Apricot,
    Aquamarine, Asparagus, AtomicTangerine,
    BananaMania, Beaver, Bittersweet,
    Black, BlizzardBlue, Blue
  }

  // A fixed-size stack vector
  let stack_crayons: [Crayon, ..3] = [Almond, AntiqueBrass, Apricot];

  // A borrowed pointer to stack-allocated vector
  let stack_crayons: &[Crayon] = &[Aquamarine, Asparagus, AtomicTangerine];

  // A local heap (managed) vector of crayons
  let local_crayons: @[Crayon] = @[BananaMania, Beaver, Bittersweet];

  // Exchange heaps (owned) vector of crayons
  let exchange_crayons: ~[Crayon] = ~[Black, BlizzardBlue, Blue];
  let my_crayons = ~[Almond, AntiqueBrass, Apricot];
  let your_crayons = ~[BananaMania, Beaver, Bittersweet];

  // The `+` operator means concatenation when applied to vector types.
  // Add two vectors to create a new one
  let our_crayons = my_crayons + your_crayons;  

  // .push_all() will append to a vector, provided it lives in a mutable slot
  let mut my_crayons = my_crayons; // make my_crayons mutable
  my_crayons.push_all(your_crayons);
  
  fn draw_scene(c: Crayon) { }
  let crayons: [Crayon, ..3] = [BananaMania, Beaver, Bittersweet];
  match crayons[0] {
    Bittersweet => draw_scene(crayons[0]),
    _ => ()
  }

  // A vector can be destructured using pattern matching:
  let numbers: [int, ..3] = [1, 2, 3];
  let score = match numbers {
    [] => 0,
    [a] => a * 10,
    [a, b] => a * 6 + b * 4,
    [a, b, c, ..rest] => a * 5 + b * 3 + c * 2 + rest.len() as int
  };
}
