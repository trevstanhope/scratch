package a1posted;

/*
  STUDENTNAME: Trevor Stanhope
  STUDENTID: 260399515
*/

/*
  NOTES:
  1. The four methods assume that the two numbers are of the same base.
  2. I spoke with my classmate Martin Weiss about the methods longerNaturalNumber and shorterNaturalNumber.
  3. I unfortunately was not able to use Tester.java, but I did test important cases on paper.
  4. I was not aware what, 'use space proprotional to the number of coefficients' in the requirements for multiply() meant,  
  but I interpretted it to mean that a table summation was not necessary (i.e. using a 2d array).
  
 */

import java.util.LinkedList;

public class NaturalNumber  {
	
    int	base;       
    public LinkedList<Integer>  coefficients;

    /* CONSTRUCTORS */
	NaturalNumber(int base){
		this.base = base;
		coefficients = new LinkedList<Integer>();
	}

	NaturalNumber(int base, int i) throws Exception{
		this.base = base;
		coefficients = new LinkedList<Integer>();
		
		if ((i >= 0) && (i < base))
			coefficients.addFirst( new Integer(i) );
		else {
			System.out.println("constructor error: all coefficients should be non-negative and less than base");
			throw new Exception();
		}
	}

	NaturalNumber(int base, int[] intarray) throws Exception{
		this.base = base;
		coefficients = new LinkedList<Integer>();
		for (int i=0; i < intarray.length; i++){
			if ((i >= 0) && (intarray[i] < base))
				coefficients.addFirst( new Integer( intarray[i] ) );
			else{
				System.out.println("constructor error:  all coefficients should be non-negative and less than base");
				throw new Exception();
			}
		}
	}
	
    /* METHODS */
    public NaturalNumber add( NaturalNumber  second) {
				
		//  initialize the sum as an empty list of coefficients
		NaturalNumber sum = new NaturalNumber(this.base);
		NaturalNumber longer = longerNaturalNumber(this, second);
		NaturalNumber shorter = shorterNaturalNumber(this, second);
		/***************************************************************************/
		// variables
		int a; // the i-th coefficient of 'longer'
		int b; // the i-th coefficient of 'shorter'
		int tmp; // new coefficient
		int radix = longer.base; // the base
		int carry=0; // the carried value
		
	       	for(int i = 0; i < shorter.coefficients.size(); i++) {
		    a = longer.coefficients.get(i);
		    b = shorter.coefficients.get(i);
				tmp = (a + b + carry) % radix;
				carry = (a + b + carry) / radix;
				sum.coefficients.addLast(tmp);
   		}

		// append the additional coefficients from the larger number
		for (int j = shorter.coefficients.size(); j < longer.coefficients.size(); j++) {
			sum.coefficients.addLast((longer.coefficients.get(j) + carry) % radix);
			carry = ((longer.coefficients.get(j) + carry) / radix);
		}
		
		// add last coefficient if not zero
		if (carry != 0)	{
			sum.coefficients.addLast(carry);
		}
		/***************************************************************************/

		return sum;		
    }
	
    public NaturalNumber subtract(NaturalNumber smaller) throws Exception {

		//  initialize difference as an empty list of coefficients
		NaturalNumber  difference = new NaturalNumber(this.base);
		
		// clone 'this' into 'larger'
		NaturalNumber  larger = this.clone();

		// test if 'larger' is greater than 'smaller'
		if (this.compareTo(smaller) < 0){
			System.out.println("Error:  subtract a-b requires that a > b");
			throw new Exception();
		}

		/***************************************************************************/
		// declare integer variables
		int n = larger.coefficients.size(); // length of 'larger'
		int m = smaller.coefficients.size(); // length of 'smaller'
		int a; // the i-th coefficient of 'larger'
		int b; // the i-th coefficient of 'smaller'
		int radix = larger.base; // the base
		int carry = 0;
		int tmp; // new coefficient
		
		// main loop
		for (int i=0; i < m; i++) {
		    a = larger.coefficients.get(i);
		    b = smaller.coefficients.get(i);
		    if (a >= b) {
			tmp = a - b;
		    } else {
			tmp = radix + a - b;
			for(int j=i+1; j < n; j++) { // broken when a non-zero coefficient is reached
			    carry = larger.coefficients.get(j);
			    if (carry == 0) {
				larger.coefficients.set(j, (radix - 1)); // sets zeros if carrying to base - 1
			    } else {
				larger.coefficients.set(j, (carry - 1));
				break; // breaks the inner for-loop if a non-zero is reached
			    }
			}
		    }
		    difference.coefficients.addLast(tmp);
		}
		
		// bring down the remaining terms in 'larger'
		for (int k=m; k < n; k++) {
		    difference.coefficients.addLast(larger.coefficients.get(k));
		}
		
		// remove zeros
		while (difference.coefficients.getLast() == 0) {
		    difference.coefficients.removeLast();
		}
		/***************************************************************************/
		
		return difference;	
    }

    /* 
       you must write a method that uses space that is proportional to
       the number of coefficients.  This can be done by basically 
       changing the order of loops, as was sketched in class. 
    */

