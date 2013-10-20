/*
  Module file to be included in main.rs
  Note: No module declaration is needed, this is essentially
        the body of the `farm` module
*/

struct Human { name: ~str } // need to own ALL strings
  
struct Chicken { weight: float }
  
pub struct Field {
  priv chickens: ~[Chicken],
  farmer: Human
}
    
pub fn weed() { println("Weeding"); seed(); } // seed() is in local scope
  
fn seed() { println("Seeding"); }
  
pub mod barn { // no (), needs to be a public module
  pub fn feed() { println("Feeding"); } // feed() is now available to barn
}
