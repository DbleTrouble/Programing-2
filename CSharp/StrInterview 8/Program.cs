﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrInterview_8
{
    class Program
    {
       
        static void Main(string[] args)
        {
            Console.Write("Enter word: ");
            string word = Console.ReadLine().ToLower();
            Console.Write("Enter letter to find: ");
            char letter = Console.ReadLine().ToLower()[0];

            int l = 0;

            for (int i = 0; i < word.Length; i++)
            {
                if (word[i] == letter)
                {
                    l++;
                }
            }
            Console.WriteLine("The word is {0} the number of the letter '{1}' in the word is {2}", word, letter, l);
            Console.ReadLine();
        }
    }
}
