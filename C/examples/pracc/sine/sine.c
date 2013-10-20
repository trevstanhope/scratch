/********************************************************
 * sine -- compute sine using very simple floating      *
 *      arithmetic.                                     *
 *                                                      *
 * Usage:                                               *
 *      sine <value>                                    *
 *                                                      *
 *      <value> is an angle in radians                  *
 *                                                      *
 * Format used in f.fffe+X                              *
 *                                                      *
 * f.fff is a 4 digit fraction                          *
 *      + is a sign (+ or -)                            *
 *      X is a single digit exponent                    *
 *                                                      *
 * sine(x) = x  - x**3 + x**5 - x**7                    *
 *               -----   ----   ---- . . . .            *
 *                 3!     5!     7!                     *
 *                                                      *
 * Warning: This program is intended to show some of    *
 *      problems with floating point.  It not intended  *
 *      to be used to produce exact values for the      *
 *      sin function.                                   *
 *                                                      *
 * Note: Even though we specify only one-digit for the  *
 *       exponent, two are used for some calculations.  *
 *       This is due to the fact that printf has no     *
 *       format for a single digit exponent.            *
 ********************************************************/
#include <stdlib.h>	
#include <math.h>
#include <stdio.h>

/********************************************************
 * float_2_ascii -- turn a floating-point string        *
 *      into ascii.                                     *
 *                                                      *
 * Parameters                                           *
 *      number -- number to turn into ascii             *
 *                                                      *
 * Returns                                              *
 *      Pointer to the string containing the number     *
 *                                                      *
 * Warning: Uses static storage, so later calls         *
 *              overwrite earlier entries               *
 ********************************************************/
static char *float_2_ascii(float number)
{
    static char result[10]; /*place to put the number */

    sprintf(result,"%8.3E", number);
    return (result);
}
/********************************************************
 * fix_float -- turn high precision numbers into        *
 *              low precision numbers to simulate a     *
 *              very dumb floating-point structure.     *
 *                                                      *
 * Parameters                                           *
 *      number -- number to take care of                *
 *                                                      *
 * Returns                                              *
 *      number accurate to 5 places only                *
 *                                                      *
 * Note: This works by changing a number into ascii and *
 *       back.  Very slow, but it works.                *
 ********************************************************/
float fix_float(float number)
{
    float   result; /* result of the conversion */
    char    ascii[10];      /* ascii version of number */

    sprintf(ascii,"%8.4e", number);
    sscanf(ascii, "%e", &result);
    return (result);
}
/********************************************************
 * factorial -- compute the factorial of a number.      *
 *                                                      *
 * Parameters                                           *
 *      number -- number to use for factorial           *
 *                                                      *
 * Returns                                              *
 *      factorial(number) or number!                    *
 *                                                      *
 * Note: Even though this is a floating-point routine,  *
 *       using numbers that are not whole numbers       *
 *       does not make sense.                           *
 ********************************************************/
float factorial(float number)
{
    if (number <= 1.0)
	return (number);
    else
	return (number *factorial(number - 1.0));
}

int main(int argc, char *argv[])
{
    float   total;  /* total of series so far */
    float   new_total;/* newer version of total */
    float   term_top;/* top part of term */
    float   term_bottom;/* bottom of current term */
    float   term;   /* current term */
    float   exp;    /* exponent of current term */
    float   sign;   /* +1 or -1 (changes on each term) */
    float   value;  /* value of the argument to sin */
    int     index;  /* index for counting terms */

    if (argc != 2) {
	fprintf(stderr,"Usage is:\n");
	fprintf(stderr,"  sine <value>\n");
	exit (8);
    }

    value = fix_float(atof(&argv[1][0]));

    total = 0.0;
    exp = 1.0;
    sign = 1.0;

    for (index = 0; /* take care of below */ ; ++index) {
	term_top = fix_float(pow(value, exp));
	term_bottom = fix_float(factorial(exp));
	term = fix_float(term_top / term_bottom);
	printf("x**%d     %s\n", (int)exp, 
			float_2_ascii(term_top));
	printf("%d!       %s\n", (int)exp, 
			float_2_ascii(term_bottom));
	printf("x**%d/%d! %s\n", (int)exp, (int)exp,
		float_2_ascii(term));
	printf("\n");
	new_total = fix_float(total + sign * term);
	if (new_total == total)
	    break;
	total = new_total;
	sign = -sign;
	exp = exp + 2.0;
	printf("  total   %s\n", float_2_ascii(total));
	printf("\n");
    }
    printf("%d term computed\n", index+1);
    printf("sin(%s)=\n", float_2_ascii(value));
    printf("  %s\n", float_2_ascii(total));
    printf("Actual sin(%G)=%G\n",
	    atof(&argv[1][0]), sin(atof(&argv[1][0])));
    return (0);
}
