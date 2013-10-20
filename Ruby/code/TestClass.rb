#!/usr/bin/env ruby
class TestClass
  def initialize(word = "Word")
    @word = word
  end
  def print
    puts "#{@word}!"
  end
end

word = TestClass.new("Something")
word.print
puts "Global Methods..."
puts TestClass.instance_methods
puts "Local Methods..."
puts TestClass.instance_methods(false)

