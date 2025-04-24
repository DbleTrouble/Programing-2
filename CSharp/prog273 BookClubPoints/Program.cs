using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog273_BookClubPoints
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the number of books purchased this month: ");
            int b = int.Parse(Console.ReadLine());
            if (b == 0)
            {
                Console.WriteLine("You have earned 0 points");
            }
            else if (b == 1)
            {
                Console.WriteLine("You have earned 5 points");
            }
            else if (b == 2)
            {
                Console.WriteLine("You have earned 15 points");
            }
            else if (b == 3)
            {
                Console.WriteLine("You have earned 30 points");
            }
            else if (b >= 4)
            {
                Console.WriteLine("You have earned 60 points");
            }
            Console.ReadLine();
        }
    }
}
