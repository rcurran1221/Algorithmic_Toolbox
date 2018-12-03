using Microsoft.VisualStudio.TestTools.UnitTesting;
using organize_lottery;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace organize_lottery.Tests
{
    [TestClass()]
    public class Organize_LotteryTests
    {
        static Random r = new Random();
        const int Min = -100000000;
        const int Max = 100000001;

        [TestMethod()]
        public void StressTest()
        {
            var random = new Random();

            for (int i = 0; i < 1; i++)
            {
                var points = GeneratePoints(r.Next(1, 50001));
                var starts = GenerateStarts(r.Next(1, 50001));
                var ends = GenerateEnds(starts);

                var naiveResult = Organize_Lottery.NaiveCountSegments(starts, ends, points);

                var stopwatch = new Stopwatch();
                stopwatch.Start();
                var fastResult = Organize_Lottery.FastCountSegments(starts, ends, points);
                stopwatch.Stop();

                Assert.AreEqual(naiveResult.Count, fastResult.Count);
                Assert.IsTrue(stopwatch.ElapsedMilliseconds / 1000F < 5F);

                for(int x = 0; x < naiveResult.Count; x++)
                {
                    int n = naiveResult[x];
                    int f = fastResult[x];
                    Assert.AreEqual(n, f, x + " " + i);
                }
            }
        }

        [TestMethod()]
        public void StressTestDebug()
        {
            var random = new Random();

            for (int i = 0; i < 100000; i++)
            {
                var points = GeneratePoints(r.Next(1, 51),-1000, 1001);
                var starts = GenerateStarts(r.Next(1, 51), -1000, 1001);
                var ends = GenerateEnds(starts, 1001);

                var naiveResult = Organize_Lottery.NaiveCountSegments(starts, ends, points);
                var fastResult = Organize_Lottery.FastCountSegments(starts, ends, points);

                Assert.AreEqual(naiveResult.Count, fastResult.Count);
                for (int x = 0; x < naiveResult.Count; x++)
                {
                    int n = naiveResult[x];
                    int f = fastResult[x];
                    Assert.AreEqual(n, f, x + " " + i);
                }

            }
        }

        static List<int> GeneratePoints(int count, int min = Min, int max = Max)
        {
            var points = new List<int>();

            while (points.Count < count)
            {
                points.Add(r.Next(min, max));
            }

            return points;
        }

        static List<int> GenerateStarts(int count, int min = Min, int max = Max)
        {
            var starts = new List<int>();

            for (int i = 0; i < count; i++)
            {
                starts.Add(r.Next(min, max));
            }

            return starts;
        }

        static List<int> GenerateEnds(List<int> starts, int max = Max)
        {
            var ends = new List<int>();

            foreach (var start in starts)
            {
                ends.Add(r.Next(start, max));
            }

            return ends;
        }
    }
}