using System.Diagnostics;

namespace AOC2019.Day2;
class Day2
{
    public static List<int> RunProgram(List<int> instructions, int memoryA, int memoryB)
    {
        List<int> newInstructions = new List<int>(instructions);
        newInstructions[1] = memoryA;
        newInstructions[2] = memoryB;
        int i = 0;
        while (i < newInstructions.Count)
        {
            int instruction = newInstructions[i];
            if (instruction == 1)
            {
                newInstructions[newInstructions[i + 3]] = newInstructions[newInstructions[i + 1]] + newInstructions[newInstructions[i + 2]];
            }
            else if (instruction == 2)
            {
                newInstructions[newInstructions[i + 3]] = newInstructions[newInstructions[i + 1]] * newInstructions[newInstructions[i + 2]];
            }
            else if (instruction == 99)
            {
                break;
            }
            i += 4;
        }
        return newInstructions;
    }
    
    public static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        string[] numStrings = File.ReadAllLines(filePath)[0].Split(",");
        List<int> instructions = new List<int>();
        foreach (string l in numStrings)
        {
            instructions.Add(Convert.ToInt32(l));
        }


        Console.WriteLine($"Part 1: {RunProgram(instructions,12, 2)[0]}");
        int targetAnswer = 19690720;
        for (int x = 0; x < 100; x++){
            for (int y = 0; y < 100; y++){
                if (RunProgram(instructions, x, y)[0] == targetAnswer){
                    Console.WriteLine($"Part 2: {100 * x + y}");
                }
            }
        }
        stopwatch.Stop();
        TimeSpan elapsed = stopwatch.Elapsed;
        Console.WriteLine($"Time: {elapsed.Minutes}:{elapsed.Seconds}.{elapsed.Milliseconds}:{elapsed.Nanoseconds}");
    }
}