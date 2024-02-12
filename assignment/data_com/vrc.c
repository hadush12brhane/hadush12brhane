"""#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
	int a[20][20],ch,i,j,k,no,n,m,sum,re,r[50],flag=0;
	clrscr();
	do
	{
	printf("\nVRC");
	printf("\n1.Sender \n2.Receiver\n3.Exit");
	printf("\nEnter your choice:");
	scanf("%d",&ch);
	switch(ch)
	{
	case 1:
		printf("Enter No. of Messages:");
		scanf("%d",&n);
		printf("\nEnter the no. of bits for message:");
		scanf("%d",&m);
		for(i=0;i<n;i++)
		{
			printf("\nEnter %d message=",i+1);
			for(j=0;j<m;j++)
				scanf("%d",&a[i][j]);
		}
		for(i=0;i<n;i++)
		{
			sum=0;
			for(j=0;j<m;j++)
				sum=sum+a[i][j];
		 a[i][j]=(sum%2);
		}
		for(i=0;i<=m;i++)
		{
			sum=0;
			for(j=0;j<n;j++)
				sum=sum+a[j][i];
		 a[j][i]=(sum%2);
		}
		printf("\nMessage sent is :-\n");
		for(i=0;i<=n;i++)
		{
		 for(j=0;j<=m;j++)
			printf("%d ",a[i][j]);
		printf("  ");
		}
	break;

	case 2:
	flag=0;
		printf("Enter Number of bits for received message=");
		scanf("%d",&re);
		printf("\nEnter The Received Message:-\n");
		for(i=0;i<re;i++)
			scanf("%d",&r[i]);
		printf("Enter Number of Messages=");
		scanf("%d",&n);
		m=re/(n+1);
		k=0;
		for(i=0;i<=n;i++)
		{
			for(j=0;j<m;j++)
			{
				a[i][j]=r[k];
				k++;
			}
		}
		for(i=0;i<=n;i++)
		{
			for(j=0;j<m;j++)
			printf("%d ",a[i][j]);
		 printf("\n");
		}

		for(i=0;i<=n;i++)
		{
			sum=0;
			for(j=0;j<m;j++)
			{
				sum=sum+a[i][j];
			}
			if(sum%2!=0)
			{
				printf("\nThere is an Error");
				flag=1;
				break;
			}
		}
		if(flag!=1)
		{
			for(i=0;i<m;i++)
			{
				sum=0;
				for(j=0;j<=n;j++)
				{
					sum=sum+a[j][i];
				}
				if(sum%2!=0)
				{
					printf("\nThere is an Error");
					flag=1;
					break;
				}
			}
		}
		if(flag!=1)
		printf("No Error");
		break;
	case 3: exit(0);
      }
     }while(1);
}"""

#include <stdio.h>
#include <string.h>

// Function prototypes
int calculateVRC(char data[]);
int calculateLRC(char data[]);

int main() {
    char data[100];
    int choice;

    do {
        // Display menu
        printf("\nMenu:\n");
        printf("1. Enter data\n");
        printf("2. Calculate VRC\n");
        printf("3. Calculate LRC\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                // Enter data
                printf("Enter data stream (up to 99 characters): ");
                scanf("%s", data);
                break;

            case 2:
                // Calculate VRC
                if (strlen(data) == 0) {
                    printf("Error: Please enter data first.\n");
                } else {
                    printf("VRC: %d\n", calculateVRC(data));
                }
                break;

            case 3:
                // Calculate LRC
                if (strlen(data) == 0) {
                    printf("Error: Please enter data first.\n");
                } else {
                    printf("LRC: %d\n", calculateLRC(data));
                }
                break;

            case 4:
                // Exit
                printf("Exiting program.\n");
                break;

            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    } while (choice != 4);

    return 0;
}

// Function to calculate Vertical Redundancy Check (VRC)
int calculateVRC(char data[]) {
    int vrc = 0;
    int len = strlen(data);

    for (int i = 0; i < len; i++) {
        vrc ^= data[i];
    }

    return vrc;
}

// Function to calculate Longitudinal Redundancy Check (LRC)
int calculateLRC(char data[]) {
    int lrc = 0;
    int len = strlen(data);

    for (int i = 0; i < len; i++) {
        lrc += data[i];
    }

    return lrc % 256;
}
