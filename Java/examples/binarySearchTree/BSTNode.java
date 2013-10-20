class BSTNode<T>
{
    T           element;     	// The data in the node
    BSTNode<T>  left;   		// left child
    BSTNode<T>  right;  		// right child
	
	// Constructors
    
    BSTNode( T theElement )
    {
        this( theElement, null, null );
    }

    BSTNode( T theElement, BSTNode<T> lt, BSTNode<T> rt )
    {
        element  = theElement;
        left     = lt;
        right    = rt;
    }

} 
