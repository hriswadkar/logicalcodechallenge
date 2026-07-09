using System;

public class ValidAnagram
{
    public static void Main(String[] args)
    {
        ValidAnagram va = new ValidAnagram();
        Console.WriteLine(va.IsAnagram("anagram", "nagaram"));
        Console.WriteLine(va.IsAnagram("rat", "car"));
        Console.WriteLine(va.IsAnagram("a", "ab"));
        Console.WriteLine(va.IsAnagram("ba", "ab"));

    }

    public bool IsAnagram(String first, String second)
    {
        if(first.Length != second.Length)
        {
            return false;
        } else
        {
            char[] a = first.ToCharArray();
            char[] b = second.ToCharArray();
            Array.Sort(a);
            Array.Sort(b);

            return new String(a) == new string(b);
        }
    }
}