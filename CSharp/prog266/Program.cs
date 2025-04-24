using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog266
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Number 1: ");
            double num1 = double.Parse(Console.ReadLine());
            Console.Write("Enter Number 2: ");
            double num2 = double.Parse(Console.ReadLine());

            if (num1 > num2)
            {
                Console.WriteLine("Number 1 is greater than Number 2");
            }
            else
            {
                Console.WriteLine("Number 2 is greater than Number 1");
            }
            Console.ReadLine();
        }
    }
}
