#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <string.h>
#include <sys/types.h>
#include <errno.h>
#include <sys/stat.h>
#include <limits.h>

void our_print(const char *our_char);
void execute_command(const char *command);
void print_prompt(void);
void read_line(char *command, size_t size);

#endif
