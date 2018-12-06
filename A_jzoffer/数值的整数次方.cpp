
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。 

#include<stdlib.h>
class Solution {
public:
    double Power(double base, int exponent) {
        if (exponent == 0) return 1;
        else if (exponent == 1) return base;
        if (exponent > 0){
            double res = Power(base,exponent>>1);
            res *= res;
            if (exponent % 2 !=0) res *= base;
            return res;
        }
        else return 1/Power(base,0-exponent);
 
    }
};