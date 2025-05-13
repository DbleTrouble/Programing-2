using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ListDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // List<TYPE> name = new List<TYPE>();
            List<string> lines = new List<string>();
            List<int> nums = new List<int>() { 1, 2, 3 };

            nums.Add(4);
            nums.Add(5);
            nums.Add(6);
            nums.Add(7);

            nums.RemoveAt(5); // Removes '6'
            nums.Remove(7); // Removes '7'

            Console.WriteLine("Length: " + nums.Count);
            Console.WriteLine(string.Join(", ", nums)); // "1, 2, 3, 4, 5"

            foreach (int n in nums)
                Console.WriteLine(n);

            nums[0] = 100;
            Console.WriteLine(nums[0]);

            Console.ReadLine();

        }
    }
}
