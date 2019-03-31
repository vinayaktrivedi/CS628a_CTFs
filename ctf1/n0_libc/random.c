#include<stdio.h>
#include<time.h>
#include<stdlib.h>
int main(){
unsigned int timer = (int)time(0);
unsigned int random;
unsigned int var = timer*0x343fd;
var = var+0x269ec3;
var = var >> 16;
var = var & 0x7fff;

printf("%u ",var%256);
printf("%u",var>>8);

return 0;
}
