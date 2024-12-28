using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
namespace AOC2015Day1{
    class Day1{
        public static void Main(){
            string filePath = Path.Combine(Directory.GetCurrentDirectory(),"input.txt");

            string[] lines = File.ReadAllLines(filePath);
            foreach(string line in lines){
                Console.WriteLine(line);
            }
        }
    }
}