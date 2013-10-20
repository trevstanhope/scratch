// GetInput.java
// Get string from keyboard
// Works
import java.util.Scanner;
public class GetInput {
    public static void main (String[] args) {
	Scanner user_input = new Scanner(System.in);
	String keyboard_input;
	keyboard_input = user_input.next();
	System.out.println(keyboard_input);
	}
}

