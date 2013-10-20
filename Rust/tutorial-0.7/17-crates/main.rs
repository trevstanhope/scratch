use plants::need;
mod farm;
mod plants; 

fn main() {
  println("Welcome to Stanhope Farms...");
  ::farm::weed();
  ::farm::barn::feed();
  need();
}
