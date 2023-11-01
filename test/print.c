#include "main.h"

void our_print(const char *our_char)
{
	write(STDOUT_FILENO, our_char, strlen(our_char));
}
