using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using System.Linq;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {

            Dictionary<string, Plant> plants = new Dictionary<string, Plant>();

            int n = int.Parse(Console.ReadLine());
            for (int i = 0; i < n; i++)
            {
                string[] command = Console.ReadLine().Split("<->");
                if (plants.ContainsKey(command[0]))
                    {
                    plants[command[0]].Rarity = int.Parse(command[1]);
                }
                else
                {
                    plants.Add(command[0], new Plant( int.Parse(command[1]), new List<double>()));
                }
            }

            string com = String.Empty;
            while ((com = Console.ReadLine()) != "Exhibition")
            {
                string[] input = com.Split(new char[] { ' ', ':', '-' }, StringSplitOptions.RemoveEmptyEntries);

                if(input.Length <  2 || input.Length > 3)
                {
                    Console.WriteLine("error");
                }
             if(input[0] == "Rate")
                {
                    if (plants.ContainsKey(input[1]))
                    {
                        plants[input[1]].Rating.Add(double.Parse(input[2]));
                    }
                    else
                    {
                        Console.WriteLine("error");
                    }
                }
             else if (input[0] == "Update")
                {
                    if (plants.ContainsKey(input[1]))
                    {
                        plants[input[1]].Rarity = int.Parse(input[2]);
                    }
                    else
                    {
                        Console.WriteLine("error");
                    }
                }
             else if(input[0] == "Reset")
                {
                    if (plants.ContainsKey(input[1]))
                    {
                     plants[input[1]].Rating.Clear();
                    }
                    else
                    {
                        Console.WriteLine("error");
                    }
                }
                else
                {
                    Console.WriteLine("error");
                }
            }



   
            plants = plants.OrderByDescending(x => x.Value.Rarity).ThenByDescending(y=> y.Value.Rating.Count > 0 ? y.Value.Rating.Average() : 0).ToDictionary(a => a.Key, b => b.Value);
            Console.WriteLine("Plants for the exhibition:");
            foreach (var item in plants)
            {
                double avr = 0;
                if (item.Value.Rating.Count > 0)
                {
                    avr = item.Value.Rating.Average();
                }
                   
                    Console.WriteLine($"- {item.Key}; Rarity: {item.Value.Rarity}; Rating: {avr:F2}");
               
                
                
               

            }

        }
       
    }


    public class Plant
    {
        public int Rarity { get; set; }
        public List<double> Rating { get; set; }

        public Plant(int a, List<double> b)
        {
            this.Rarity = a;
          this.Rating = b;
        }
    }

}
