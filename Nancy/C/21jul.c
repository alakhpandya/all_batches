// Restaurant Menu Program
#include<stdio.h>

int main()
{
    int choice1, choice2;
    printf("Welcome to Royal Restaurant!\n");
    printf("Which cuisine would you prefer?\n");
    printf("Press 1 for North Indian\n");
    printf("Press 2 for South Indian\n");
    printf("Press 3 for Mexican\n");
    printf("Press 4 for Chinese\n");
    printf("Press 5 for Italian\n");
    scanf("%d", &choice1);
    switch (choice1)
    {
        case 1:
        printf("Please choose your sabji:\n");
        printf("Press 1 for Paneer Sabjis\n");
        printf("Press 2 for Veg Sabjis\n");
        printf("Press 3 for Kofta Sabjis\n");
        printf("Press 4 for Spicy Sabjis\n");
        scanf("%d", &choice2);
        switch (choice2)
        {
            case 1:
            printf("Thanks for ordering North Indian dish- Paneer Sabji!");
            break;
            case 2:
            printf("Thanks for ordering North Indian dish- Veg Sabji!");
            break;
            case 3:
            printf("Thanks for ordering North Indian dish- Kofta Sabji!");
            break;
            case 4:
            printf("Thanks for ordering North Indian dish- Spicy Sabji!");
            break;
            default:
            printf("This item is not available! Please try again...");
            break;
        }
    }
}