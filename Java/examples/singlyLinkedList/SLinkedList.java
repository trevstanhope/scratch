package singlyLinkedList;
import java.lang.Iterable;

/*
 *   COMP 250 students:
 *   This example of a singly linked list class is incomplete.   There are many 
 *   interesting methods that have not been implemented.  e.g. See the Java LinkedList<E>
 *   class which defines other methods.   If you want to make sure you understand
 *   how singly linked lists work, then I suggest you try to implement and test 
 *   some of those other methods.
 *   - Mike Langer
 */

public class SLinkedList<E> implements Iterable<E> {

//  Ignore "implements Iterable" for now.  We will return to this 
//	later in the course when we discuss "Java interfaces"

/* 
 *  Fields
 */
	
	private		SNode<E> head;			 
	private		SNode<E> tail;		
	private		int 	 size; 	

	/*
	 * Constructor
	 */
	SLinkedList(){
    	head  = null;
	    tail  = null;
	    size  = 0;
	}
	
	/**
	 * Instance methods.
	 */
	
	SNode<E>  getHead(){
		return this.head;			 
	}
	
	/**
	 * @return element (an object of type E) stored at first node of list
	 * Note it returns the element, not the node.
	 */
	public E  getFirst(){
		if (head != null)
			return head.getElement();	
		else
			return null;
	}

	/**
	 * @return element (an object of type E) stored at last node of list
	 * Note it returns the element, not the node.
	 */

	public E  getLast(){
		if (tail != null)
			return tail.getElement();
		else
			return null;
	}
		
	/**
	 * create a new node and add to front of list 
	 * Element is passed to the method (not node passed to method)
	 */
	
	public void addFirst(E element){	
		SNode<E> newNode = new SNode<E>(element); 
		size++;
		if (head == null){
			head = newNode;
			tail = head; 
		}
		else{
			newNode.setNext(head);
			head = newNode;
		}
	}

	/**
	 * create a new node and add to end of list 
	 * Element is passed to the method (not node passed to method)
	 */
	
	void addLast(E element){
		SNode<E> newNode = new SNode<E>(element); 
		size++;
		if (head == null){
			head = newNode;
			tail = newNode;
		}
		else{
			tail.setNext(newNode);
			tail = newNode;
		}
	}
	
	/**
	 * @return first element in list
	 */
	

	public	E removeFirst(){  
		if (head != null){
			size--;
			SNode<E> tmp = head;
			head = head.getNext();
			return tmp.getElement();
		}
		else return null;
	}

	/**
	 * @return  last element 
	 * There is no particular reason why I made this method return it (as opposed to just removing it)
	 * If list is empty, then it returns nothing.
	 */
	
	public E removeLast(){ 
		SNode<E> cur = head;
		if (cur == null){
			System.out.println("list is empty so cannot remove tail.. returning null");
			return null;   
		}
		else{
			size--;
			if (cur == tail){  	//  only one node in list
				head = null;  
				tail = null;
				return cur.getElement(); 
			}
			else{
				while (cur.getNext() != tail){
					cur = cur.getNext();
				}
				tail = cur;
				SNode<E> tmp = cur.getNext();
				cur.setNext(null);
				return tmp.getElement();
			}
		}
	}
	
/**
 *   finds and removes the first occurence of an element from a list
 *   If element is not in the list, then do nothing.	
 */

	void remove( E element){		 
		SNode<E>  cur = head;

		/*
		 *  First deal with special cases that the list is empty, or the element we are 
		 *  looking for is the first element in the list.
		 */
		if (head != null){
			if (head == tail){    // only one node in list
				if (head.getElement() == element){  	
					head = null;  
					tail = null;
					size = 0;
				}
			}
			else{
				if (head.getElement() == element){    // element is at head
					head = head.getNext();
					size--;
				}
				else {
					/*
					 *	There is more than one node in list and the element (if it is in the list)
					 *  is not at the front of the list.   In this case,  keep going until either
					 *  the next element is the one we are looking for, or we reach the end of the list.
					 */

					while ((cur != null) & (cur.getNext().getElement() != element)){
						cur = cur.getNext();
					}
					//  either we reached the end (cur == null)  or  cur.next contains the element  
					if (cur != null){   //  i.e.  cur.next contains the element
						size--;
						cur.setNext( cur.getNext().getNext() );   // jump over the next guy
						//  if the guy we just deleted was the tail
						if (cur.getNext() == null){      //  If you forget this, then tail will still
							tail = cur;                //  point to the node we just removed.
						} 
					}
				}
			}
		}
	}
	
/**
 *   puts the list nodes in opposite order
 *   The links must all go in the opposite direction, and head and tail must be swapped.
 *   To do it, we walk from head to tail, maintaining a partition of the nodes into two
 *   lists:  the nodes up to the current node, and the nodes beyond the current node.    
 */
	
	public	void reverse(){
		SNode<E> headLeft, headRight, tmp;
		if (head != null){
			headLeft = null;
			headRight = head;
			while (headRight != null){
				tmp = headRight.getNext();
				headRight.setNext(headLeft);
				headLeft = headRight;
				headRight = tmp;
			}
			tail = head;
			head = headLeft;
		}
	}

	public	void reverseRecursive(){
		if (head != null){
			reverse1(head);
			head.setNext(null);
			SNode<E> tmp = tail;
			tail = head;
			head = tmp;
		}
	}
	
	/**
	 *    helper method used by reverseRecursive()
	 */
	
	private SNode<E> reverse1(SNode<E> head){  //  only gets called when head != null
		SNode<E> tmp = head;
		head = head.getNext();
		if (head != null){
			reverse1(head);
			head.setNext(tmp);
		}
		return tmp;
	}
	
	public int getIndexOf(E  e){
		SNode<E>  cur = head;
		int i = 0;     //  add code here
		
		while ((cur.getElement() != e) && (cur.getNext() != null)){
			cur = cur.getNext();
			i++;
		}
		
		if (cur.getElement() == e)
			return i;
		else 
			return -1;
	}
	
	/**
	 * Show all elements in list.
	 */
	public void show(){			 
		SNode<E> cur = head;
		while (cur != null){
			System.out.print("  " + cur.getElement().toString());
			cur = cur.getNext();
		}
		System.out.println("  (size is " + size + " )");
	}

	//  ignore this guy for now !
	
	public SLLIterator<E> iterator() {
		SLLIterator<E> iter = new SLLIterator<E>(this);
		return iter;
	}
}
