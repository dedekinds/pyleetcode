状态机  逻辑要清晰

class Solution {
public:
    bool checkmatch(char* str, char* pattern){
        if (*str == '\0' && *pattern == '\0')
            return true;
        if (*str != '\0' && *pattern =='\0')
            return false;
        
        if (*(pattern+1) == '*'){
            if (*str == *pattern || (*pattern == '.' && *str != '\0') )
                return checkmatch(str+1,pattern+2)\
                        || checkmatch(str+1,pattern)\
                        || checkmatch(str,pattern+2);
            else
                return checkmatch(str,pattern+2);
        }
        if (*str == *pattern || (*pattern == '.' && *str != '\0') )
            return checkmatch(str+1,pattern+1);
        return false;
    }
    bool match(char* str, char* pattern){
        if (str == nullptr || pattern == nullptr){
            return false;
        }
        return checkmatch(str,pattern);
    }
};