using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LP_4_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter package weight in kilograms: ");
            int we = int.Parse(Console.ReadLine());
            Console.Write("Enter package length in centimeters: ");
            int l = int.Parse(Console.ReadLine());
            Console.Write("Enter package width in centimeters: ");
            int wi = int.Parse(Console.ReadLine());
            Console.Write("Enter package height in centimeters: ");
            int h = int.Parse(Console.ReadLine());

            if ((we >= 27 && l >= 100000) || (we >= 27 && wi >= 100000) || (we >= 27 && h >= 100000))
            {
                Console.WriteLine("Too Heavy and Too Large");
            }
            else if (we >= 27)
            {
                Console.WriteLine("Too Heavy");
            }
            else if (l >= 100000)
            {
                Console.WriteLine("Too large");
            }
            else if (wi >= 100000)
            {
                Console.WriteLine("Too large");
            }
            else if (h >= 100000)
            {
                Console.WriteLine("Too large");
            }
            else
            {
                Console.WriteLine("The package is all good");
            }
            Console.ReadLine();
        }
    }
}
