/**
Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192

Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
   return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:
If this function is called many times, how would you optimize it?

**/


/**

Let's look at how it's done for an 8 bit value:

The first line in the function takes every second bit and moves it left or
right:

12345678  -->  1-3-5-7-  -->  -1-3-5-7  -->  21436587
               -2-4-6-8       2-4-6-8-
The second line takes groups of two bits and moves left or right:

21436587  -->  21--65--  -->  --21--65  -->  43218765
               --43--87       43--87--
The third line takes groups of four bits and moves left or right:

43218765  -->  4321----  -->  ----4321  -->  87654321
               ----8765       8765----
Now the bits are reversed. For a 32 bit value you need two more steps that moves
bits in groups of 8 and 16.

**/

uint32_t reverseBits(uint32_t n) {
 
    n = (((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1));
    n = (((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2));
    n = (((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4));
    n = (((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8));

    return((n >> 16) | (n << 16));

}