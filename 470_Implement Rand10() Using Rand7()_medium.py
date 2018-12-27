// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        int temp;
        while(1){
            temp = 7*(rand7() - 1) + rand7();
            if (temp <= 40)
                return temp%10+1;
        }
    }
};


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        return 1+(rand7()+rand7()+rand7()+rand7()+rand7())%10