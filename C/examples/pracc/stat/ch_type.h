/********************************************************
 * char_type -- Character type module			*
 ********************************************************/
enum CHAR_TYPE {
    C_EOF,	/* End of file character */
    C_WHITE,	/* Whitespace or control character */
    C_NEWLINE,	/* A newline character */
    C_ALPHA,	/* A Letter (includes _) */
    C_DIGIT,	/* A Number */
    C_OPERATOR,	/* Random operator */
    C_SLASH,	/* The character '/' */
    C_L_PAREN,	/* The character '(' */
    C_R_PAREN,	/* The character ')' */
    C_L_CURLY,	/* The character '{' */
    C_R_CURLY,	/* The character '}' */
    C_SINGLE,	/* The character '\'' */
    C_DOUBLE,	/* The character '"' */
    /* End of simple types, more complex, derrived types follow */
    C_HEX_DIGIT,/* Hexidecimal digit */
    C_ALPHA_NUMERIC/* Alpha numeric */
};

/******************************************************** 
 * is_char_type -- Determine if a character belongs to  *
 * 		a given character type.			*
 *							*
 * Parameters						*
 *	ch -- Character to check			*
 *	kind -- type to check it for			*
 *							*
 * Returns:						*
 *	0 -- character is not of the specified kind	*
 *	1 -- character is of the specified kind.	*
 ********************************************************/
extern int is_char_type(int ch, enum CHAR_TYPE kind);

/********************************************************
 * get_char_type -- Given a character, return it's type.*
 *							*
 * Note: We return the simple types.  Compoisite types	*
 * such as C_HEX_DIGIT and C_ALPHA_NUMERIC are not	*
 * returned.						*
 *							*
 * Parameters:						*
 *	ch -- character who's type we want.		*
 *							*
 * Returns						*
 *	character type.					*
 ********************************************************/
extern enum CHAR_TYPE get_char_type(int ch);
