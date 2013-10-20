// AddArrays.java
// Adds two arrays of integers

// Imports
import java.util.*;

public class AddArrays {
    public static void main (String[] args) {
	Scanner user_input = new Scanner(System.in);
	String keyboard_input;

	// create array a[]
	System.out.println("Input first integer:");
	keyboard_input = user_input.next();
	int a_length = keyboard_input.length();
	int[] a_array = new int[a_length];
	char[] a_char = keyboard_input.toCharArray();
	for (int i=0; i < a_length; i++) {
	    a_array[i] = Character.getNumericValue(a_char[i]);
	}

	// create array b[]
	System.out.println("Input first integer:");
	keyboard_input = user_input.next();
	int b_length = keyboard_input.length();
	int[] b_array = new int[b_length];
	char[] b_char = keyboard_input.toCharArray();
	for (int j=0; j < b_length; j++) {
	    b_array[j] = Character.getNumericValue(b_char[j]);
	}

	// find N, and make arrays the same dimension
	

	// find the sum of a and b
	int[] result = new int[N];
	int carry = 0;
	for (int k=0; k < (N-1); k++) {
	    result[k] =  % 10;
	    carry =   / 10;
	}
	result[N] = carry;      				     
    }
}