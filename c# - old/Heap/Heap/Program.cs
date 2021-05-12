using System;

namespace Heap
{
    class Program
    {
        public class Heap
        {
            public int[] data;
            public int last;

            public Heap(int size)
            {
                data = new int[size];
                last = 0;
            }

            public void Insert(int value)
            {
                if(last != data.Length - 1)
                {
                    Console.WriteLine("Inserting value: " + value);
                    data[last] = value;
                    FixUp(data, last);
                    last++;
                }
                else
                {
                    Console.WriteLine("Heap is full.");
                    return;
                }
            }

            public int DeleteMax()
            {
                if (last == 0)
                {
                    Console.WriteLine("Heap is empty.");
                    return -1;
                }

                int max = data[0];
                data[0] = data[last - 1];

                Console.WriteLine("Swapped old root, " + max + ", with: " + data[0]);

                FixDown(data, last - 2, 0);
                last--;

                Console.WriteLine("New root is now: " + data[0]);

                return max;
            }

            public void FixUp(int[] data, int i)
            {
                while(i != 0)
                {
                    if(data[FindParent(i)] < data[i])
                    {
                        int temp = data[FindParent(i)];
                        data[FindParent(i)] = data[i];
                        data[i] = temp;
                        i = FindParent(i);
                    }
                    else
                    {
                        break;
                    }
                }
            }

            public void FixDown(int[] data, int lastIndex, int i)
            {
                while(lastIndex >= FindLeftChild(i))
                {
                    Console.WriteLine("Last index is at: " + lastIndex);
                    Console.WriteLine("Left child is at: " + FindLeftChild(i));
                    if(lastIndex == FindLeftChild(i))
                    {
                        Console.WriteLine("Last node found.");
                        Console.WriteLine("Checking if " + data[i] + " is less than " + data[lastIndex]);
                        if(data[i] < data[FindLeftChild(i)])
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

                        if(data[i] <= data[FindLeftChild(i)] || data[i] < data[FindLeftChild(i) + 1])
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

            public int FindParent(int i)
            {
                return (i - 2) / 2;
            }

            public int FindLeftChild(int i)
            {
                return i * 2 + 1;
            }

            public void Peek()
            {
                if (last == 0)
                {
                    Console.WriteLine("Empty.");
                }
                else
                {
                    Console.WriteLine("Root is: " + data[0]);
                    return;
                }
                
            }
        }
        static void Main(string[] args)
        {
            var heap = new Heap(10);
            var rand = new Random();
            heap.Insert(rand.Next(1, 100));
            heap.Insert(rand.Next(1, 100));
            heap.Insert(rand.Next(1, 100));
            heap.Insert(rand.Next(1, 100));
            heap.Insert(rand.Next(1, 100));
            heap.DeleteMax();
        }
    }
}
