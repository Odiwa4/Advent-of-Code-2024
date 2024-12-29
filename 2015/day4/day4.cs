using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using System.Numerics;
using System.Security.Cryptography;
using System.Text;
namespace AOC2015.Day4;
/*
bit of a brute force method but it works so... its good i guess
*/
class Day4
{
    public static void Main()
    {
        string filePath = Path.Combine(Directory.GetCurrentDirectory(), "input.txt");
        string input = File.ReadAllLines(filePath)[0];
        int partOneAnswer = -1;
        for (int i = 0; i < 100000000; i++){
            using (MD5 md5 = MD5.Create()){
                byte[] inputBytes = Encoding.UTF8.GetBytes(input + i.ToString());
                byte[] hashBytes = md5.ComputeHash(inputBytes);
                StringBuilder sb = new StringBuilder();
                foreach (byte b in hashBytes)
                {
                    sb.Append(b.ToString("x2"));
                }
                if (sb.ToString().Substring(0, 5) == "00000" && partOneAnswer == -1){
                    partOneAnswer = i;
                }

                if (sb.ToString().Substring(0, 6) == "000000"){
                    Console.WriteLine($"Part 1: {partOneAnswer}");
                    Console.WriteLine($"Part 2: {i}");
                    break;
                }
            }
        }
    }
}