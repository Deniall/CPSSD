using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Toggleboard
{
    class Program
    {
        static void Main()
        {

            //gets the number of rows from the user..
            Console.Write("Please type the number of rows you want and press enter: ");
            string rws = Console.ReadLine();
            int rows;
            if (int.TryParse(rws, out rows))
            {
                //if the user enters anything BUT an integer the program just restarts
            }
            else { Main(); }
            


            //...and the number of columns.
            Console.Write("Please type the number of columns you want and press enter: ");
            string cols = Console.ReadLine();
            int columns;
            if (int.TryParse(cols, out columns))
            {
                // same thing again
            }
            else { Main(); };
            Console.Write(Environment.NewLine);

                bool playgame = true; // while this is set to true, the game runs
                int[,] arr = new int[rows, columns]; // makes the grid of RxC size
                int rowLength = arr.GetLength(0); //gets the length of the first dimension of the array
                int colLength = arr.GetLength(1); //gets the length of the second dimension of the array
            
            
            // this gets the coordinates from the user
            Console.WriteLine("Enter the coordinates of the switch you wish to toggle, in the format \"x,y\".");
            Console.WriteLine("To end the game, type \"end\". When you complete the game, type \"finished\".");
           

            while (playgame == true)
            {
                //this prints out the grid every turn
                Console.Write(Environment.NewLine);
                for (int i = 0; i < rowLength; i++)
                {
                    for (int j = 0; j < colLength; j++)
                    {
                        Console.Write(string.Format("{0} ", arr[i, j]));
                    }
                    Console.Write(Environment.NewLine);
                }
                Console.Write(Environment.NewLine);
                //gets the input (coordinates, 'finished', 'end', or something that will cause errors)
                string input = Console.ReadLine();
                
                // this will end the game if the user enters "end" to quit
                if (input == "end")
                {
                    playgame = false;
                    break;
                }

                // this will check if the user has successfully completed the game or not (crashes if they have for some reason)
                bool allTrue = true;
                if (input == "finished")
                {
                    while (allTrue == true)
                    {
                        for (int x = 0; x < rowLength - 1; x++) { for (int y = 0; y < colLength - 1; y++) { if (arr[x, y] == 1) { continue;} else { allTrue = false; }  } } }

                    if (allTrue == true)
                    {
                        Console.WriteLine("You win, congrats!"); // why does this never execute but the 'else' below it does?
                    }
                    else { Console.WriteLine("Nope, press enter to quit"); }
                    Console.ReadLine();
                    break;
                }

                

                //this turns the coordinates into integers which the program can understand and work with
                List<int> coords = input.Split(',')
                     .Select(t => int.Parse(t))
                     .ToList();

                // making life easier for myself
                int coord1 = coords[0];
                int coord2 = coords[1];
                int c1 = coord1 - 1;
                int c2 = coord2 - 1;

                // this code makes sure the game doesnt break if a bad set of coordinates is entered
                if ((coord1 == 0 || coord2 == 0) || coord1 > rowLength || coord2 > colLength)
                {
                    Console.WriteLine("Not valid coordinates");
                }

                
                // this is where all the logic and the arcane sorcery resides. It's kinda convoluted and hard to understand but
                // basically it just checks if the surrounding coordinates of the one you entered are 1's,0's or out of bounds
                // of the actual array, and then changes the value. there's definitley a better way of doing this. (recursion??)

                if ((c1 >= 0 && c1 < rowLength) && (c2 >= 0 && c2 < colLength)) { if (arr[c1, c2] == 0) { arr[c1, c2] = 1; }else if (arr[c1, c2] == 1) { arr[c1, c2] = 0; }}
                if ((c1 - 1 >= 0 && c1 - 1 < rowLength) && (c2 >= 0 && c2 < colLength)){if (arr[c1 - 1, c2] == 0) { arr[c1 - 1, c2] = 1; } else if (arr[c1 - 1, c2] == 1) { arr[c1 - 1, c2] = 0; }}
                if ((c1 + 1 >= 0 && c1 + 1 < rowLength) && (c2 >= 0 && c2 < colLength)){ if (arr[c1 + 1, c2] == 0) { arr[c1 + 1, c2] = 1; }else if (arr[c1 + 1, c2] == 1) { arr[c1 + 1, c2] = 0; }}
                if ((c1 >= 0 && c1 < rowLength) && (c2 - 1 >= 0 && c2 - 1 < colLength)){if (arr[c1, c2 - 1] == 0) { arr[c1, c2 - 1] = 1; }else if (arr[c1, c2 - 1] == 1) { arr[c1, c2 - 1] = 0; }}
                if ((c1 >= 0 && c1 < rowLength) && (c2 + 1 >= 0 && c2 + 1 < colLength)){if (arr[c1, c2 + 1] == 0) { arr[c1, c2 + 1] = 1; }else if (arr[c1, c2 + 1] == 1) { arr[c1, c2 + 1] = 0; }}
            }
        }
    }
}

