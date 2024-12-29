using System.Diagnostics;

namespace AOC2019.Day5;
/*
the following code is an abomination
but hey- it works.
*/
class Day5
{
    public static int RunProgram(List<int> instructions, int input, bool partTwo = false)
    {
        List<int> newInstructions = new List<int>(instructions);
        int output = -1;
        int i = 0;
        while (i < newInstructions.Count)
        {
            int instruction = newInstructions[i];
            List<char> digitStrings = instruction.ToString().ToCharArray().ToList();
            List<int> digits = new List<int>();
            digitStrings.Reverse();
            foreach (char digit in digitStrings){
                digits.Add(Convert.ToInt32(digit.ToString()));
            }
            int opcode;
            if (digits.Count > 1){
                opcode = Convert.ToInt32(digits[1].ToString() + digits[0].ToString());
                digits.RemoveAt(0);
                digits.RemoveAt(0);
            }
            else{
                opcode = digits[0];
                digits.RemoveAt(0);
            }
            if (opcode == 99){
                break;
            }
            List<int> parameters = [newInstructions[i+1], newInstructions[i+2], newInstructions[i+3]];
            for (int p = 0; p < parameters.Count; p++){
                if (parameters[p] < 0)
                    continue;
                if (parameters[p] > newInstructions.Count)
                    continue;
                
                if (p > digits.Count - 1){
                    parameters[p] = newInstructions[parameters[p]];
                }else if (digits[p] == 0){
                    parameters[p] = newInstructions[parameters[p]];
                }
            }
            if (opcode == 1)
            {
                newInstructions[newInstructions[i+3]] = parameters[0] + parameters[1];
                i += 4;
            }
            else if (opcode == 2)
            {
                newInstructions[newInstructions[i+3]] = parameters[0] * parameters[1];
                i += 4;
            }else if (opcode == 3)
            {
                newInstructions[newInstructions[i+1]] = input;
                i += 2;
            }else if (opcode == 4)
            {
                output = parameters[0];
                i += 2;
            }
            else if (opcode == 99)
            {
                break;
            }

            if (!partTwo)
                continue;
            if (opcode == 5){
                if (parameters[0] != 0){
                    i = parameters[1];
                }else
                    i += 3;
            }else if (opcode == 6){
                if (parameters[0] == 0){
                    i = parameters[1];
                }else
                    i += 3;
            }else if (opcode == 7){
                if (parameters[0] < parameters[1])
                    newInstructions[newInstructions[i+3]] = 1;
                else
                    newInstructions[newInstructions[i+3]] = 0;
                i += 4;
            }else if (opcode == 8){
                if (parameters[0] == parameters[1])
                    newInstructions[newInstructions[i+3]] = 1;
                else
                    newInstructions[newInstructions[i+3]] = 0;
                i += 4;
            }
        }
        return output;
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


        Console.WriteLine($"Part 1: {RunProgram(instructions,1)}");
        Console.WriteLine($"Part 2: {RunProgram(instructions,5, true)}");
        stopwatch.Stop();
        TimeSpan elapsed = stopwatch.Elapsed;
        Console.WriteLine($"Time: {elapsed.Minutes}:{elapsed.Seconds}.{elapsed.Milliseconds}:{elapsed.Nanoseconds}");
    }
}