using System.Diagnostics;

/*
hello for part two to work just go into your input data and change the line that says
NUMBER -> b
to this
PART1ANSWER -> b
and run the code again
*/
namespace AOC2015.Day7;
class Day7
{
    public static bool IsDigit(string x){
        return x.All(char.IsDigit);
    }
    public static void Main()
    {
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        string[] lines = File.ReadAllLines(filePath);
        List<Wire> wires = new List<Wire>();
        Dictionary<string, int> wireDict = new Dictionary<string, int>();
        foreach (string l in lines)
        {
            string z = "";
            WireType currentType = WireType.AND;
            string[] typeSplit = [];
            if (l.Contains("NOT"))
            {
                currentType = WireType.NOT;
                typeSplit = l.Split("NOT ");
            }
            else if (l.Contains("AND"))
            {
                currentType = WireType.AND;
                typeSplit = l.Split(" AND ");
            }
            else if (l.Contains("OR"))
            {
                currentType = WireType.OR;
                typeSplit = l.Split(" OR ");
            }
            else if (l.Contains("LSHIFT"))
            {
                currentType = WireType.LSHIFT;
                typeSplit = l.Split(" LSHIFT ");
            }
            else if (l.Contains("RSHIFT"))
            {
                currentType = WireType.RSHIFT;
                typeSplit = l.Split(" RSHIFT ");
            }
            else
            {
                currentType = WireType.SET;
                typeSplit = ["", l];
            }
            string[] wireSplit = typeSplit[1].Split(" -> ");
            string xString = typeSplit[0];
            string yString = wireSplit[0];
            string zString = wireSplit[1];
            object x;
            if (IsDigit(xString) && xString != "")
                x = Convert.ToInt32(xString);
            else
                x = xString;

            //just making them bools so they arent ints or strings which are the types we use
            //terrible method but shh noone needs to know
            //this is the null value
            object y;
            if (IsDigit(yString) && yString != "")
                y = Convert.ToInt32(yString);
            else
                y = yString;

            z = zString;
            wires.Add(new Wire(currentType, x, y, z));

        }
        foreach (Wire wire in wires)
        {
            Console.Write($"{wire.type} | {wire.x} | {wire.y} | {wire.z}\n");
        }

        List<Wire> currentWires = new List<Wire>(wires);

        while (currentWires.Count > 0)
        {
            List<Wire> tempWires = new List<Wire>(currentWires);
            foreach (Wire wire in currentWires)
            {
                if ((wire.x is string && !wireDict.ContainsKey((string) wire.x) && (string) wire.x != "") || (wire.y is string && !wireDict.ContainsKey((string) wire.y) && (string) wire.y != ""))
                    continue;
                int newX = -1;
                if (!(wire.x is string && (string) wire.x == ""))
                    newX = wire.x is int intValueX ? intValueX : wireDict[(string)wire.x];
                int newY = -1;
                if (!(wire.y is string && (string) wire.y == ""))
                    newY = wire.y is int intValueY ? intValueY : wireDict[(string)wire.y];
                if (wire.type == WireType.SET)
                {
                    if (!wireDict.ContainsKey(wire.z))
                        wireDict.Add(wire.z, 0);

                    wireDict[wire.z] = newY;
                }else if (wire.type == WireType.NOT)
                {
                    if (!wireDict.ContainsKey(wire.z))
                        wireDict.Add(wire.z, 0);

                    wireDict[wire.z] = ~newY;
                }else if (wire.type == WireType.AND)
                {
                    if (!wireDict.ContainsKey(wire.z))
                        wireDict.Add(wire.z, 0);

                    wireDict[wire.z] = newX & newY;
                }else if (wire.type == WireType.OR)
                {
                    if (!wireDict.ContainsKey(wire.z))
                        wireDict.Add(wire.z, 0);

                    wireDict[wire.z] = newX | newY;
                }else if (wire.type == WireType.LSHIFT)
                {
                    if (!wireDict.ContainsKey(wire.z))
                        wireDict.Add(wire.z, 0);

                    wireDict[wire.z] = newX << newY;
                }else if (wire.type == WireType.RSHIFT)
                {
                    if (!wireDict.ContainsKey(wire.z))
                        wireDict.Add(wire.z, 0);

                    wireDict[wire.z] = newX >> newY;
                }
                tempWires.Remove(wire);
            }

            currentWires = new List<Wire>(tempWires);
            Console.WriteLine(currentWires.Count);
        }

        Console.WriteLine($"Part 1: {wireDict["a"]}");
        stopwatch.Stop();
        TimeSpan elapsed = stopwatch.Elapsed;
        Console.WriteLine($"Time: {elapsed.Minutes}:{elapsed.Seconds}.{elapsed.Milliseconds}:{elapsed.Nanoseconds}");
    }
}

public enum WireType { AND, OR, NOT, LSHIFT, RSHIFT, SET }
public struct Wire
{
    public WireType type;
    public object x;
    public object y;
    public string z;
    public Wire(WireType type, object x, object y, string z)
    {
        this.type = type;
        this.x = x;
        this.y = y;
        this.z = z;
    }
}