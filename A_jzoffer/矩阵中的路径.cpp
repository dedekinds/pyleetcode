请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。 


class Solution {
public:
    bool search(char* matrix,vector<char> flag, char* str,int rows,int cols,int i,int j){
        if (i < 0 || j < 0 || i >= rows || j >= cols) return false;
        if (matrix[i*cols+j] == *str && flag[i*cols+j] == 0){
            flag[i*cols+j] = 1;
            if (*(str+1) == 0) return true;
            bool res = search(matrix,flag,str+1,rows,cols,i-1,j)||\
                search(matrix,flag,str+1,rows,cols,i+1,j)||\
                search(matrix,flag,str+1,rows,cols,i,j-1)||\
                search(matrix,flag,str+1,rows,cols,i,j+1);
            if (!res) flag[i*cols+j] = 0;
            return res;
        }
        else return false;
    }
    bool hasPath(char* matrix, int rows, int cols, char* str){
        if (matrix == nullptr || str == nullptr) return false;
        vector<char> flag(rows*cols,0);
        bool res = false;
        for (int i=0; i<rows; i++){
            for (int j=0; j<cols; j++){
                res = search(matrix,flag,str,rows,cols,i,j);
                if(res) return true;
            }
        }
        return false;
    }
 
 
};

——————————————————————————————————————————————————————————————————————————————
class Solution(object):
    def dfs(self,matrix,string,index,x,y):
        rows = len(matrix)
        cols = len(matrix[0])
        if matrix[x][y] != string[index]:return False
        if index == len(string)-1:return True
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        temp = matrix[x][y]
        matrix[x][y] = '*'
        for i in range(len(dx)):
            m = x + dx[i]
            n = y + dy[i]
            if m >=0 and m < rows and n >=0 and n < cols:
                if self.dfs(matrix,string,index+1,m,n):return True
        matrix[x][y] = temp
        return False
        
        
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        rows = len(matrix)
        if rows == 0 :return False
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if self.dfs(matrix,string,0,i,j):
                    return True
        return False;