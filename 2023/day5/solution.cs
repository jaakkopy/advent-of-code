using System.Collections.Generic;
using System;
using System.Linq;

public class Node {
    public long DestStart {get; set;}
    public long SrcStart {get; set;}
    public long Length {get; set;}
    public Node Left {get; set;} = null;
    public Node Right {get; set;} = null;

    public Node(long destStart, long srcStart, long length) {
        this.DestStart = destStart;
        this.SrcStart = srcStart;
        this.Length = length;
    }
}

// Use binary trees for faster lookup of ranges
public class BinTree {
    private Node root = null;

    public void AddNode(long destStart, long srcStart, long length) {
        if (this.root == null) {
            this.root = new Node(destStart, srcStart, length);
            return;
        }
        Node r = this.root;
        Node parent = r;
        while (r != null) {
            parent = r;
            if (srcStart <= r.SrcStart) {
                r = r.Left;
            } else {
                r = r.Right;
            }
        }
        Node n = new Node(destStart, srcStart, length);
        if (srcStart <= parent.SrcStart) {
            parent.Left = n;
        } else {
            parent.Right = n; 
        }
    }

    public long FindRangeValue(long value) {
        Node r = this.root;
        while (r != null) {
            if (value >= r.SrcStart && value <= r.SrcStart + r.Length) {
                return r.DestStart + (value - r.SrcStart);
            } else if (value < r.SrcStart) {
                r = r.Left;
            } else {
                r = r.Right;
            }
        }
        return value;
    }
}

public class Solution
{
    public static List<string> ReadLines() {
        List<string> lines = new List<string>();
        string line;
        while ((line = Console.ReadLine()) != null)
            lines.Add(line);
        return lines;
    }

    // Read each map in reversed order (e.g seed->soil becomes soil->seed)
    public static List<BinTree> ReadMapsToBinTrees(List<string> lines) {
        List<BinTree> trees = new List<BinTree>();
        int i = 2;
        int lc = lines.Count;
        while (i < lc) {
            BinTree t = new BinTree();
            int j = i + 1;
            while (j < lc && lines.ElementAt(j).Length > 0) {
                List<long> destSrcRange = lines.ElementAt(j).Split().ToList().ConvertAll(long.Parse);
                t.AddNode(destSrcRange[1], destSrcRange[0], destSrcRange[2]);
                ++j;
            }
            trees.Add(t);
            if (j != i + 1)
                i = j;
            ++i;
        }
        return trees;
    }

    // Check if the seed exists. If exact is true, only exact matches count. If exact is false, check ranges of seeds
    public static bool seedExists(List<long> initalSeeds, long seed, bool exact) {
        for (int i = 0; i < initalSeeds.Count - 1; i += 2) {
            if (exact) {
                if (initalSeeds[i] == seed || initalSeeds[i+1] == seed)
                    return true;
            }
            else if (seed >= initalSeeds[i] && seed <= initalSeeds[i] + initalSeeds[i+1] - 1)
                return true;
        }
        return false;
    }

    // Begin from location 0 and advance upward until a seed matching the location is found
    // (kind of slow)
    public static long FindMinimumLocation(List<BinTree> trees, List<long> initalSeeds, bool exact) {
        long location = 0;
        while (true) {
            long key = location;
            for (int mapTree = trees.Count - 1; mapTree >= 0; --mapTree) {
                key = trees.ElementAt(mapTree).FindRangeValue(key);
            }
            if (seedExists(initalSeeds, key, exact))
                return location;
            ++location;
        }
    }

    public static void Main()
    {
        List<string> lines = ReadLines();
        List<long> initalSeeds = lines.ElementAt(0).Substring(7).Split().ToList().ConvertAll(long.Parse);
        var trees = ReadMapsToBinTrees(lines); 
        Console.WriteLine(FindMinimumLocation(trees, initalSeeds, true));  // Part 1
        Console.WriteLine(FindMinimumLocation(trees, initalSeeds, false)); // Part 2
    }
}
