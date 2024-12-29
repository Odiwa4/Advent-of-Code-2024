using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;

namespace AOC2015.Day2;
class Day2
{
    public static void Main()
    {
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        string[] lines = File.ReadAllLines(filePath);
        int answer = 0;
        int ribbonCost = 0;
        foreach (string l in lines){
            string[] splitLine = l.Split("x");
            int length = Convert.ToInt32(splitLine[0]);
            int width = Convert.ToInt32(splitLine[1]);
            int height = Convert.ToInt32(splitLine[2]);

            int[] lengths = [length, width, height];
            int[] sides = [length*width, width*height, height*length];
            Array.Sort(lengths);
            Array.Sort(sides);

            answer += (2*length*width) + (2*width*height) + (2*height*length) + sides[0];
            ribbonCost += (lengths[0] * 2) + (lengths[1] * 2) + (length*width*height);
        }
        Console.WriteLine($"Part 1: {answer}");
        Console.WriteLine($"Part 2: {ribbonCost}");
    }
}