package a1posted;

import java.math.BigInteger;

public class Tester {
	
	public static void main(String[] args) throws Exception {
		
     /*  For the sake of readability, we define number coefficients for 
	     this Tester file to be in the usual human readable order:
		 { a[N-1],  a[N-2],  ...,  a[1],  a[0] }
		 where the coefficients a[ ]  are assumed to be written in 
		 base 10.   For example,  if you are using base 16,  then 
		 the following is possible { 12,  5, 6, 15, 13, 0}.  You
		 should not try to use other symbols for coefficients greater
		 than 10,  e.g.  {C, 5, 6, F, D, 0}  is NOT allowed.		  
		
		 The NaturalNumber constructor  will reverse the order of the 
		 coefficients when making the list,  so that the coefficient 
		 the methods in the NaturalNumber class corresponds to the 
		 order given in the PDF specification.
	  */
				
		int[] first  =  {5, 7, 3, 8};  // Base 10 coefficient representation for the integer number 9375
		int[] second =  {1, 8};        // Base 10 coefficient representation for the integer number 81
		
		//  You can test the correctness of your NaturalNumber implementation 
		//  by using Java's BigInteger class.  
		
		String firstAsString = new String();
		for(int i=0; i< first.length; i++)		{   
		    firstAsString += Character.toString( (char) (first[i] + '0' ));
		}
		String secondAsString = new String();
		for(int i=0; i< second.length; i++)		{   
		    secondAsString += Character.toString( (char) (second[i] + '0' ));
		}		
		BigInteger firstBigInteger  = new BigInteger(firstAsString);  
		BigInteger secondBigInteger  = new BigInteger(secondAsString);  
		
		int base     = 10;   // often called "radix" 
		
		NaturalNumber  firstNum  = new NaturalNumber(base,first);
		NaturalNumber  secondNum = new NaturalNumber(base,second);		
		
		System.out.println("first number:  a = " + firstAsString);
		System.out.println("second number: b = " + secondAsString);
		
		System.out.println("TEST FOR ADDITION (a+b) ");
		System.out.println("Correct answer   :  " + reFormat(firstBigInteger.add(secondBigInteger)));
		System.out.println("Your answer (a+b):  " + firstNum.add( secondNum ).toString() );
		System.out.println("Your answer (b+a):  " + secondNum.add( firstNum ).toString() );
		
		System.out.println("TEST FOR MULTIPLICATION (a*b) ");
		System.out.println("Correct answer    : " + reFormat(firstBigInteger.multiply(secondBigInteger)));
		System.out.println("Your answer (a*b) : " + firstNum.multiply( secondNum ).toString() );
		System.out.println("Your answer (b*a) : " + secondNum.multiply( firstNum ).toString() );
		
		System.out.println("TEST FOR SUBTRACTION (a-b, where a > b)  ");
		System.out.println("Correct answer    : " + reFormat(firstBigInteger.subtract(secondBigInteger)));
		System.out.println("Your answer       : " + firstNum.subtract( secondNum ).toString() );

		System.out.println("TEST FOR DIVISION (a/b) ");		
		System.out.println("Correct answer    : " + reFormat(firstBigInteger.divide(secondBigInteger)));
		System.out.println("Your answer       : " + firstNum.divide(secondNum).toString());
	}
	

	/*
	 *   This method takes a BigInteger and returns a string which we
	 *   can use to compare with what NaturalNumber.toString() produces. 
	 */

	public static String reFormat(BigInteger bigInt){
		String bigIntStr = bigInt.toString();
		String str = new String("[");		
		for (int i = 0; i < bigIntStr.length()-1; i++){
			str += bigIntStr.substring(i, i+1) + ", ";
		}
		str += bigIntStr.substring(bigIntStr.length()-1,bigIntStr.length())  + "]";
		return str;
	}
}
