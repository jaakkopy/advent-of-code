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

// Use binary trees for fast lookup of ranges
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
        {
            lines.Add(line);
        }
        return lines;
    }

    // Each map (seed->soil etc) has its own binary tree in a list
    public static List<BinTree> ReadMapsToBinTrees(List<string> lines) {
        List<BinTree> trees = new List<BinTree>();
        int i = 2;
        int lc = lines.Count;
        while (i < lc) {
            BinTree t = new BinTree();
            int j = i + 1;
            while (j < lc && lines.ElementAt(j).Length > 0) {
                List<long> destSrcRange = lines.ElementAt(j).Split().ToList().ConvertAll(long.Parse);
                t.AddNode(destSrcRange[0], destSrcRange[1], destSrcRange[2]);
                ++j;
            }
            trees.Add(t);
            if (j != i + 1)
                i = j;
            ++i;
        }
        return trees;
    }

    public static long FindMinimumLocation(List<long> intialSeeds, List<BinTree> trees) {
        long min = -1;
        foreach (var s in intialSeeds) {
            long key = s;
            for (int mapTree = 0; mapTree < trees.Count; ++mapTree) {
                key = trees.ElementAt(mapTree).FindRangeValue(key);
            }
            if (min == -1 || key < min) {
                min = key;
            }
        }
        return min;
    }

    public static void Main()
    {
        List<string> lines = ReadLines();
        List<long> initalSeeds = lines.ElementAt(0).Substring(7).Split().ToList().ConvertAll(long.Parse);
        var trees = ReadMapsToBinTrees(lines); 
        long minLocation = FindMinimumLocation(initalSeeds, trees);
        Console.WriteLine(minLocation);
    }
}
