#include <stdio.h>

void printBanner(){
    puts("   _____                                  __  __       _\n"       
"  / ____|                                |  \\/  |     | |           \n"
" | (___   __ _ _   _ ___  __ _  __ _  ___| \\  / | __ _| | _____ _ __ \n"
"  \\___ \\ / _` | | | / __|/ _` |/ _` |/ _ \\ |\\/| |/ _` | |/ / _ \\ '__|\n"
"  ____) | (_| | |_| \\__ \\ (_| | (_| |  __/ |  | | (_| |   <  __/ |   \n"
" |_____/ \\__,_|\\__,_|___/\\__,_|\\__, |\\___|_|  |_|\\__,_|_|\\_\\___|_|   \n"
"                                __/ |                                \n"
"                               |___/                                 \n");
}

int main() {
    printBanner();
    unsigned int input, result;
    const int XOR_VALUE_1 = 0xDEADBEEF; // First XOR value
    const int XOR_VALUE_2 = 0xFEEDFACE; // Second XOR value
    const int XOR_VALUE_3 = 0xBEEFFACE; // Third XOR value
    
    // Get input from user
    printf("Enter a number: ");
    scanf("%d", &input);
    
    // Perform three XOR operations
    result = input ^ XOR_VALUE_1;
    result ^= XOR_VALUE_2;
    result ^= XOR_VALUE_3;
    
    // Output the final result in hexadecimal format
    printf("Result: 0x%x\n", result);
    
    return 0;
}