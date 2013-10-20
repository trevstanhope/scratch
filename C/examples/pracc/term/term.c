/*-*/
/********************************************************
 * Name:						*
 *	term -- compute the value of three terms	*
 *							*
 * Purpose						*
 *	demonstrate the use of variables.		*
 *							*
 * Notes:						*
 *	Demonstration program only, does nothing 	*
 *	very useful.					*
 ********************************************************/
/*+*/
int term;       /* term used in two expressions */
int term_2;     /* twice term */
int term_3;     /* three times term */
int main()
{
    term = 3 * 5;
    term_2 = 2 * term;
    term_3 = 3 * term;
    return (0);
}
