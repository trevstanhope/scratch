//  Trevor Stanhope
//  260399515
//  COMP 250 - Introduction to Computer Science - Fall 2012
//  Assignment #3

// Import statements.
import java.util.*;

// Trie Class
// Each node is associated with a prefix of some key 
// stored in the trie (Note any string is a prefix of itself).
public class Trie {
    private TrieNode root;

    // Empty tree has just a root node.  All the children are null.
    public Trie() {
        root = new TrieNode();
    }
    
    // Returns the root of the tree
    public TrieNode getRoot() {
        return root;
    }
   
    /**********************************************/
    // Return true if key was in the trie (i.e. it was added by insert).
    public boolean contains(String key) { 
        
        // Initialize objects.
        TrieNode current = getRoot(); // start temporary node at root
        
        // For each character, test if child exists
        for (int i=0; i < key.length(); i++) {
            // Assign current node to the child associated with the i-th character of the argument key.
            current = current.getChild(key.charAt(i));
            if (current == null) { // if one child does not exist, contains() fails
                return false;
            }
        }
        
        // Return true if the last node was an end of a key.
        return current.isEndOfKey();
    }
    /**********************************************/
   
    /**********************************************/
    // Insert key into the trie.  
    // The first step should be finding the longest prefix of key already in the trie.
    // Then add TrieNodes in such a way that the key is inserted.
    public void insert(String key) {
        
        // Initialize objects.
        TrieNode current = getPrefixNode(key); // start temporary node at prefix
        int depth = current.getDepth(); // find the depth of the prefix node
                
        // If the depth of the prefix is the depth of the key, setEndOfKey.
        // This handles the situation where the key existed in the tree, but was 
        // formalized as the end of a key.
        if (current.getDepth() == key.length()) {
            current.setEndOfKey(true);
        }  
        
        // For each character, create a new branch to the next child with the 
        // character of that ASCII value as the index reference.
        for (int i=depth; i < key.length(); i++) {
            current.createChild(key.charAt(i)); // index of the child is i-th char in key
            current = current.getChild(key.charAt(i));
            if (i == key.length() - 1) { // for the last node created isEndOfKey = true
                current.setEndOfKey(true);
            }
        }
    }
    /**********************************************/
   
    // Insert each key in the list (keys).
    public void loadKeys(ArrayList<String> keys) {
        for (int i = 0; i < keys.size(); i++) {
            System.out.println("Inserting " + keys.get(i));
            insert(keys.get(i));
        }
        return;
    }
   
    /**********************************************/
    // Return the TrieNode corresponding the longest prefix of a key that is found. 
    // If no prefix is found, return the root. 

    private TrieNode getPrefixNode(String word) {
        
        // Initialize objects.
        TrieNode current = getRoot(); // start temporary node at root
        
        // For each character, get next child until null or end of string.
        // A null return means that the word was either longer than any existing
        // keys, or contained an order of characters previously not in the tree.
        for (int i=0; i < word.length(); i++) {
        
            // After reaching a null branch, return the last existing node.
            if (current.getChild(word.charAt(i)) == null) {
			    return current;
            }
            // If the index for the child does exist, get the child node
            else {
                current = current.getChild(word.charAt(i));
			    continue;
            }
        }
        
        // If the word is in the tree, return the node associated with the last 
        // character in the word.
        return current;
    }
    /**********************************************/

    // Similar to getPrefixNode() but now return the prefix as a String, 
    // rather than as a TrieNode.   
    public String getPrefix(String word) {
        return getPrefixNode(word).toString();
    }

    /**********************************************/
    // Return a list of all keys in the trie that have the given prefix.  
    public ArrayList<String> getAllPrefixMatches(String prefix) {
    
        // Initialize objects.
        ArrayList<String> matches = new ArrayList<String>(); // list of matching keys
        ArrayList<String> empty = new ArrayList<String>(); // create empty message
        empty.add("No words begin with this prefix"); // throw error if empty
        TrieNode current = getRoot(); // start temporary node at root
	   
	    // Just like getPrefixNode(), but return error message for an empty set.
        for (int i = 0; i < prefix.length(); i++) {
            // If child node for i-th index exists, set current node to child node.
            if(current.getChild(prefix.charAt(i)) != null) {
                current = current.getChild(prefix.charAt(i));
            }
            // If child node is null, return empty message because no children
            // exist for the given prefix.
            else {
                return empty;
		    }
        }
        
        // Return results of the recursive function treeClimber(), which is a 
        // list of matching key strings, see the method treeClimber().
	    return treeClimber(current, matches);
    }
    /**********************************************/
    
    /**********************************************/
    // Recursion method for traversing the tree
    public ArrayList<String> treeClimber(TrieNode current, ArrayList<String> matches) {
        
        // For each of the 256 possible children, search for non-null nodes.
        // Here, the iteration limit is 256 because NUMCHILDREN = 256, i.e. 
        // there are 256 children per node that must be checked for key matches.
        for (int i = 0; i < 256; i++) {
        
            // If child node is null, disregard it and consider descendents of 
            // the next child
            if(current.getChild((char)i) == null) {
                continue;
            }
            
            // If the child node is the end of a key, store it in the list 
            // matches, and then recursively call treeClimber() with the last 
            // node as the starting node (i.e. the prefix).
            else if (current.getChild((char)i).isEndOfKey()) {
                matches.add(current.getChild((char)i).toString());
			    treeClimber(current.getChild((char)i), matches);
		    }   
		    // If the child node isn't null or the end of a key, recursively call
		    // treeClimber with the child node as the starting node.
		    else {
		        treeClimber(current.getChild((char)i), matches);
		    }
        }
        
        // Return the list of matching keys for the given prefix.
	    return matches;
    }
    /**********************************************/    
}
