#include <stdio.h>
#include <time.h>
#include "TM1637.h"
  
#define clk 4 //pins definitions for TM1637 and can be changed to other ports       
#define dio 5
// 4 = GPIO.4,  wiringPi_4, pyhsics pin=16
// 5 = GPIO.5,  wiringPi_6, pyhsics pin=18

int setup()
{
  
  if(wiringPiSetup()==-1)
  {
     printf("setup wiringPi failed ! n");
     return 1;
  }
  
  pinMode(clk,INPUT);
  pinMode(dio,INPUT);
  delay(200); 
  
  TM1637_init(clk,dio);
  TM1637_set(BRIGHTEST,0x40,0xc0);//BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7;
  
  fprintf(stdout,"Digital Tube test code!n");
  fprintf(stdout,"Using DATA = GPIO5, CLK = GPIO4.n");   
  
}
  
int main()
{
  
  unsigned char i = 0;
  unsigned char count = 0;
  
  time_t rawtime;
  struct tm *tm;
  int8_t PointONOFF=0;

  delay(150);
  setup();

  while(1)
  {

    time(&rawtime);
    tm=localtime(&rawtime);
	if (PointONOFF==0) PointONOFF=1; else PointONOFF=0;
	TM1637_point(PointONOFF);
    TM1637_display(0,tm->tm_hour/10);
    TM1637_display(1,tm->tm_hour%10);
    TM1637_display(2,tm->tm_min/10);
    TM1637_display(3,tm->tm_min%10);
	delay(500);
  }
}
