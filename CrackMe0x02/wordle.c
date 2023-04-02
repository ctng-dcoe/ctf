#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define NUM_STRINGS 20
#define STR_LEN 5

char *strings[NUM_STRINGS] = {
    "apple",
    "candy",
    "melon",
    "dates",
    "elder",
    "figgy",
    "grape",
    "honey",
    "pears",
    "juice",
    "kiwis",
    "lemon",
    "mango",
    "pasta",
    "olive",
    "peach",
    "scone",
    "berry",
    "straw",
    "cyber"
};

void printBanner(){
    puts("            ___          _ _      ____  \n"
"           / _ \\        | | |    |___ \\ \n"
" __      _| | | |_ __ __| | |      __) |\n"
" \\ \\ /\\ / / | | | '__/ _` | |     |__ < \n"
"  \\ V  V /| |_| | | | (_| | |____ ___) |\n"
"   \\_/\\_/  \\___/|_|  \\__,_|______|____/ \n"
                                        
    );
}
char *obfuscated_flag = "dudzcfs|e4cvh`n1e4`bdujwbu4e~";  // obfuscated value for "ctcyber{d3bug_m0d3}"

void win(){
    int len = strlen(obfuscated_flag);
    char* output_string = (char*) malloc((len + 1) * sizeof(char));  // allocate memory for output string
    for (int i = 0; i < len; i++) {
        output_string[i] = obfuscated_flag[i] - 1;  // subtract 1 from each character in the input string
    }
    output_string[len] = '\0';  // add null terminator to output string
    printf("%s\n",output_string);
}

int main() {
    printBanner();
    srand(time(NULL));  // seed random number generator

    int index = rand() % NUM_STRINGS;  // choose random index
    char *answer = strings[index];  // get the corresponding string

    printf("Guess a %d-letter word: ", STR_LEN);
    char guess[STR_LEN + 1];  // allocate space for the guess
    scanf("%s", guess);

    if (strcmp(guess, answer) == 0) {  // compare strings
        printf("Correct! The answer was \"%s\".\n", answer);
        // printf("Flag{you_won_the_game}\n");  // output flag
        win();
    } else if (strcmp(guess, "debug") == 0) {  // check for debug mode
        printf("Debug mode activated!\n");
        printf("Seed used: %d\n",index);

        // Allow one more guess in debug mode
        printf("Make one more guess: ");
        scanf("%s", guess);
        if (strcmp(guess, answer) == 0) {
            printf("Correct! The answer was \"%s\".\n", answer);
            win();
        } else {
            printf("Incorrect. The answer was \"%s\".\n", answer);
        }
    } else {
        printf("Incorrect. The answer was \"%s\".\n", answer);
    }

    return 0;
}