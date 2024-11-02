public class Solution {
    public IList<string> GenerateParenthesis(int n) {
        IList<string> validParentheses = new List<string>();

        void Generate(string s, int open, int closed) {
            if (s.Length == 2 * n) {
                validParentheses.Add(s);
                return;
            }

            if (open < n) Generate(s + "(", open + 1, closed);

            if (closed < open) Generate(s + ")", open, closed + 1);
        }

        // Anfang der Rekursion
        Generate("", 0, 0);

        return validParentheses;
    }
}
