mod farm { // no ()

  struct Human { name: ~str } // need to own ALL strings
  
  struct Chicken { weight: float }
  
  pub struct Field {
    priv chickens: ~[Chicken],
    farmer: Human
  }
    
  pub fn weed() { println("Weeding"); seed(); } // seed() is in local scope
  
  fn seed() { println("Seeding"); }
  
  mod barn { // no ()
    pub fn feed() { println("Feeding"); } // feed() is now available to barn
  }
  
  
//  impl Farm {
//    fn feed_chickens(&self) { println("Feeding Chickens"); }
//    pub fn add_chicken(&self, c: Chicken) { println("Adding Chicken"); }
//  }
//  
//  pub fn feed_animals(farm: &Farm) {
//    farm.feed_chickens();
//  }
}

fn main() {
  println("Welcome to Stanhope Farms...");
  ::farm::weed();
  ::farm::barn::feed();
}
