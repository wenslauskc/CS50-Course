#include <cs50.h>
#include <stdio.h>

int main(void)
{
   // Prompt user to agree
   get_string("Do you agree? "); 

   // Check whether user agreed
   if (c == 'y' || c == 'Y')   
   {
        printf("Agreed.\n");
   }
   else if (c == 'n' || c == 'N')
   {
        printf("Not agreed.\n");
   }
}