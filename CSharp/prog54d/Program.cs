using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54d
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Base: ");
            double bas = int.Parse(Console.ReadLine());
            Console.Write("Enter Height: ");
            double hei = int.Parse(Console.ReadLine());
            double area = (bas * hei) / 2;
            double hypo = Math.Sqrt(Math.Pow(bas, 2) + Math.Pow(hei, 2));
            double perim = bas + hei + hypo;
            Console.WriteLine("Hypotenuse: " + Math.Round(hypo, 2));
            Console.WriteLine("Area: " + Math.Round(area, 2));
            Console.WriteLine("Perimeter: " + Math.Round(perim, 2));
            Console.ReadLine();
        }
    }
}
