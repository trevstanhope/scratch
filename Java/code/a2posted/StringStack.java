import java.util.LinkedList;

/*
This class implements the Stack ADT for Strings of non-zero length.
*/
public class StringStack {
	
	
	// The stack is represented using a linked list of String elements.
	private LinkedList<String> list;
	
	
	/**
	 * Constructor, which simply creates the linked list
	 */
	public StringStack () {
		
		list = new LinkedList<String>();
		
	}
	
	/**
	 * Returns true is the stack is empty, false otherwise.
	 */
	public boolean isEmpty () {
		
		return list.isEmpty();
		
	}
	
	/**
	 * Pushes the given String onto the stack.
	 * 
	 * NOTE: EMPTY STRINGS ARE NOT ALLOWED ON THE STACK.
	 *       If the given string has length zero, this method
	 *       should have no effect on the stack.
	 */
	public void push (String s) {
		
		if (s.length() > 0)
			list.addFirst(s);
		
	}
	
	/**
	 * Removes the String on top of the stack and returns it.
	 * 
	 * NOTE: IF THE STACK IS EMPTY, THIS METHOD SHOULD RETURN
	 *       AN EMPTY STRING: ""
	 */
	public String pop () {
		
		if (isEmpty())
			return "";
		else
			return list.removeFirst();
		
	}
	
	/**
	 * Returns the String on top of the stack without removing it.
	 * 
	 * NOTE: IF THE STACK IS EMPTY, THIS METHOD SHOULD RETURN
	 *       AN EMPTY STRING: ""
	 */
	public String peek () {
		
		if (isEmpty())
			return "";
		else
			return list.getFirst();
		
	}
	
	
}
