#include <stdio.h>
#include <stdint.h>

void bf_print(int64_t x)
{
  // char c = x;
  // printf("%c", c); 

  printf("%d\n", x); 
  /*There is currently an error with the printing, because of the input format (int64_t) we can only either print the numeral or the corresponding ASCII char (TO FIX)*/
}

/*There is currently an error with the reading, the first time we acess the memory cell set by the reading, it prints a random address but then keeps the correct value*/
int8_t bf_read()
{
    int8_t res; 
    char buf[3]; 
    int maxLength = 4; 
    fgets(buf, maxLength, stdin);
    printf("from runtime.c"); 
    printf(buf);
    printf("\n");  
    printf("value of atoi func : %d\n", atoi(buf));
    res = atoi(buf);
    return res; 
}