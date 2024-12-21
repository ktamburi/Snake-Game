// C program to build the complete
// snake game
#include <conio.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int i, j, height = 30, width = 60;
int gameover, score;
int x, y, fruitx, fruity, flag;

// Function to generate the fruit
// within the boundary
void setup()
{
	gameover = 0;
	// Stores height and width
	y = height / 2;
	x = width / 2;
label1:
	fruity = rand() % 30;
	if (fruity == 0)
		goto label1;
label2:
	fruitx = rand() % 60;
	if (fruitx == 0)
		goto label2;
	score = 0;
}

// Function to draw the boundaries
void draw()
{
	system("cls");
	for (i = 0; i <= height; i++) {
		for (j = 0; j <= width; j++) {
			if (i == 0 || i == height || j == 0 || j == width ) {
				printf("#");
			}
			else {
				if (i == y && j == x)
					printf("O");
				else if (i == fruity && j == fruitx)
					printf("*");
				else
					printf(" ");
			}
		}
		printf("\n");
	}

	// Print the score after the
	// game ends
	printf("score = %d", score);
	printf("\n");
	printf("press X to quit the game");
}

// Function to take the input
void input()
{
	if (kbhit()) {
		switch (getch()) {
		case 75:
			flag = 1;
			break;
		case 80:
			flag = 2;
			break;
		case 77:
			flag = 3;
			break;
		case 72:
			flag = 4;
			break;
		case 'x':
			gameover = 1;
			break;
		}
	}
}

// Function for the logic behind
// each movement
void logic()
{
	sleep(0.02);
	switch (flag) {
	case 1:
		x--;
		break;
	case 2:
		y++;
		break;
	case 3:
		x++;
		break;
	case 4:
		y--;
		break;
	default:
		break;
	}

	// If the game is over
	if (y <= 0 || y >= height || x <= 0 || x >= width)
		gameover = 1;

	// If snake reaches the fruit
	// then update the score
	if (y == fruity && x == fruitx) {
	label3:
		fruity = rand() % 30;
		if (fruity == 0)
			goto label3;

	// After eating the above fruit
	// generate new fruit
	label4:
		fruitx = rand() % 60;
		if (fruitx == 0)
			goto label4;
		score += 1;
	}
}

// Driver Code
int main()
{
    // Generate boundary
	setup();

	// Until the game is over
	while (!gameover) {

		// Function Call
		draw();
		input();
		logic();
	}
    return 0;
}