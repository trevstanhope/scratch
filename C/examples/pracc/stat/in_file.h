/********************************************************
 * input_file -- data from the input file		*
 *							*
 * The current two characters are store in 		*
 *	cur_char and next_char				*
 * Lines are buffered so they can be output to 		*
 * the screen after a line is assembled.		*
 *							*
 * Functions:						*
 *	in_open -- opens the input file.		*
 *	in_close -- close the input file		*
 *	read_char   -- Read the next character.		*
 *	in_char_char -- return the current character	*
 *	in_next_char -- return the next character	*
 *	in_flush -- Send line to the screen.		*
 ********************************************************/

/********************************************************
 * in_open -- open the input file			*
 *							*
 * Parameters						*
 *	name -- name of disk file to use for input	*
 *							*
 * Returns						*
 *	0 -- Open succeeded.				*
 *	non-zero -- Open failed.			*
 ********************************************************/
extern int in_open(const char name[]);

/********************************************************
 * in_close -- close the input file.			*
 ********************************************************/
extern void in_close(void);

/********************************************************
 * in_read_char -- read the next character from the 	*
 *	input file					*
 ********************************************************/
extern void in_read_char(void);

/********************************************************
 * in_cur_char -- Get the current input character	*
 *							*
 * Returns						*
 *	current character.				*
 ********************************************************/
extern int in_cur_char(void);

/********************************************************
 * in_next_char -- Peek ahead one character		*
 *							*
 * Returns						*
 *	next character.					*
 ********************************************************/
extern int in_next_char(void);

/********************************************************
 * in_flush -- flush the buffered input line to the	*
 *		screen.					*
 ********************************************************/
extern void in_flush(void);
