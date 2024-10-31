public class Solution {
    public bool IsValid(string s) {
        Stack stack = new Stack();

        for(int i = 0; i < s.Length; i++){
            char character = s[i];

            if(character == '(' || character == '{' || character == '['){
                stack.Push(character);

            } else{
                //Wenn Stack leer oder missmatch
                if(stack.Count == 0 || 
                (character == ')' && (char)stack.Peek() != '(') || 
                (character == '}' && (char)stack.Peek() != '{') || 
                (character == ']' && (char)stack.Peek() != '['))
                {
                    return false;
                }

                stack.Pop();
            }
        }

        //Stack muss leer sein
        return stack.Count == 0;
    }
}
