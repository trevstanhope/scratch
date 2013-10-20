import java.util.*;

/*  @author:  Michael Langer
 *  
 *  The iterator for a BST uses an inorder traversal of the nodes in the list.
 *  It makes a private LinkedList of BSTNodes and the next() method returns
 *  the element of the next node in the list.   The list follows the ordering
 *  of an inorder traversal, which is typically suitable for a binary search tree. 
 *
 *   Only has package visiblity.  Any clients of the BinarySearchTree that are
 *	 outside the package do not need to know how this iterator is implemented.
 */

class BSTIterator<T>  implements Iterator<T>  {

	private  LinkedList<T>        queue;
	
	//  Constructor
	
	BSTIterator(BSTNode<T> root){
		queue = new LinkedList<T>();
		inOrder(root); 
	}

	private void inOrder( BSTNode<T> node){
		if (node != null){
			inOrder(node.left);
			queue.addLast(node.element);
			inOrder(node.right);
		}
	}

	public boolean hasNext() {
		if (queue.isEmpty())
			return false;
		else
			return true;
	}

	public T next() {
		return queue.removeFirst();
	}

	public void remove() {
		// not implemented	
	}
	
	
}
