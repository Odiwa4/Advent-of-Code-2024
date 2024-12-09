using System;
using System.IO;
using System.Numerics;
using System.Collections;
using System.Collections.Generic;
Day6P1.Solve();

class Day6P1
{
    public static void Solve()
    {
        //string fileName = "Tday-6 input.txt";
        string filePath = @"C:\Users\olive\Documents\RCPIMWIB\ADVENT OF CODE 2024\day6\day-6 input.txt";
        string[] lines = File.ReadAllLines(filePath);

        string[,] board = new string[lines[0].Length, lines.Length];
        Vector2 startPos = new Vector2();
        List<Vector2> obstaclePos = new List<Vector2>();
        for (int y = 0; y < lines.Length; y++)
        {
            for (int x = 0; x < lines[y].Length; x++)
            {
                board[x, y] = lines[y][x].ToString();
                if (board[x, y] == "^")
                {
                    startPos = new Vector2(x, y);
                }
                else if (board[x, y] == "#")
                {
                    obstaclePos.Add(new Vector2(x, y));
                }
            }
        }

        Console.WriteLine($"Part One: {Move(startPos, board)}");
        
        List<Vector2> obstacleSpots = GetObstacleSpots(startPos, board);

        int loopCount = 0;
        foreach (Vector2 o in obstacleSpots){
            string[,] newBoard = (string[,])board.Clone();
  
            newBoard[(int) o.X, (int) o.Y] = "#";
            if (CausesLoop(startPos, newBoard, 500)){
                loopCount++;
                Console.WriteLine(o);
                continue;
            }
        }

        Console.WriteLine($"Part Two: {loopCount}");
    }
    static Vector2[] directions = [new Vector2(0, -1), new Vector2(1, 0), new Vector2(0, 1), new Vector2(-1, 0)];

    private static FinishData Step(int direction, Vector2 pos, string[,] board)
    {
        Vector2 dirVector = directions[direction];
        List<Vector2> positions = new List<Vector2>();
        bool finished = false;
        int steps = 1;
        while (finished == false)
        {
            try
            {
                Vector2 nextPos = new Vector2(pos.X + (dirVector.X * steps), pos.Y + (dirVector.Y * steps));
                if (board[(int)nextPos.X, (int)nextPos.Y] == "#")
                {
                    steps--;
                    Vector2 lastPos = new Vector2(pos.X + (dirVector.X * steps), pos.Y + (dirVector.Y * steps));
                    FinishData finishData = new FinishData();
                    finishData.finishPos = lastPos;
                    finishData.steps = steps;
                    finishData.locations = positions;
                    finishData.exited = false;
                    return finishData;
                }
                else
                {
                    steps++;
                    positions.Add(new Vector2(nextPos.X, nextPos.Y));
                }
            }
            catch (IndexOutOfRangeException)
            {
                steps--;
                Vector2 lastPos = new Vector2(pos.X + (dirVector.X * steps), pos.Y + (dirVector.Y * steps));
                FinishData finishData = new FinishData();
                finishData.finishPos = lastPos;
                finishData.steps = steps;
                finishData.locations = positions;
                finishData.exited = true;
                return finishData;
            }
        }
        return new FinishData();
    }

    private static int Move(Vector2 pos, string[,] board)
    {
        bool moved = false;
        int direction = 0;
        Vector2 lastPos = pos;
        List<Vector2> positions = new List<Vector2>();
        while (moved == false)
        {
            FinishData currentFinish = Step(direction, lastPos, board);
            foreach (Vector2 l in currentFinish.locations)
            {
                if (!positions.Contains(l))
                {
                    positions.Add(l);
                }
            }
            if (currentFinish.exited)
            {
                moved = true;
            }
            else
            {
                if (direction >= 3)
                    direction = 0;
                else
                    direction++;
                lastPos = currentFinish.finishPos;
            }
        }

        if (!positions.Contains(pos))
            positions.Add(pos);

        return positions.Count;
    }

    private static bool CausesLoop(Vector2 pos, string[,] board, int attempts)
    {
        int direction = 0;
        Vector2 lastPos = pos;
        List<Vector2> positions = new List<Vector2>();

        for (int i = 0; i < attempts; i++)
        {
            FinishData currentFinish = Step(direction, lastPos, board);

            if (currentFinish.exited)
            {
                return false;
            }
            else
            {
                if (direction >= 3)
                    direction = 0;
                else
                    direction++;
                lastPos = currentFinish.finishPos;
            }

            if (i == attempts - 1){
                return true;
            }
        }

        return false;
    }

    private static List<Vector2> GetObstacleSpots(Vector2 pos, string[,] board)
    {
        bool moved = false;
        int direction = 0;
        Vector2 lastPos = pos;
        List<Vector2> positions = new List<Vector2>();
        while (moved == false)
        {
            FinishData currentFinish = Step(direction, lastPos, board);
            foreach (Vector2 l in currentFinish.locations)
            {
                if (!positions.Contains(l))
                {
                    positions.Add(l);
                }
            }
            if (currentFinish.exited)
            {
                moved = true;
            }
            else
            {
                if (direction >= 3)
                    direction = 0;
                else
                    direction++;
                lastPos = currentFinish.finishPos;
            }
        }

        if (!positions.Contains(pos))
            positions.Add(pos);

        List<Vector2> obstacleSpots = new List<Vector2>();

        Vector2[] obstaclePosibilities = [new Vector2(0, 0), new Vector2(-1, 0), new Vector2(1, 0), new Vector2(0, -1), new Vector2(0, 1)];

        foreach (Vector2 location in positions)
        {
            foreach (Vector2 spot in obstaclePosibilities)
            {
                try
                {
                    if (!obstacleSpots.Contains(location + spot) && board[(int)location.X + (int)spot.X, (int)location.Y + (int)spot.Y] == ".")
                    {
                        obstacleSpots.Add(location + spot);
                    }
                }
                catch (IndexOutOfRangeException)
                {

                }
            }
        }
        return obstacleSpots;
    }
}

public class FinishData
{
    public List<Vector2> locations = new List<Vector2>();
    public bool exited;
    public int steps;
    public Vector2 finishPos = new Vector2(-1, -1);
}