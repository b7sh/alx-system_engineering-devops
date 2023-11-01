#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
#include <stdlib.h>
int main()
{
	int arr[5];
	srand(time(NULL));
	int i;
	for (i = 0; i < 5; i++)
	{
		arr[i] = rand() % 10;
	}
	int fd = open("sum", O_WRONLY);
	if (fd == -1)
	{
		return 1;
	}
	if(write(fd, arr, sizeof(int) *5) == -1)
	{
		return 2;
	}
	close(fd);
	return 0;
}
