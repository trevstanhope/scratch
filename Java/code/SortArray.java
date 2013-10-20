// SortArray
// Sort an integer array

import java.util.*;

public class SortArray {
    public static void main( String[] args) {
	int a[] = {200, 200, 100, 400, 800, 600, 700, 500, 900, 1000}; // unordered array
	int l = 10; // length of the array
	int tmp; // a temporary integer
	int j; // 

	for (int i=1; i < (l-1); i++) { // iterate i from 1 to l-1
	    tmp = a[i];
	    j = i;
	    // for the while, you MUST include j > 0 in case j = 0
	    while ((j > 0) && (tmp < a[j-1])) { // && is the AND conditional
		a[j] = a[j-1];
		j = j-1;
	    }
	    a[j] = tmp;
	}
	System.out.println(Arrays.toString(a)); // print result
    }
}