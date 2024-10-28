using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> LetterCombinations(string digits) {
        if (string.IsNullOrEmpty(digits)) {
            return new List<string>();
        }

        Dictionary<char, string> phoneMap = new Dictionary<char, string> {
            ['2'] = "abc",
            ['3'] = "def",
            ['4'] = "ghi",
            ['5'] = "jkl",
            ['6'] = "mno",
            ['7'] = "pqrs",
            ['8'] = "tuv",
            ['9'] = "wxyz"
        };

        List<string> letters = new List<string>();
        
        foreach(char digit in digits){
            letters.Add(phoneMap[digit]);
        }

        List<string> result = new List<string>();
        genCombos(letters, 0, "", result);
        
        return result;
    }

    public void genCombos(List<string> letters, int index, string current, List<string> result){
        if (index == letters.Count){ //Rekursionsanker
            result.Add(current);
            return;
        }

        foreach(char letter in letters[index]){
            genCombos(letters, index + 1, current + letter, result);
        }
    }
}
