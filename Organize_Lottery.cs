using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace organize_lottery
{
    public class Organize_Lottery
    {
        static Random r = new Random();

        static void Main(string[] args)
        {
            string[] nm = Console.ReadLine().Split(' ');

            int n = Convert.ToInt32(nm[0]);
            int m = Convert.ToInt32(nm[1]);

            List<int> segmentStarts = new List<int>();
            List<int> segmentEnds = new List<int>();

            for(int i = 1; i <= n; i++)
            {
                string[] segment = Console.ReadLine().Split(' ');
                segmentStarts.Add(Convert.ToInt32(segment[0]));
                segmentEnds.Add(Convert.ToInt32(segment[1]));
            }

            string[] pointsS = Console.ReadLine().Split(' ');

            List<int> points = new List<int>();
            
            for(int i = 0; i < m; i++)
            {
                points.Add(Convert.ToInt32(pointsS[i]));
            }

            List<int> counts = FastCountSegments(segmentStarts, segmentEnds, points);

            foreach(int count in counts)
            {
                Console.Write(count + " ");
            }
            //Console.ReadLine();
        }

        public static List<int> FastCountSegments(List<int> starts, List<int> ends, List<int> points)
        {
            var counts = new List<int>();

            string END = "END";
            string START = "START";
            string POINT = "POINT";

            List<Tuple<int, string>> collection = new List<Tuple<int, string>>();
            foreach(var p in points)
            {
                collection.Add(new Tuple<int, string>(p, POINT));
            }

            for (int i = 0; i < ends.Count; i++)
            {
                collection.Add(new Tuple<int, string>(starts[i], START));
                collection.Add(new Tuple<int, string>(ends[i], END));
            }

            collection.Sort(new LottoComparer());

            int startCount = 0;
            var countByPoint = new Dictionary<int, int>();

            foreach(var entry in collection)
            {
                if(entry.Item2 == START)
                {
                    startCount++;
                    continue;
                }
                if(entry.Item2 == END)
                {
                    startCount--;
                    continue;
                }
                if(entry.Item2 == POINT)
                {
                    if(!countByPoint.ContainsKey(entry.Item1))
                    {
                        countByPoint.Add(entry.Item1, startCount);
                        continue;
                    }
                }
            }

            foreach(var p in points)
            {
                counts.Add(countByPoint[p]);
            }

            return counts;
        }

        public static List<int> NaiveCountSegments(List<int> starts, List<int> ends, List<int> points)
        {
            List<int> counts = new List<int>();

            foreach(var point in points)
            {
                counts.Add(0);
            }

            for(int i = 0; i < points.Count; i++)
            {
                for (int y = 0; y < starts.Count; y++)
                {
                    if(starts[y] <= points[i] && points[i] <= ends[y])
                    {
                        counts[i] += 1;
                    }
                }
            }

            return counts;
        }
    }

    class LottoComparer : IComparer<Tuple<int, string>>
    {
        string END = "END";
        string START = "START";
        string POINT = "POINT";

        public int Compare(Tuple<int, string> x, Tuple<int, string> y)
        {
            if(x == null)
            {
                if (y == null)
                {
                    return 0;
                }
                else
                {
                    return -1;
                }
            }
            else
            {
                if (y == null)
                {
                    return 1;
                }
                else
                {
                    if(x.Item1 > y.Item1)
                    {
                        return 1;
                    }
                    
                    if(x.Item1 < y.Item1)
                    {
                        return -1;
                    }

                    if(x.Item1 == y.Item1)
                    {
                        if(x.Item2 == START && y.Item2 == END)
                        {
                            return -1;
                        }

                        if(x.Item2 == START && y.Item2 == POINT)
                        {
                            return -1;
                        }

                        if(x.Item2 == POINT && y.Item2 == END)
                        {
                            return -1;
                        }

                        if(x.Item2 == POINT && y.Item2 == START)
                        {
                            return 1;
                        }

                        if (x.Item2 == END && y.Item2 == POINT)
                        {
                            return 1;
                        }

                        if(x.Item2 == END && y.Item2 == START)
                        {
                            return 1;
                        }

                        return 0;
                    }

                    return 0;
                }
            }
        }
    }

}
