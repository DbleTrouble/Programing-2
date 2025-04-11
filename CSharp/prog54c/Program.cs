using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54c
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Radius: ");
            int rad = int.Parse(Console.ReadLine());
            double pie = 3.14159;
            double area = pie * Math.Pow(rad,2);
            double circum = 2 * pie * rad;
            Console.WriteLine("Area: " + area);
            Console.WriteLine("Circumference: " + circum);
            Console.ReadLine();
        }
    }
}
