#include <stdio.h>
#include <string.h>

void decode3(unsigned char* encoded, unsigned char* decoded);
void decode2(unsigned char* encoded, unsigned char* decoded);
int decode1(unsigned char* encoded);

int main() {
    unsigned char encoded1[4] = {63, 59, 42, 45};
    unsigned char encoded2[4] = {0xa6, 0xfb, 0x1d, 0x0e};
    unsigned char encoded3[4] = {0xa2, 0x57, 0x78, 0x1b};

    // Decode the bytes to obtain the original number
    unsigned char decoded3[4];
    decode3(encoded3, decoded3);
    unsigned char decoded2[4];
    decode2(encoded2, decoded2);
    unsigned char decoded1[4];
    decoded1[0] = decode1(encoded1);

    // Combine the bytes into a single integer
    int num = *((int*)decoded1);

    // Print the original number and the corresponding ASCII output
    printf("Original number: %d\n", num);
    printf("ASCII output: %s\n", decoded3);

    return 0;
}

void decode3(unsigned char* encoded, unsigned char* decoded) {
    for (int i = 0; i < 4; i++) {
        decoded[i] = (encoded[i] >> 5) | (encoded[i] << 3);
    }
}

void decode2(unsigned char* encoded, unsigned char* decoded) {
    int key = 0xDEADBEEF;
    unsigned char* key_ptr = (unsigned char*) &key;
    for (int i = 0; i < 4; i++) {
        decoded[i] = encoded[i] ^ key_ptr[i];
    }
}

int decode1(unsigned char* encoded) {
    int num;
    memcpy(&num, encoded, 4);
    return num;
}