    public NaturalNumber multiply( NaturalNumber  second) throws Exception {
	
		//  initialize product as an empty list of coefficients
		NaturalNumber product	= new NaturalNumber(this.base);
		// clone 'this'
		NaturalNumber  first = this.clone();

		/***************************************************************************/
		// variables
		int n = first.coefficients.size(); // length of 'first'
		int m = second.coefficients.size(); // length of 'second'
		int a; // the i-th coefficient of 'first'
		int b; // the j-th coeffcieint of 'second'
		int radix = first.base; // base
		int tmp; // new coefficient
		int carry=0;

		// fill product with zeros
		for (int k=0; k <= m+n-2; k++) {
		    product.coefficients.add(0);
		}
		
		// for i,j in first,second, increment product(i,j) by a*b
		for(int i=0; i < n; i++) {
		    for(int j=0; j < m; j++) {
			a = first.coefficients.get(i);
			b = second.coefficients.get(j);
			tmp = (a * b + carry ) % radix;
			carry = (a * b + carry ) / radix;
			product.coefficients.set((i+j), product.coefficients.get(i+j) + tmp); // add 'tmp' to the previous value at index i,j
		    }
		}

		// remove zeros
		while (product.coefficients.getLast() == 0) {
		    product.coefficients.removeLast();
		}
		/***************************************************************************/
				
		return product;
	}
		
	public NaturalNumber divide( NaturalNumber  divisor ) throws Exception {
		
		//  initialize quotient as an empty list
		NaturalNumber  quotient = new NaturalNumber(this.base);

		// clone 'this' into 'dividend'
		NaturalNumber  dividend = this.clone();
		
		/***************************************************************************/
		// declare integer variables
		int n = dividend.coefficients.size(); // length of dividend
		int m = divisor.coefficients.size(); // length of divisor
		int a; // the i-th from last coefficient of the dividend
		int b; // the i-th from last coefficient of the divisor
		int radix = dividend.base; // base
		int lead = divisor.coefficients.getLast(); // leading term of divisor
		int remainder = 0; // remainder starts as zero
		int tmp = 0; // coefficient of quotient

		// main loop
		for(int i=0; n-m-i >= 0; i++) {
		    a = dividend.coefficients.get(n-i-1);
		    b = divisor.coefficients.get(m-i-1);
		    tmp = (a + radix*remainder - b*tmp) / lead; // always divide by the leading coefficient of the divisor
		    remainder = a - tmp * b; // the 
		    quotient.coefficients.addFirst(tmp); // since the loop works in reverse
		}
		
		// remove zeros
		while (quotient.coefficients.getLast() == 0) {
		    quotient.coefficients.removeLast();
		}
	        /***************************************************************************/

		return quotient;		
	}

    // HELPERS
    /*
      The methods should not alter the two numbers.  If a method require
      that one of the numbers be altered (e.g. borrowing in subtraction)
      then you need to clone the number and work with the cloned number 
      instead of the original. 
    */

    public NaturalNumber  clone() {

		//  For technical reasons we'll discuss later, this methods 
		//  has to be declared public (not private).
		//  This detail need not concern you now.

	NaturalNumber copy = new NaturalNumber(this.base);
	for (int i=0; i < this.coefficients.size(); i++){
	    copy.coefficients.addLast( new Integer( this.coefficients.get(i) ) );
	}
	return copy;
    }
	
    public NaturalNumber longerNaturalNumber(NaturalNumber a,NaturalNumber b) {
		if(a.coefficients.size() > b.coefficients.size())
		{
			return a;
		}
		return b;
	}
    public NaturalNumber shorterNaturalNumber(NaturalNumber a,NaturalNumber b) {
		if(a.coefficients.size() < b.coefficients.size()) {
			return a;
		}
		return b;
	}
    private int 	compareTo(NaturalNumber second){
		
		int diff = this.coefficients.size() - second.coefficients.size();
		if (diff < 0)
			return -1;
		else if (diff > 0)
			return 1;
		else { 
			boolean done = false;
			int i = this.coefficients.size() - 1;
			while (i >=0 && !done){
				diff = this.coefficients.get(i) - second.coefficients.get(i); 
				if (diff < 0){
					return -1;
				}
				else if (diff > 0)
					return 1;
				else{
					i--;
				}
			}
			return 0;
		}
	}

	/*  computes  a*base^n  where a is the number represented by 'this'
	 */
	
	private NaturalNumber multiplyByBaseToThePower(int n){
		for (int i=0; i< n; i++){
			this.coefficients.addFirst(new Integer(0));
		}
		return this;
	}

	//   This method is invoked by System.out.print.
	//   It returns the string with coefficients in the reverse order 
	//   which is the natural format for people to reading numbers,
	//   i.e..  [ a[N-1], ... a[2], a[1], a[0] ] as in the Tester class. 
	//   It does so simply by make a copy of the list with elements in 
	//   reversed order, and then printing the list using the LinkedList's
	//   toString() method.
	
	public String toString(){	
		LinkedList<Integer> reverseCoefficients = new LinkedList<Integer>();
		for (int i=0;  i < coefficients.size(); i++)
			reverseCoefficients.addFirst( coefficients.get(i));
		return reverseCoefficients.toString();		
	}

}

