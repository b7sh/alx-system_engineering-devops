#include "main.h"

void execute_command(const char *command)
{
	pid_t child_pid = fork();

	if (child_pid == -1)
	{
		our_print("Error forking");
		exit(EXIT_FAILURE);
	}
	else if (child_pid == 0)
	{
		char *args[128];
		int argc = 0, count = 0;
		char *token;

		token = strtok((char *)command, " ");
		while (token)
		{
			args[count++] = token;
			token = strtok(NULL, " ");
		}
		args[count] = NULL;
		execvp(args[0], args);
		our_print("Error\n");
		exit(EXIT_FAILURE);
	}
	else
		wait(NULL);
}
