/**
 * Implements an binary search tree.
 * @author Mark Allen Weiss  (from textbook "Data Structures and Algorithm Analysis in Java")
 * Modified by M Langer March 2011
 */

//  public class BinarySearchTree<T extends Comparable<? super T>>
//
//  M. Langer:   I  simplified the generic type below to remove the wildcards.
//  In the generic type parameter of the class, it says "T extends ..."  rather
//  than "T implements ..."    If you write the latter, it doesn't compile.
//  Seem a bit weird to me...  

public class BinarySearchTree <T extends Comparable<T>>  implements Iterable<T>
{
	BSTNode<T> root;    //   give it package visibility because the iterator needs
                        //   access to the nodes.
    /**
     * Constructor
     */
	
    public BinarySearchTree( )
    {
        root = null;
    }

    /**
     * Insert element into the tree; duplicates are ignored.
     * @param x the item to insert.
     */
    
    public void insert( T x )
    {
        root = insert( x, root );     //  see private insert method below
    }

    /**
     * Remove element from the tree. Nothing is done if x is not found.
     * @param x the element to remove.
     */
    
    public void remove( T x )
    {
        root = remove( x, root );
    }

    /**
     * Find the smallest element in the tree.
     * @return smallest element or null if empty.
     */
    
    public T findMin( )
    {
		if( isEmpty( ) )
			return null;
        return findMin( root ).element;           //  see private method below
    }

    /**
     * Find the largest element in the tree.
     * @return the largest element or null if empty.
     */
    public T findMax( )
    {
		if( isEmpty( ) )
			return null;
        return findMax( root ).element;
    }

    /**
     * Find an element in the tree.
     * @param x the element to search for.
     * @return true if not found.
     */
    public boolean contains( T x )
    {
        return contains( x, root );
    }

    /**
     * Make the tree logically empty.
     */
    public void makeEmpty( )
    {
        root = null;
    }

    /**
     * Test if the tree is logically empty.
     * @return true if empty, false otherwise.
     */
    public boolean isEmpty( )
    {
        return root == null;
    }

    /**
     * Print the tree contents in sorted order.
     */
    public void printTree( )
    {
        if( isEmpty( ) )
            System.out.println( "Empty tree" );
        else
            printTree( root );
    }

	/*   
	 *   @author  M. Langer.    Adapted from an idea by Pritchard and Carrano.
	 *                          "Java Walls and Mirrors"  book  
	 *                          
	 *                          unclear about whether I need "static" 
	 */

	public BSTIterator<T> iterator() {
		 BSTIterator<T>  iter = new BSTIterator<T>(root);
		 return iter;
	}
	
	
//  --------------------------   private or package methods ------------------------------------
    
    /**
     * Internal method to insert into a subtree.
     * @param x the element to insert.
     * @param t the node that roots the subtree.
     * @return the new root of the subtree.
     */
    private BSTNode<T> insert( T x, BSTNode<T> t )
    {
        if( t == null )
            return new BSTNode<T>( x, null, null );
		
		int compareResult = x.compareTo( t.element );
			
        if( compareResult < 0 )
            t.left = insert( x, t.left );
        else if( compareResult > 0 )
            t.right = insert( x, t.right );
        else
            ;  // x is already there, so do nothing
        return t;
    }

    /**
     * Internal method to remove from a subtree.
     * @param x the element to remove.
     * @param t the node that roots the subtree.
     * @return the new root of the subtree.
     */
    
    private BSTNode<T> remove( T x, BSTNode<T> t )
    {
        if( t == null )
            return t;   // element not found; do nothing
			
		int compareResult = x.compareTo( t.element );
			
        if( compareResult < 0 )
            t.left = remove( x, t.left );
        else if( compareResult > 0 )
            t.right = remove( x, t.right );
        else //  remove root
        	if( t.left != null && t.right != null ) // two children
        	{
        		t.element = findMin( t.right ).element;
        		t.right = remove( t.element, t.right );
        	}
        	else
        		t = ( t.left != null ) ? t.left : t.right;
        return t;
    }

    /**
     * Internal method to find the smallest element in a subtree.
     * @param t the node that roots the subtree.
     * @return node containing the smallest element.
     */
    private BSTNode<T> findMin( BSTNode<T> t )
    {
        if( t == null )
            return null;
        else if( t.left == null )
            return t;
        return findMin( t.left );
    }

    /**
     * Internal method to find the largest element in a subtree.
     * @param t the node that roots the subtree.
     * @return node containing the largest element.
     */
    private BSTNode<T> findMax( BSTNode<T> t )
    {
        if( t != null )
            while( t.right != null )
                t = t.right;

        return t;
    }

    /**
     * Internal method to find an element in a subtree.
     * @param x is element to search for.
     * @param t the node that roots the subtree.
     * @return node containing the matched element.
     */
    private boolean contains( T x, BSTNode<T> t )
    {
        if( t == null )
            return false;
			
		int compareResult = x.compareTo( t.element );
			
        if( compareResult < 0 )
            return contains( x, t.left );
        else if( compareResult > 0 )
            return contains( x, t.right );
        else
            return true;    // Match
    }

    /**
     * Internal method to print a subtree in sorted order.
     * @param t the node that roots the subtree.
     */
    
    private void printTree( BSTNode<T> t )
    {
        if( t != null )
        {
            printTree( t.left );
            System.out.println( t.element );
            printTree( t.right );
        }
    }

    /**
     * Method to compute height of a subtree.
     * @param t the node that roots the subtree.
     */
    int height( BSTNode<T> t )
    {
        if( t == null )
			return -1;
		else
			return 1 + Math.max( height( t.left ), height( t.right ) );	
        //  will result in height 0, if t is a leaf
    }

}
