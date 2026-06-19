class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int width = 9;
        int height = 9;

        //ver se j linha esta valida (o elemento ainda nao apareceu no set linha)
        for(int i = 0 ; i < height; i++){
            unordered_set<char> l;
            for(int j = 0; j < width; j++){
                char value = board[i][j];
                if(value == '.') continue;

                if(l.find(value) != l.end()) return false;

                l.insert(value);
            } 
        }

        //ver se a coluna x esta valida
        for(int i = 0; i < width; i++){
            unordered_set<char> c;
            for(int j = 0; j < height; j++){
                char value = board[j][i];

                if(value == '.') continue;

                if(c.find(value) != c.end()) return false;

                c.insert(value);
            }
        }

        for(int i = 0; i < height; i += 3){
            for(int j = 0 ; j < width; j += 3){
                
                unordered_set<char> r;
                
                for(int k = 0; k < 3; k++){
                    for(int l = 0 ; l < 3; l++){
                        char value = board[i + k][j + l];

                        if(value == '.') continue;

                        if(r.find(value) != r.end()) return false;

                        r.insert(value);
                    }
                }

            }
        }

        return true;
    }
};
