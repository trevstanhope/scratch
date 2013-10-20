#!/usr/bin/env ruby

class SuperTestClass

  attr_accessor :word

  # Create the object
  def initialize(word = "Word")
    @word = word
  end

  # Print the word(s)
  def print
    if @word.nil?
      puts "..."
    elsif @word.respond_to?("each")
      # If @names is a list of some kind, iterate!
      @word.each do |temp|
        puts "#{temp}"
      end
    else
      puts "#{@word}"
    end
  end

  # Print all words at once
  def printall
    if @word.nil?
      puts "..."
    elsif @word.respond_to?("join")
      # Join the list elements with commas
      puts "#{@word.join(", ")}"
    else
      puts "#{@word}"
    end
  end

end


if __FILE__ == $0
  words = SuperTestClass.new
  words.print
  words.printall

  # Single word
  words.word = "Something"
  words.print
  words.printall

  # Multiple words
  words.word = ["This", "That", "These", "Those"]
  words.print
  words.printall

  # Change to nil
  words.word = nil
  words.print
  words.printall
end
