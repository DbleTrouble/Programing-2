using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrInterview_18
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter word: ");
            string word = Console.ReadLine().ToLower();
            Console.Write("Enter letter to remove: ");
            char letter = Console.ReadLine().ToLower()[0];
            string word2 = "";

            for (int i = 0; i < word.Length; i++)
            {
                if (word[i] == letter)
                {
                    word2 = word.Remove(i,1);
                }
            }
            
            Console.WriteLine("The origanl word is {0}, the letter removed is '{1}', the new word is {2}", word, letter, word2);
            Console.ReadLine();
        }
    }
}
