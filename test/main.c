#include "main.h"

int main()
{
	char command[124];
	while (1)
	{
		print_prompt();
		read_line(command, sizeof(command));
		execute_command(command);
	}
	return 0;
}
