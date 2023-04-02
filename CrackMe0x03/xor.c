#include <stdio.h>
#include <string.h>

void encode1(int num, unsigned char* encoded);
void encode2(unsigned char* num_ptr, unsigned char* encoded);
void encode3(unsigned char* num_ptr, unsigned char* encoded);
void printAscii(unsigned char* encoded);

int main() {
    unsigned int num;
    unsigned char encoded1[8];
    unsigned char encoded2[8];
    unsigned char encoded3[8];

    // Prompt the user to enter a number
    printf("Enter a number: ");
    scanf("%d", &num);

    // Encode the number using three different techniques
    encode1(num, encoded1);
    encode2(encoded1, encoded2);
    encode3(encoded2, encoded3);

    // Print the encoded bytes in hexadecimal form
    printf("Encoded 1: %02x %02x %02x %02x\n", encoded1[0], encoded1[1], encoded1[2], encoded1[3]);
    printf("Encoded 2: %02x %02x %02x %02x\n", encoded2[0], encoded2[1], encoded2[2], encoded2[3]);
    printf("Encoded 3: %02x %02x %02x %02x\n", encoded3[0], encoded3[1], encoded3[2], encoded3[3]);

    // Print the encoded bytes from encode3 as ASCII characters
    printf("Encoded 3 as ASCII: ");
    printAscii(encoded3);

    return 0;
}

// Encoding technique 1: simply convert the number to bytes
void encode1(int num, unsigned char* encoded) {
    memcpy(encoded, &num, 4);
}

// Encoding technique 2: XOR each byte with a fixed value
void encode2(unsigned char* num_ptr, unsigned char* encoded) {
    int key = 0x55AA55AA;
    unsigned char* key_ptr = (unsigned char*) &key;
    for (int i = 0; i < 4; i++) {
        encoded[i] = num_ptr[i] ^ key_ptr[i];
    }
}

// Encoding technique 3: perform a bitwise rotation on each byte
void encode3(unsigned char* num_ptr, unsigned char* encoded) {
    for (int i = 0; i < 4; i++) {
        encoded[i] = (num_ptr[i] << 3) | (num_ptr[i] >> 5);
    }
}

// Print the encoded bytes as ASCII characters
void printAscii(unsigned char* encoded) {
    for (int i = 0; i < 4; i++) {
        printf("%c", encoded[i]);
    }
    printf("\n");
}
