#include <stdio.h>
#include <stdlib.h>

int main() {
  char alphaNumArr[] = ""; // array of all lowercase alpha numeric characters
  int inputNum, numLength, i;

  printf("Enter a number: ");
  scanf("%d", &inputNum);

  // calculate the length of the input number
  numLength = snprintf(NULL, 0, "%d", inputNum);

  // allocate memory for an array to hold each digit in the input number
  int* digitsArr = (int*) malloc(numLength * sizeof(int));

  // store each digit of the input number in the digitsArr array
  for (i = numLength-1; i >= 0; i--) {
    digitsArr[i] = inputNum % 10;
    inputNum /= 10;
  }

  // print out the characters corresponding to each digit in the input number
  for (i = 0; i < numLength; i++) {
    printf("%c", alphaNumArr[digitsArr[i]]);
  }

  // free the dynamically allocated memory
  free(digitsArr);

  return 0;
}