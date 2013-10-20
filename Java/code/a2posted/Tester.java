/*
Tester.java
Trevor Stanhope
260399515
*/

import java.util.HashMap;

public class Tester {

    public static void main(String... args) {   
        // define test cases
        HashMap<String, Boolean> testCases = new HashMap<String, Boolean>();
        testCases.put("23=foo", false);
		testCases.put("foo=23", true);
		testCases.put("foo=23 end", false);
		testCases.put("if true then a=1 end", true);
		testCases.put("if true then if true then a=1 end end", true);
		testCases.put("if true then if true then a=1 else a=1 end end", true);
		testCases.put("if true then if true then a=1 else a=1 end else a=1 end", true); // conjugate inside a conjugate
	    testCases.put("if true then if true then a=1 else a=1 else a=1 end else a=1 end", false); // double else
	    testCases.put("if true then if true then a=1 else a=1 end else if true then a=1 else a=1 end end", true); // conjugates inside a conjugate
	    testCases.put("if true then if true then a=1 else if true then a=1 end end else if true then a=1 else a=1 end end", true); // conjugates inside a conjugate
	    
	    // define iterators
		StringSplitter splitter;
		int trues = 0;
		int falses = 0;
		int fails = 0;
		int passes = 0;
		int total;
		
		// run tests
		for (String testCase : testCases.keySet()) {
			splitter = new StringSplitter(testCase);
			
			// count number of trues and falses
			if (testCases.get(testCase)) {
			    trues++;
			}
			else {
			    falses++;
			}
			
			// if a test fails, print it
			if (LanguageParser.parse(splitter) != testCases.get(testCase)) {
                fails++;
				System.out.println("Test case \"" + testCase +"\" failed!\nExpected result: " + 
						testCases.get(testCase) + "\nObtained result: " + !testCases.get(testCase) + "\n");
			}
			else {
			    passes++;
		    }
		}
		total = falses + trues;
		System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
		System.out.println("total cases passed : " + passes + " out of " + total);
		System.out.println("total cases failed: " + fails + " out of " + total);
		System.out.println("number of false tests: " + falses);
		System.out.println("number of true tests: " + trues);
	}
}
