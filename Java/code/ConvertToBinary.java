// ConvertToBinary.java
// Convert decimal to binary

// Imports
import java.util.*;

// Class
public class ConvertToBinary {
    public static void main (String[] args) {
	// Instantiate
	Scanner user_input = new Scanner(System.in);
	String keyboard_input; // keyboard input string
	int m; // decimal number
	int[] b = new int[32]; // 32bit binary array

	System.out.println("Input first integer:");
	keyboard_input = user_input.next();
	m = Integer.parseInt(keyboard_input);
	for (int i=0; m > 0; i++) {
	    b[i] = m % 2;
	    m = m / 2;
	}
	for(int i = 0; i < b.length; i++){
	    System.out.println(b[b.length-i-1]);
	}
    }
}

