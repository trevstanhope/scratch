import java.util.Random;

//import java.util.*;

public class TestBST {

	/**
	 * @param args
	 */
	
    // Test program
    public static void main( String [ ] args )
    {
        BinarySearchTree<Integer> t = new BinarySearchTree<Integer>( );
        
        
        //  This test program adds N randomly chosen integers to a binary search
        //  tree.   For each successive power of 2,  it prints out the height of
        //  of the tree.  Notice that the height grows approximately like 2 log2(n).  
    
        
        Random  rand = new Random();
        final int N = 1000000;
        
        //  Ignore the possibility that we insert the same element twice. 
        //  This should happen only rarely in the code below.
        
        int  nextPowerOf2 = 32;  //  start printing heights at n = 32
		System.out.println("n    log2(n)  BSTheight");
        for (int i = 0; i < N; i++){
        	t.insert(rand.nextInt());
        	if (i == nextPowerOf2){
        		System.out.print(i + "       ");
        		//  Math.log  is log_e.  
        		//  log_e(x) = log_e(2) * log_2(x)
        		//  So,  log_2(x) = log_e(x) / log_e(2)  
        		System.out.format(Math.round(Math.log(i) / Math.log(2)) + "    ");
        		System.out.println(t.height(t.root));
        		nextPowerOf2 *=2;
        	}
        }
        
        
        /*
        
        final int NUMS = 200;
        final int GAP  =  37;

        System.out.println( "Checking... (no more output means success)" );

        for( int i = GAP; i != 0; i = ( i + GAP ) % NUMS )
            t.insert( i );

        //  remove all odd numbers
        for( int i = 1; i < NUMS; i+= 2 )
            t.remove( i );

//        t.printTree( );
  
        BSTIterator<Integer>	iter = t.iterator();
        while (iter.hasNext()){
        	System.out.println(iter.next());
        }
        
        System.out.println(" Min:  " + t.findMin());
        System.out.println(" Max:  " + t.findMax());

        //   tree should contain all even numbers from 2 to NUMS
        //   but none of the odd numbers
        
        for( int i = 2; i < NUMS; i+=2 )
             if( !t.contains( i ) )
                 System.out.println( "Find error1!" );

        for( int i = 1; i < NUMS; i+=2 )
        {
            if( t.contains( i ) )
                System.out.println( "Find error2!" );
        }
        
        */
    }
}
