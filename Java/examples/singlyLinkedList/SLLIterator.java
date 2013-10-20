package singlyLinkedList;

import java.util.Iterator;

//   This will only make sense later in the course.  

public class  SLLIterator<T> implements Iterator<T>{
	private SNode<T>    cur;
	
	SLLIterator(SLinkedList<T> list){
		cur = list.getHead();
	}

	public boolean hasNext() {
		return (cur != null);
	}

	public T next() {
		SNode<T> tmp = cur;
		cur = cur.getNext();
		return tmp.getElement();
	}

	public void remove() {
		// Not implemented 		
	}
}