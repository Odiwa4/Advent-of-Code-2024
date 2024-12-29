using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

namespace AOC2015.Day1;
class Day1
{
    public static void Main()
    {
        int floor = 0;
        int index = 0;
        bool finishedP2 = false;
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");

        string[] lines = File.ReadAllLines(filePath);

        foreach (string l in lines)
        {
            foreach (char c in l)
            {
                if (c == '(')
                {
                    floor++;
                    if (!finishedP2)
                        index++;
                }
                else if (c == ')')
                {
                    floor--;
                    if (!finishedP2)
                        index++;
                }
                
                if (floor < 0)
                {
                    finishedP2 = true;
                }
            }
        }
        Console.WriteLine($"Part 1: {floor}");
        Console.WriteLine($"Part 2: {index}");
    }
}
