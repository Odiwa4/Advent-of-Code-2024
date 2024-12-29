using System;
using System.IO;
using System.Numerics;
using System.Diagnostics;
namespace AOC2015.Day6;
class Day6
{
    public static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        string[] lines = File.ReadAllLines(filePath);
        bool[,] board = new bool[1000, 1000];
        int[,] partTwoBoard = new int[1000, 1000];
        foreach (string l in lines)
        {
            bool value = false;
            bool toggle = false;
            string[] splitString;
            if (l.Contains("off")){
                value = false;
                splitString = l.Split(" off ");
            }
            else if (l.Contains("toggle")){
                toggle = true;
                splitString = l.Split("toggle ");
            }
            else{
                value = true;
                splitString = l.Split(" on ");
            }
            string[] posSplit = splitString[1].Split(" through ");
            string[] posASplit = posSplit[0].Split(",");
            string[] posBSplit = posSplit[1].Split(",");
            Vector2 posA = new Vector2(Convert.ToInt32(posASplit[0]), Convert.ToInt32(posASplit[1]));
            Vector2 posB = new Vector2(Convert.ToInt32(posBSplit[0]), Convert.ToInt32(posBSplit[1]));
            
            for (int x = (int) posA.X; x <= posB.X; x++){
                for (int y = (int) posA.Y; y <= posB.Y; y++){
                    if (toggle){
                        board[x,y] = !board[x,y];
                        partTwoBoard[x,y]+= 2;
                    }else{
                        board[x,y] = value;
                        if (value)
                            partTwoBoard[x,y]+= 1;
                        else
                            if (partTwoBoard[x,y] > 0)
                                partTwoBoard[x,y]-= 1;
                    }
                }
            }
        }

        int partOneAnswer = 0;
        int partTwoAnswer = 0;
        for (int x = 0; x < 1000; x++){
            for (int y = 0; y < 1000; y++){
                partTwoAnswer += partTwoBoard[x,y];
                if (board[x,y]){
                    partOneAnswer++;
                }
            }
        }
        Console.WriteLine($"Part 1: {partOneAnswer}");
        Console.WriteLine($"Part 2: {partTwoAnswer}");
        stopwatch.Stop();
        TimeSpan elapsed = stopwatch.Elapsed;
        Console.WriteLine($"Time: {elapsed.Seconds}.{elapsed.Milliseconds}");
    }
}