/*
LanguageParser.java
Trevor Stanhope
260399515
*/

public class LanguageParser {
	
        /* 
        Simple Language Terms; These methods simply pattern match for recognized tokens
        */
        private static boolean isBoolean (String token) {
	        return (token.equals("true") || token.equals("false"));
        }
        private static boolean isAssignment (String token) {
	        return (token.matches("[a-zA-Z]+=\\d+"));	
        }
        private static boolean isIf (String token) {
	        return (token.equals("if"));	
        }
        private static boolean isThen (String token) {
	        return (token.equals("then"));	
        }
        private static boolean isElse (String token) {
	        return (token.equals("else"));	
        }
        private static boolean isEnd (String token) {
	        return (token.equals("end"));	
        }
        private static boolean isEmpty (String token) {
	        return (token.equals(""));	
        }
    
        /*
        Complex Language Terms; These methods pattern match for terms that represent more complex syntax
        */
        private static boolean isCondition (String token) {
	        return (token.equals("condition"));	// if + true = condition
        }
        private static boolean isClause (String token) {
	        return (token.equals("clause")); // condition + then = clause
        }
        private static boolean isPhrase (String token) {
	        return (token.equals("phrase")); // clause + assignment = phrase
        }
        private static boolean isException (String token) {
	        return (token.equals("exception")); // phrase + else = exception
        }
        private static boolean isConjugate (String token) {
	        return (token.equals("conjugate")); // exception + assignment = conjugate
        }
        private static boolean isStatement (String token) {
	        return (token.equals("statement"));	// statement = assignment || phrase + end || conjugate + end
        }

    /*
    Parse; Given any sequence of tokens in a splitter object, returns 'true' if it meets valid syntax
    */
    public static boolean parse(StringSplitter splitter) {

	    // declare objects
	    StringStack stack = new StringStack(); // the stack of tokens to be sorted
	    String newToken; // the next token from the splitter object
	    String topToken; // the top token from the stack

	    // for each token in the splitter object ...
        while(splitter.hasMoreTokens()) {

	        // catch the next token from the splitter
	        newToken = splitter.nextToken();
	        // get the top token from the stack
	        topToken = stack.peek();
	        
	        /*
	        Handlers; Match each caught token to a recognized term then do something
	        */
	        // If-Handler
	        if (isIf(newToken)) {
	            // ifs can only come first, or after clauses/exceptions
	    	    if (isEmpty(topToken) || isClause(topToken) || isException(topToken)) {
		            stack.push(newToken);
	        	}
		        else {
    		        return false;
    		    }
            }
    	    
    	    // Boolean-Handler
    	    else if (isBoolean(newToken)) {
    		    // booleans can only come after ifs
    		    if (isIf(topToken)) {
    		        stack.pop();
    		        stack.push("condition"); // if + boolean = condition
    		    }
    		    else {
    		        return false; 
    		    }
    	    }
    	    
    	    // Then-Handler
    	    else if (isThen(newToken)) {
    		    if (isCondition(topToken)) {
    		        stack.pop();
    		        stack.push("clause"); // condition + then = clause
    		    }
    		    else {
    		        return false;
    		    }
    	    }
    	    
    	    // Else-Handler
    	    else if (isElse(newToken)) {
    		    if (isPhrase(topToken)) {
    		        stack.pop();
    		        stack.push("exception"); // phrase + else = exception
    		    }
    		    else {
    		        return false;
    		    }
    	    }
    	    
    	    // Assignment-Handler
    	    else if (isAssignment(newToken)) {
    		    if (isClause(topToken)) {
    		        stack.pop();
    		        stack.push("phrase"); // clause + assignment = phrase
    		    }
    		    else if (isException(topToken)) {
    		        stack.pop();
    		        stack.push("conjugate"); // exception + assignment = conjugate
    		    } 
    		    else if (isEmpty(topToken)) {
    		        stack.pop();
    		        stack.push("statement"); // assignment = statement
    		    }
    		    else {
    		        return false;
    		    }
    	    }
    	    
    	    // End-Handler
    	    else if (isEnd(newToken)) {
    	        if (isPhrase(topToken)) {
    	            stack.pop(); // pop phrase
    	            if (isClause(stack.peek())) {
    	                stack.pop();
    	                stack.push("phrase"); // replace the preceding clause with a phrase
    	            }
    	            else if (isException(stack.peek())) {
    	                stack.pop();
    	                stack.push("conjugate"); // replace the preceding exception with a conjugate
    	            }
    	            else if (stack.isEmpty()) {
    	                stack.push("statement"); // if there is nothing after the last phrase, the stack was a complete statement
    	            }
    	        }
    	        else if (isConjugate(topToken)) {
    	            stack.pop(); // pop conjugate
    	            if (isClause(stack.peek())) {
    	                stack.pop();
    	                stack.push("phrase"); // replace the preceding clause with a phrase
    	            }
    	            else if (isException(stack.peek())) {
    	                stack.pop();
    	                stack.push("conjugate"); // replace the preceding exception with a conjugate
    	            }
    	            else if (stack.isEmpty()) {
    	                stack.push("statement"); // if there is nothing after the last conjugate, the stack was a complete statement
    	            }
    	        }
    	        else { // this is primarily for the case of (assignment, end) 
    	            return false;
    	        }
    	    }
    		  
    	    // Null-Handler, if a caught token does not match any recognized terms return false
    	    else {
    	        return false;
    	    }
    	}
    
        // You should now only have a stack with a single 'statement'
	    if (isStatement(stack.pop()) && stack.isEmpty()) {
	        return true;
	    }
	    // This else is somewhat redundant as the vast majority (if not all) of the cases will return false in the loop
	    else {
	        return false;
        }
    }
}
