using System;
using System.IO;
namespace AOC2015.Day5;
class Day5
{
    public static void Main()
    {
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        string[] lines = File.ReadAllLines(filePath);

        int partOneAnswer = 0;
        List<char> vowelList = ['a', 'e', 'i', 'o', 'u'];
        foreach (string l in lines){
            if (l.Contains("ab") || l.Contains("cd") || l.Contains("pq") || l.Contains("xy")){
                continue;
            }
            int vowelCount = 0;
            bool nice = false;
            for (int c = 0; c < l.Length; c++){
                if (c != l.Length - 1){
                    if (l[c] == l[c+1])
                        nice = true;}

                if (vowelList.Contains(l[c]))
                    vowelCount++;
            }
            if (vowelCount >= 3 && nice)
                partOneAnswer += 1;
        }

        int partTwoAnswer = 0;
        foreach (string l in lines){
            bool repeat = false;
            bool paired = false;
            List<string> pairs = new List<string>();
            for (int c = 0; c < l.Length; c++){
                if (c < l.Length - 2){
                    if (l[c] == l[c+2])
                        repeat = true;}
                if (c != l.Length - 1){
                    string pair = l[c].ToString() + l[c+1].ToString();
                    if (pairs.Contains(pair)){
                        if (pairs.IndexOf(pair) != c - 1)
                            paired = true;
                    }
                    pairs.Add(pair);
                }
            }
            if (repeat && paired){
                partTwoAnswer++;
            }
        }
        Console.WriteLine($"Part 1: {partOneAnswer}");
        Console.WriteLine($"Part 2: {partTwoAnswer}");
    }
}