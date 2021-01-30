using System;

namespace HeapSort
{
    class Program
    {
        public class DataSet
        {
            int[] array;

            public DataSet(int x)
            {
                var rand = new Random();
                array = new int[x];
                for (int i = 0; i < array.Length; i++)
                {
                    array[i] = rand.Next(1, 100);
                    Console.WriteLine(array[i]);
                }
            }

            public void Heapify()
            {
                for (int i = array.Length - 1; i >= 0; i--)
                {
                    FixDown(array, array.Length - 1, i);
                }
            }

            public void FixDown(int[] data, int lastIndex, int i)
            {
                while (lastIndex >= FindLeftChild(i))
                {
                    Console.WriteLine("Last index is at: " + lastIndex);
                    Console.WriteLine("Left child is at: " + FindLeftChild(i));
                    if (lastIndex == FindLeftChild(i))
                    {
                        Console.WriteLine("Last node found.");
                        Console.WriteLine("Checking if " + data[i] + " is less than " + data[lastIndex]);
                        if (data[i] < data[FindLeftChild(i)])
                        {
                            Console.WriteLine("Swapping");
                            int temp = data[i];
                            data[i] = data[FindLeftChild(i)];
                            data[FindLeftChild(i)] = temp;
                        }

                        return;
                    }
                    else
                    {
                        Console.WriteLine("Comparing " + data[i] + " to:");
                        Console.WriteLine("Left child: " + data[FindLeftChild(i)]);
                        Console.WriteLine("Right child: " + data[FindLeftChild(i) + 1]);

                        if (data[i] <= data[FindLeftChild(i)] || data[i] < data[FindLeftChild(i) + 1])
                        {
                            if (data[FindLeftChild(i)] > data[FindLeftChild(i) + 1])
                            {
                                Console.WriteLine("Swapping with left.");

                                int temp = data[i];
                                data[i] = data[FindLeftChild(i)];
                                data[FindLeftChild(i)] = temp;

                                i = FindLeftChild(i);
                            }
                            else
                            {
                                Console.WriteLine("Swapping with right.");

                                int temp = data[i];
                                data[i] = data[FindLeftChild(i) + 1];
                                data[FindLeftChild(i) + 1] = temp;

                                i = FindLeftChild(i) + 1;
                            }
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }

            public static int FindParent(int i)
            {
                return (i - 2) / 2;
            }

            public static int FindLeftChild(int i)
            {
                return i * 2 + 1;
            }
            public void Print()
            {
                for (int i = 0; i < array.Length; i++)
                {
                    Console.WriteLine(array[i]);
                }
            }

            public void HeapSort()
            {
                for(int i = array.Length - 1; i > 0;)
                {
                    int temp = array[0];
                    array[0] = array[i];
                    array[i] = temp;

                    i--;

                    FixDown(array, i, 0);
                }
            }
        }
        static void Main(string[] args)
        {
            var data = new DataSet(10);
            data.Heapify();
            data.Print();
            data.HeapSort();
            data.Print();
        }
    }
}
