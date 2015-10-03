using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TomDIY
{
    class Program
    {
        static void Main(string[] args)
        {
            double screwBox = 2.50;
            double sandPaper = .55;
            double lampShades = 30.00;
            double pictureFrames = 7.99;
            double paintBrushes = 6.95;
            double paintLarge = 34.50;
            double paintSmall = 9.95;
            double gardeningPots = 10.00;
            double allPlants = 7.00;
            double costBeforeDeductions = 0;
            double costAfterDeductions = 0;
            double limiterDeductions = 0;
            Console.WriteLine(@"        
  _____                               ____    ___  __   __
 |_   _|   ___    _ __ ___    ___    |  _ \  |_ _| \ \ / /
   | |    / _ \  | '_ ` _ \  / __|   | | | |  | |   \ V / 
   | |   | (_) | | | | | | | \__ \   | |_| |  | |    | |  
   |_|    \___/  |_| |_| |_| |___/   |____/  |___|   |_|  
                ");
            Console.WriteLine("Enter the product code of the item you wish to add to the cart and press enter.");
            Console.WriteLine("When you finish, just press enter without entering a code. This will show you");
            Console.WriteLine("your total order cost, total amt. of deductions, and total after deductions.");
            Console.WriteLine();
            Console.WriteLine("                        Product codes:");
            Console.WriteLine("1: Screw Box         2: Sandpaper        3: Lampshade");
            Console.WriteLine("4: Picture Frames    5: Paint Brushes    6: Paint(Large)");
            Console.WriteLine("7: Paint(Small)      8: Gardening Pots   9: Plants");
            Console.WriteLine();
            Console.WriteLine("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
            int i = 0;
            string[] sBasket = new string[100000];
            for (i = 0; i < sBasket.Length; i++)
            {
                string input = Console.ReadLine();
                if (input == "")
                    break;
                if (input != "1" && input != "2" && input != "3" && input != "4" && input != "5" && input != "6" && input != "7" && input != "8" && input != "9")
                {
                    Console.WriteLine("That is not a valid item");
                    continue;
                }
                sBasket[i] = input;
                Console.WriteLine("Your item has been added.");
            }
            for (int j = 0; j < 100; j++)
            {
                switch (sBasket[j])
                {
                    case "1":
                        costBeforeDeductions += screwBox;
                        break;
                    case "2":
                        costBeforeDeductions += sandPaper;
                        break;
                    case "3":
                        costBeforeDeductions += lampShades;
                        break;
                    case "4":
                        costBeforeDeductions += pictureFrames;
                        break;
                    case "5":
                        costBeforeDeductions += paintBrushes;
                        break;
                    case "6":
                        costBeforeDeductions += paintLarge;
                        break;
                    case "7":
                        costBeforeDeductions += paintSmall;
                        break;
                    case "8":
                        costBeforeDeductions += gardeningPots;
                        break;
                    case "9":
                        costBeforeDeductions += allPlants;
                        break;
                }
            }
            Console.WriteLine("Your total amount before deductions is: " + costBeforeDeductions + " euro.");

            for (int k = 0; k < 100; k++)
            {
                switch (sBasket[k])
                {
                    case "1":
                        costAfterDeductions += screwBox;
                        break;
                    case "2":
                        costAfterDeductions += sandPaper;
                        break;
                    case "3":
                        costAfterDeductions += lampShades;
                        break;
                    case "4":
                        costAfterDeductions += pictureFrames;
                        break;
                    case "5":
                        costAfterDeductions += paintBrushes;
                        break;

                }
                if (costAfterDeductions < 50)
                {
                    double ded50 = costAfterDeductions / 100 * 5;
                    limiterDeductions = ded50;
                }
                if (costAfterDeductions >= 50 && costAfterDeductions < 100)
                {
                    double ded100 = costAfterDeductions / 100 * 7.5;
                    limiterDeductions = ded100;
                }
                if (costAfterDeductions >= 100 && costAfterDeductions < 250)
                {
                    double ded250 = costAfterDeductions / 100 * 10;
                    limiterDeductions = ded250;
                }
                if (costAfterDeductions >= 250)
                {
                    double dedMax = costAfterDeductions / 100 * 15;
                    limiterDeductions = dedMax;
                }
            }
            for (int l = 0; l < 100; l++)
            {
                switch (sBasket[l])
                {
                    case "6":
                        costAfterDeductions += paintLarge / 2;
                        break;
                    case "7":
                        costAfterDeductions += paintSmall / 2;
                        break;
                    case "8":
                        costAfterDeductions += gardeningPots / 4 * 3;
                        break;
                    case "9":
                        costAfterDeductions += allPlants / 4 * 3;
                        break;
                }
            }
            
            double finalCost = costAfterDeductions - limiterDeductions;
            double deductions = costBeforeDeductions - finalCost;
            Console.WriteLine("Your total amount of deductions applied is: " + deductions + " euro.");
            Console.WriteLine("Your total cost after deductions is: " + finalCost + " euro.");
            Console.ReadLine();
        }
    }
}
