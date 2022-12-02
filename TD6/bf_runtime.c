#include <stdio.h>
#include <stdint.h>

void bf_print(int64_t x)
{
  printf("%lld\n", x);
}

void bf_read(char* line)
{
    size_t len = 0;
    getline(&line, &len, stdin); 
}
