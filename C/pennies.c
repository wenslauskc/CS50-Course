#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    float number = get_float("Dollar amount: ");
    int pennies = round(amount * 100);
    printf("Pennies: %i\n", pennies);
}