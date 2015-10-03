using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AGameOfIntsAndFloats
{
    class Program
    {
        static void Main(string[] args)
        {


            string[,] family = new string[4, 5];
            family[1, 1] = "ormond";
            family[2, 1] = "steffon";
            family[3, 1] = "robert";
            family[3, 2] = "stannis";
            family[5, 3] = "renly";
            family[4, 1] = "joffrey";
            family[4, 2] = "myrcella";
            family[4, 3] = "tommen";
            family[4, 4] = "shireen";

        }

        static void IsParent()
        {

            string a = Console.ReadLine();
            string b = Console.ReadLine();

            int x;
            int y;

            switch (a)
            {
                case "ormond":
                    x = 1;
                    y = 1;
                    break;
                case "steffon":
                    x = 2;
                    y = 1;
                    break;
                case "robert":
                    x = 3;
                    y = 1;
                    break;
                case "stannis":
                    x = 3;
                    y = 2;
                    break;
                case "renly":
                    x = 5;
                    y = 3;
                    break;
                case "joffrey":
                    x = 4;
                    y = 1;
                    break;
                case "myrcella":
                    x = 4;
                    y = 2;
                    break;
                case "tommen":
                    x = 4;
                    y = 1;
                    break;
                case "shireen":
                    x = 1;
                    y = 1;
                    break;


            }

        }












        
    }
}
