using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog85c
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter birth month based on number 1 - 12: ");
            int month = int.Parse(Console.ReadLine());
            Console.Write("Enter birth day: ");
            int day = int.Parse(Console.ReadLine());
            double sa = ((((((month * 5) + 6) * 4) + 9) * 5) + day);
            double a1 = Math.Floor((sa - 165) / 100);
            double a2 = ((sa - 165) % 100);
            Console.WriteLine("Your Number: " + sa);
            Console.WriteLine("Brithday: " + a1 + "/" + a2);
            Console.ReadLine();
        }
    }
}
