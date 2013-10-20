//  COMP 250 - Introduction to Computer Science - Fall 2012
//  Assignment #3 - Question 1

import java.io.*;
import java.util.*;

// Performs lookups and autocompletes using the Trie structure; 
// Also provides method to read from a file.

public class AutoComplete
{
	public static ArrayList<String> readWordsFromFile(String filename)
	{
		ArrayList<String> words = new ArrayList<String>();
		try
		{
			File file = new File(filename);
			Scanner scanner = new Scanner(file);
			// Strip non-alphanumeric \\W
			scanner.useDelimiter("\\W+"); 
			while (scanner.hasNext())
			{
				words.add(scanner.next());
			}
		}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
			System.exit(1);
		}
		return words;
	}

	public static void main(String[] args)
	{	   
		ArrayList<String> list = new ArrayList<String>();

/*      Test with an input file.
 *	  Your assignment will be graded using a different input file,
 *	  If you wish to share your outputs on the given input file, that's fine. 
 *		
 *	  You will need to put a different pathname in here.
 *		
 *		String fileName = "C:\\Program Files\\eclipse\\workspace\\2012\\src\\a3\\inputFile.txt";
 *		list = readWordsFromFile(fileName);
*/
		
		//   For debugging, you may wish to use a small set of keys only.      

		Collections.addAll(list, "an", "a", "and", "ax", "dog", "door", "dot");

		Trie   trie = new Trie();
		trie.loadKeys(list);

		System.out.println("list contains " + list.size() + " keys");

		// Test if contains() works, print input and output
		//
		//  e.g.: try door, an, cat (should return true, false, and false respectively)

		System.out.println();
		System.out.println("---  Test contains() method.   Correct answer shown in brackets. -----" );
		System.out.println("trie contains 'door' = " + trie.contains("door") + " (true)" );
		System.out.println("trie contains 'and' = " + trie.contains("and")   + " (true)");
		System.out.println("trie contains 'cat' = " + trie.contains("cat")   + " (false)");
		System.out.println("trie contains 'dog' = " + trie.contains("dog")   + " (true)");
		System.out.println("trie contains 'ax' = " + trie.contains("ax")     + " (true)");
		System.out.println("trie contains 'dot' = " + trie.contains("dot")   + " (true)");
		System.out.println("trie contains 'a' = " + trie.contains("a")       + " (true)");
		System.out.println("trie contains 'an' = " + trie.contains("an")     + " (true)");      

		//  Test if getLongestMatchingPrefix works, print input and output
		//    ex: try door, any, cat (should return door, an, and null respectively

		System.out.println("");
		System.out.println("-----  Test getPrefix()");		
		System.out.println("longest prefix of door = " + trie.getPrefix("door"));
		System.out.println("longest prefix of any = " + trie.getPrefix("any"));
		System.out.println("longest prefix of cat = " + trie.getPrefix("cat"));

		// Test getMatches, print input and output
		// ex: try a, do, c (should return {a, and, ax}, {dog, door, dot}, null respectively)

		System.out.println("");
		System.out.println("-----  Test getAllPrefixMatches()  i.e. autocomplete ");		
		System.out.println("autocomplete a = " + trie.getAllPrefixMatches("a"));
		System.out.println("autocomplete do = " + trie.getAllPrefixMatches("do"));
		System.out.println("autocomplete c = " + trie.getAllPrefixMatches("c"));

	}
}
