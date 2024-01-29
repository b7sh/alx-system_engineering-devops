#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 *
 * Return: always 0
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - entry point
 *
 * Return: success
*/

int main(void)
{
	pid_t pid;
	char i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
