#include<stdio.h>

void main()
{
    float a,p,l,b; 
    printf("enter length and breadth of rectangle:-\n");
    scanf("%f%f",&l,&b);

    a=l*b;
    p= 2*(l+b);
    printf("area of the rectangle: %f\n",a);
    printf("perimeter of the rectangle:%f\n",p);
    
}
