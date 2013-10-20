//make your NaturalNumber.coefficient field public for the purposes of this Tester. Happy Testing!

package a1posted;

import java.math.BigInteger;

public class TheTester {
 
 public static void main(String[] args) throws Exception 
 { 
   int testCount = 1000;
   int base = (int)(Math.random()*34)+2;
   int length = (int)(Math.random()*10)+1;
   int[] a = randomInts(base-1,length);
   int[] b = randomInts(base-1,length);
   NaturalNumber x = new NaturalNumber(base);
   NaturalNumber y = new NaturalNumber(base);
   BigInteger testX = new BigInteger("0");
   BigInteger testY = new BigInteger("0");
   String result = "";
   String trueResult = "";
   //addition test
   for(int i = 0;i<testCount;i++)
   {
     base = (int)(Math.random()*34)+2; //we generate two random numbers of random bases, with random lengths
     length = (int)(Math.random()*10)+1;
     a = randomInts(base-1,length);
     b = randomInts(base-1,length);
     randomInts(base-1,length);
     x = new NaturalNumber(base,a);
     y = new NaturalNumber(base,b);
     testX = new BigInteger(toBigIntString(x),base);
     testY = new BigInteger(toBigIntString(y),base);
     result = convertToDec(x.add(y));
     trueResult = (testX.add(testY)).toString();
     if(!result.equals(trueResult))
       throw new Exception();
   }
   System.out.println("Addition Test: success");
   //multiplication test
   for(int i = 0;i<testCount;i++)
   {
     base = (int)(Math.random()*34)+2; //we generate two random numbers of random bases, with random lengths
     length = (int)(Math.random()*5)+1;
     a = randomInts(base-1,length);
     b = randomInts(base-1,length);
     randomInts(base-1,length);
     x = new NaturalNumber(base,a);
     y = new NaturalNumber(base,b);
     testX = new BigInteger(toBigIntString(x),base);
     testY = new BigInteger(toBigIntString(y),base);
     result = convertToDec(x.multiply(y));
     trueResult = (testX.multiply(testY)).toString();
     if(!result.equals(trueResult))
       throw new Exception();
   }
   System.out.println("Multiplication Test: success");
   
   //division test
   /*
   for(int i = 0;i<testCount;i++)
   {
     base = (int)(Math.random()*34)+2; //we generate two random numbers of random bases, with random lengths
     length = (int)(Math.random()*5)+3;
     a = randomInts(base-1,length);
     b = randomInts(base-1,length-2);
     randomInts(base-1,length);
     x = new NaturalNumber(base,a);
     y = new NaturalNumber(base,b).add(new NaturalNumber(base,1));//we don't want y to be 0 because division by 0 is impossible
     testX = new BigInteger(toBigIntString(x),base);
     testY = new BigInteger(toBigIntString(y),base);
     result = convertToDec(x.divide(y));
     trueResult = (testX.divide(testY)).toString();
     if(!result.equals(trueResult))
       throw new Exception();
   }
   */
   
   System.out.println("Division Test: not ready");
   
   
   //subtraction test
   for(int i = 0;i<testCount;i++)
   {
     base = (int)(Math.random()*34)+2; //we generate two random numbers of random bases, with random lengths
     length = (int)(Math.random()*5)+1;
     a = randomInts(base-1,length);
     b = randomInts(base-1,length);
     randomInts(base-1,length);
     y = new NaturalNumber(base,b);
     x = new NaturalNumber(base,a).add(y); //here we are setting x to be equal to y + a random number to be sure that x>y (the result of x-y should return that random number)
     testX = new BigInteger(toBigIntString(x),base);
     testY = new BigInteger(toBigIntString(y),base);
     result = convertToDec(x.subtract(y));
     trueResult = (testX.subtract(testY)).toString();
     System.out.println(result);
     if(!result.equals(trueResult))
       throw new Exception();
   }
   System.out.println("Subtraction: success");
 }
 
 /*
  *   This method takes a BigInteger and returns a string which we
  *   can use to compare with what NaturalNumber.toString() produces. 
  */

 public static int[] randomInts(int magnitude, int size)//generates an array of size size random integers between 0 and magnitude
 {
   int[] output = new int[size];
   output[0] = (int)(Math.random()*(magnitude-1))+1;//first integer shouldn't be 0 as it will generate a number in improper format
   for(int i=1;i<size;i++)
     output[i] = (int)(Math.random()*magnitude);
   return output;
 }
 
 public static String toCleanString(int[] input)//returns a string representation of the number represented in the array
 {
   String output = "";
   for(int e : input)
     output += e;
   return output;
 }
 
 public static String toBigIntString(NaturalNumber input)//returns a string representation of the NaturalNumber that is compatible with BigInteger in ALL BASES
 {
   String output = "";
   for(int e : input.coefficients)
   {
     if(e>=0 && e<=9)
       output += e;
     else //knowing that A is equivalent to 10 in other bases, and that its Dec char code is 65, we deduce 
       output += (char)(55+e)+"";
   }
   return new StringBuilder(output).reverse().toString();
 }
 
 public static String toString(int[] input)
 {
   String output = "";
   for(int e : input)
     output += e;
   return output;
 }
 
 public static String convertToDec(NaturalNumber input)
 {
   long output = 0;
   for(int i = input.coefficients.size()-1;i>=0;i--)
     output += input.coefficients.get(i)*(long)(Math.pow(input.base,i));
   return output+"";
 }
 
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
