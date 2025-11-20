/*
   ========================================
   hash_fn.c — implement your hash functions
   ========================================

   Description:
    This file contains the hash functions for integer and string keys.

   Development History:
    - 2025/11/11: Initial implementation
    - 2025/11/17: Refactored to use hash_fn.h
    - 2025/11/20: complete

   Developer: jettinglin <s1121443@mail.yzu.edu.tw>
 */

#include "hash_fn.h"

int myHashInt(int key, int m) {
    // TODO: replace with your own design
    double A = 0.6180339887;                 
    double frac = key * A - (int)(key * A);  
    return (int)(m * frac);                 
    //return key % m;  // division method example
}

int myHashString(const char* str, int m) {
    /*unsigned long hash = 0;
    unsigned char c;
    while ((c = (unsigned char)*str++) != '\0') {
        hash += c;
    }*/
    // TODO: replace with your own design
    unsigned long hash = 5381;
    unsigned char c;
    while ((c = (unsigned char)*str++) != '\0') {
        hash = ((hash * 33) + hash) + c;
    }

    return (int)(hash % m); // basic division method
}
