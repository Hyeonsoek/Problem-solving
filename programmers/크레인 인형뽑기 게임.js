function solution(board, moves) {
    var answer = 0;
    var stack = [];
    
    for(var idx in moves) {
        for(var row = 0; row < board.length; row++) {
            if(board[row][moves[idx]-1] == 0)
                continue;
            
            stack.push(board[row][moves[idx]-1]);
            board[row][moves[idx]-1] = 0;
            if(stack.length > 1 && stack[stack.length-2] == stack[stack.length-1]) {
                stack.pop(); stack.pop(); answer+=2;
            }
            
            break;
        }
    }
    
    return answer;
}