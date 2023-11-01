#include "main.h"

void read_line(char *command, size_t size)
{
	if (fgets(command, size, stdin) == NULL)
	{
		our_print("\n");
		exit(EXIT_SUCCESS);
	}
	else
	{
		our_print("Error while reading the input\n");
		exit(EXIT_FAILURE);
	}
	command[strcspn(command, "\n")] = '\0';
}
