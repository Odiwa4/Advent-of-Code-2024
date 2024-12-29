using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using System.Numerics;

namespace AOC2015.Day3;
class Day3
{
    public static void Main()
    {
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        Dictionary<Vector2, int> posMap = new Dictionary<Vector2, int>();
        Dictionary<char, Vector2> charMap = new Dictionary<char, Vector2> { ['<'] = new Vector2(-1, 0), ['>'] = new Vector2(1, 0), ['v'] = new Vector2(0, -1), ['^'] = new Vector2(0, 1) };
        Vector2 currentPos = new Vector2(0, 0);
        posMap.Add(currentPos, 0);
        string instructions = File.ReadAllLines(filePath)[0];
        foreach (char c in instructions)
        {
            currentPos += charMap[c];
            if (posMap.ContainsKey(currentPos))
                posMap[currentPos] += 1;
            else
                posMap.Add(currentPos, 1);
        }

        Dictionary<Vector2, int> partTwoMap = new Dictionary<Vector2, int>();
        Vector2 robotPos = new Vector2(0, 0);
        Vector2 santaPos = new Vector2(0, 0);
        partTwoMap.Add(robotPos, 0);
        for (int c = 0; c < instructions.Length; c++)
        {
            if (c % 2 != 0)
            {
                robotPos += charMap[instructions[c]];
                if (partTwoMap.ContainsKey(robotPos))
                    partTwoMap[robotPos] += 1;
                else
                    partTwoMap.Add(robotPos, 1);
            }
            else
            {
                Console.WriteLine(c);
                santaPos += charMap[instructions[c]];
                if (partTwoMap.ContainsKey(santaPos))
                    partTwoMap[santaPos] += 1;
                else
                    partTwoMap.Add(santaPos, 1);
            }
        }

        Console.WriteLine($"Part 1: " + posMap.Keys.Count);
        Console.WriteLine($"Part 2: " + partTwoMap.Keys.Count);
    }
}