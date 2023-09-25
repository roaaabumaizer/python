// Q1
#include <stdio.h>

int main() {

    printf("Hello, World!");
    return 0;
}


// Q2
#include <stdio.h>

int main() {

int Num1, Num2;

  printf("Type a first number and press enter: \n"); 
  scanf("%i", &Num1);
  printf("Type a second number and press enter: \n");
  scanf("%i", &Num2);
  int sum = Num1+Num2;

 printf("The sum of the two numbers:\n%i\n", sum);
 return 0;
}
// Q3
#include <stdio.h>

int main(){
int MyNum;
printf("Enter a Random Number: ");
scanf("%i", &MyNum);

if (MyNum %2 == 0) {
printf("This is an Even Number");
}
else {
printf("This is an Odd Number");
}
return 0;

}
// Q4

#include <stdio.h>

int main(){
int Num1, Num2;

  printf("Type a first number and press enter: \n"); 
  scanf("%i", &Num1);
  printf("Type a second number and press enter: \n");
  scanf("%i", &Num2);
  int sum = Num1*Num2;

 printf("The product of the two numbers:\n%i\n", sum);
 return 0;
}

// Q5

#include <stdio.h>

int main() {

char Name;
char MonthOfBirth;
int DOB, PhoneNumber;

printf("Name\t: \t");
scanf("%s", &Name);

printf("Please ENter Your Date Of birth in the following order(Month(ex: april), day(ex: 6), year(ex: 2005)): \n");
printf("DOB\t: \t");

scanf("%s %i", MonthOfBirth, DOB);

printf("Mobile\t: \t");
scanf("%i", PhoneNumber);

return 0;

}

//Q6

#include <stdio.h>

int main() {
    printf("C version: %ld\n", __STDC_VERSION__);
    return 0;
}

//Q7

#include <stdio.h>

int main() {

char x = 'x', m = 'm', l = 'l';

printf("the reverse of %c %c %c is %c %c %c", x, m, l, l, m, x );

return 0;


}

//Q8

#include <stdio.h>

int main() {

int width = 5;
int height = 7;

int area = width*height;

int perimeter = 2* width + 2*height;

printf("The area of the rectangle equals = %i sqaure inches\n", area);
printf("The perimeter of the rectangle equals = %i inches", perimeter);

return 0;
}

//Q9

#include <stdio.h>

int main() {
    
    const double pi = 3.14159265359; 
    int radius  = 6;
    int perimeter = 2 * pi * radius;
    int area = pi * pow(radius, 2.00);
    
    printf("The area of the circle equals = %i sqaure inches \n", area);
    printf("The perimeter of the circle equals = %i inches", perimeter);
    
    return 0;
}

//Q10

#include <stdio.h>

int main() {

int Number;
printf("Enter a random number to convert to years, months, and weeks: ");
scanf("%i", &Number);

int years = Number/ 365;
int months = (Number % 365)/ 30;
int weeks = (Number % 365)/ 7 ;

printf("This equals to %i years, %i months, %i weeks", years, months, weeks);
return 0;
}

//Q11

#include <stdio.h>

int main() {



}













