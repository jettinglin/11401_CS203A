/*
   ========================================
   hash_fn.cpp — implement your hash functions
   ========================================

   Description:
    This file contains the hash functions for integer and string keys.

   Development History:
    - 2025/11/11: Initial implementation
    - 2025/11/17: Refactored to use hash_fn.hpp
    - 2025/11/20: complete

    Developer: jettinglin <s1121443@mail.yzu.edu.tw>
 */
#include "hash_fn.hpp"

int myHashInt(int key, int m) {
    // TODO: replace with your own design
    /**/ double A = 0.6180339887;          
    double frac = key * A - (int)(key * A);  
    return (int)(m * frac);          
    //return (key % m + m) % m;  // basic division method
}

int myHashString(const std::string& str, int m) {
    unsigned long hash = 5381;
   // unsigned long hash = 0;
    // TODO: replace with your own design
    for (unsigned char c : str) {
        hash = ((hash * 33) + hash) + c;
    }
    /*for (unsigned char c : str) {
        hash += c;
    }*/
    return static_cast<int>(hash % m);  // basic division method
}
