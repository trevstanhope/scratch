package singlyLinkedList;

/*
 *   Class has package visibility only.   Clients will use DLinkedList class.
 */

class SNode<E> {

	private 	E 	  		element;		
	private		SNode<E> 	next;		

	SNode(){
		next = null; 
	}
	
	SNode(E element){
		this.element = element; 
		next = null;
	}
	
	/*  all methods have package visibility only.  
	 *  Clients of the SLinkedList class should not have access to these methods.
	 */	
	
	void setNext(SNode<E> next) {   
		this.next = next;
	}

	SNode<E> getNext() {
		return next;
	}

	void setElement(E  element) {	
		this.element = element;
	}

	E 	getElement() {	    
		return this.element;
	}
}