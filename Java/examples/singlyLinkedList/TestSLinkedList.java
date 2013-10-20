package singlyLinkedList;

//import java.util.LinkedList;

public class TestSLinkedList {

	public	static	void   main(String[] args){	 
		
		SLinkedList<String> list = new SLinkedList<String>();
			
	//	LinkedList<String> list = new LinkedList<String>();
	//	list.addFirst(null);
		

		list.addLast("a");
		list.addLast("b");
		list.addLast("c");
		list.addLast("d");
		
		//  use Java's enhanced for loop  (to be explained later in course)
		
		for (String l : list){
			System.out.println(l);
		}
			
//		System.out.println(list.toString());
		

		list.show();
/*		
		System.out.println(list.getIndexOf("a"));
		System.out.println(list.getIndexOf("b"));
		System.out.println(list.getIndexOf("c"));
		System.out.println(list.getIndexOf("d"));		
		System.out.println(list.getIndexOf("f"));
*/
/*
		list.removeLast();
		list.show();
		list.removeLast();
		list.show();/

		list.remove("a");
		list.show();
		list.remove("c");
		list.show();
		list.remove("d");
		list.show();
		list.remove("a");
		list.show();
		list.remove("b");
	/*	System.out.println("first is " + list.getFirst());
		System.out.println("last  is " + list.getLast());
		
		list.addLast("a");
		list.show();
		list.reverse();*/
		
	//	list.show();
		list.reverseRecursive();
		list.show();
		
	/*	
		list.addLast("b");
		list.addLast("c");
		list.addLast("d");
		list.show();

		list.reverse();
		list.show();
		System.out.println("first is " + list.getFirst());
		System.out.println("last  is " + list.getLast());

		list.reverseRecursive();
		list.show();
*/
/*
		SLLIterator<String> iter1 = list.iterator();
		SLLIterator<String> iter2 = list.iterator();	
		iter1.next();
		
		while (iter1.hasNext() && iter2.hasNext()){
			System.out.println( iter1.next() + " " + iter2.next());
		}
*/	

	}
}
