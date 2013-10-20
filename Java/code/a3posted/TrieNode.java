//  Trevor Stanhope
//  260399515
//  COMP 250 - Introduction to Computer Science - Fall 2012
//  Assignment #3

/*
A node in a Trie (prefix) tree.  
It contains an array of children: one for each possible character.
The ith child of a node corresponds to character (char)i
which is the UNICODE (and ASCII) value of i. 
Similarly the index of character c is (int)c.
So children[97] = children[ (int) 'a']  would contain the child for 'a' 
since (char)97 == 'a'   and  (int)'a' == 97.
References:
For all unicode charactors, see http://unicode.org/charts
In particular, the ascii characters are listed at http://unicode.org/charts/PDF/U0000.pdf
For ascii table, see http://www.asciitable.com/
*/

public class TrieNode {
	// Highest allowable character index is NUMCHILDREN-1
	// Assuming one-byte ASCII i.e. "extended ASCII"
	// NUMCHILDREN is constant (static and final).  
	// To access it, you need to say "TrieNode.NUMCHILDREN"
    public static final int NUMCHILDREN = 256;
    private TrieNode parent;
    private TrieNode[] children;
    private int depth;          // 0 for root, 1 for root's children, 2 for their children, etc..
    private char indexInParent; // character associated with edge between node and its parent
    private boolean endOfKey;   // set to true of prefix associated with node is also a key.
   
    // Construct new, empty node with NUMCHILDREN children.
    // All the children are null. 
    public TrieNode() {
        children = new TrieNode[NUMCHILDREN];
        endOfKey = false;
        depth = 0; 
        indexInParent = (char)0; 
    }

    /**********************************************/
    // Add a child node to the current node. 
    // The child is associated with the character specified by the index. 
    public TrieNode createChild(char index) {	
        // Initialize new TrieNode object. 
        TrieNode child = new TrieNode();
        
        // Set attributes of child-parent branch.
        child.indexInParent = index; // sets the branch equal to the character
        this.children[index] = child; // set the branch from parent to child
        child.parent = this; // link child to its parent
        child.depth = this.getDepth() + 1; // increase parent depth by 1
        
        // Return the newly created child node.
        return child;
    }
    /**********************************************/

    // Get the child node associated with a given character, i.e. that character is on 
    // the edge from this node to the child.  The child could be null.  
    public TrieNode getChild(char index) {
        return children[(int) index];
    }

    // Test whether the path from the root to this node is a key in the trie.  
    // Return true if it is, false if it is prefix but not a key.
    public boolean isEndOfKey() {
        return endOfKey;
    }
   
    // Set to true for the node associated with the last character of a word.
    public void setEndOfKey(boolean endOfKey) {
        this.endOfKey = endOfKey;
    }

    // Depth of node (distance from root).
    public int getDepth() {
        return depth;
    }

    // Get the parent
    public TrieNode getParent() {
        return parent;
    }

    // Returns x such that parent.getChild(x) == this. 
    public char getIndexInParent() {
        return indexInParent;
    }

    /**********************************************/
    // Return the prefix (as a String) associated with this node.
    public String toString() {
    
        // Initialize objects.
        char[] word = new char[depth]; // create character array for the word
	    TrieNode current = this; // start temporary node at 'this'
	    
	    // Traverse towards root, adding each branch index to char[] 'words'.
	    for(int i = 1; i <= depth; i++) {
	        // In order to avoid reversing the array later, word[depth-i]
	        // builds the character array backwards, starting at word[depth-1].
            word[depth-i] = (char) current.getIndexInParent();
            current = current.getParent();
        }
        
        // Convert char[] word to String 'prefix' and return it as output.
        String prefix = new String(word);
        return prefix;
    }
    /**********************************************/
}
