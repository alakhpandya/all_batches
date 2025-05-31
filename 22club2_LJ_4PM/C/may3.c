/*
#include<stdio.h>

int main()
{
    int balance = 1000, dep;
    printf("Your current balance = %d", balance);
    printf("\nAmount to deposite: ");
    scanf("%d", &dep);
    balance += dep;
    printf("\nNew Balance = %d", balance);
    return 0;
}
*/

// File handling:
#include<stdio.h>
#include<stdlib.h>

void updateBalance(int balance){
    FILE *fp;
    fp = fopen("account.txt", "w");
    fprintf(fp, "%d", balance);
    fclose(fp);
}
void updateTransactions(int amount, int count){
    int old_transactions[100], i=0, j=0, num=0;
    FILE *fp;
    // Reading all the data from file
    fp = fopen("transactions.txt", "r");
    for(i = 0; i < count; i++){
        fscanf(fp, "%d", &old_transactions[i]);
        fseek(fp, 1, SEEK_CUR);
    }
    old_transactions[i] = amount;
    fclose(fp);

    // Printing the array
    printf("Array: ");
    for(j = 0; j <= count+1; j++){
        printf("%d\n", old_transactions[j]);
    }

    // saving back to the file
    fp = fopen("transactions.txt", "w");
    for(j = 0; j < count+1; j++){
        fprintf(fp, "%d\n", old_transactions[count-j-1]);
    }
    fclose(fp);
}
void getLastTransaction(){
    FILE *fp;
    fp = fopen("transactions.txt", "r");



    // printf("\nCursor's current postion: %d\n", ftell(fp));
    // fprintf(fp, "17000");
    // printf("\nCursor's current postion: %d\n", ftell(fp));
    fclose(fp);
}

int main()
{
    int balance = 1000, amount, current_bill, op, count_of_transactions = 0;
    FILE *fp;
    fp = fopen("account.txt", "r");
    // scanf("%d", &balance);
    fscanf(fp, "%d", &balance);
    FILE *bill_file;
    bill_file = fopen("bills.txt", "r");
    fscanf(bill_file, "%d", &current_bill);
    fclose(bill_file);
    fclose(fp);
    while (1){
        printf("\nPress:\n");
        printf("1 for deposit\n");
        printf("2 for withdrawl\n");
        printf("3 to check balance\n");
        printf("4 to view the last transaction\n");
        printf("9 to exit\n");
        scanf("%d", &op);
        switch (op)
        {
        case 1:
            printf("\nAmount to deposite: ");
            scanf("%d", &amount);
            balance += amount;
            printf("\nNew Balance = %d\n", balance);
            updateBalance(balance);
            count_of_transactions++;
            updateTransactions(amount, count_of_transactions);
            break;
        
        case 2:
            printf("\nAmount to withdraw: ");
            scanf("%d", &amount);
            balance -= amount;
            printf("\nNew Balance = %d\n", balance);
            updateBalance(balance);
            count_of_transactions++;
            amount = (-amount);
            updateTransactions(amount, count_of_transactions);
            break;
        
        case 3:
            printf("\nCurrent Balance = %d\n", balance);
            printf("Your current bill = %d\n", current_bill);
            break;
        
        case 4:
            printf("Last transaction:\n");
            getLastTransaction();
            break;

        case 9:
            exit(0);

        default:
            break;
        }
    }
    return 0;
}

// Next Class: ftell, fseek (in getLastTransaction function) and strings in file