#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <fcntl.h>
#include <stdlib.h>

int main()
{
	int arr[5];
	int fd = open("sum", O_RDONLY);
	if (fd == -1)
	{
		return 1;
	}
	if (read(fd, arr, sizeof(int) * 5)== -1)
	{
		return 2;
	}
	close(fd);
	int sum = 0;
	int i;
	for (i = 0; i < 5; i++)
	{
		sum += arr[i];
	}
	printf("result is %d\n", sum);
	return 0;
}
