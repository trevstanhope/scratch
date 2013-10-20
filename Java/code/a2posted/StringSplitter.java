/*
This class provides a way to read an input String as a sequence of tokens
separated by whitespace. It allows you to access the tokens one by one,
in order.

YOU ARE NOT ALLOWED TO MODIFY THIS FILE, AND THERE IS NO NEED TO SUBMIT IT.
*/
public class StringSplitter {
	
	// Array of tokens extracted from the input String
	private String[] tokens;
	
	// Index of current token
	private int cur = 0;
	
	/**
	 * The constructor obtains the array of tokens from the input String.
	 */
	public StringSplitter (String s) {
		
	// The argument to String.split() below is a regular expression specifying
	// which characters separate tokens in the String. The special code "\\s"
	// signifies any whitespace character. You are NOT required to understand
	// Java regular expressions. But if you would like to understand them, 
	// you could try here:
	// http://docs.oracle.com/javase/tutorial/essential/regex/
	// http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html
		
		tokens = s.split("\\s");

	}
	
	/**
	 * Returns the number of tokens that are available to read with nextToken().
	 */
	public int countTokens () {
		
		return (tokens.length - cur);		
	}
	
	/**
	 * Returns true if there is at least one more token available to read
	 * with nextToken().
	 */
	public boolean hasMoreTokens() {
		
		return (cur < tokens.length);
		
	}
	
	/**
	 * Returns the next token, or the empty string "" if there are no more
	 * tokens.
	 */
	public String nextToken() {
		
		if (hasMoreTokens()) {
			String s = tokens[cur];
			cur++;
			return s;
		}
		
		else
			return "";
		
	}
	
	
}
