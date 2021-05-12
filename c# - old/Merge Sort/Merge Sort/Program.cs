using System;

namespace Merge_Sort
{
    class Program
    {
        public class RandArray
        {
            public int[] data;

            public RandArray(int size)
            {
                var rand = new Random();
                data = new int[size];
                for(int i = 0; i < size; i++)
                {
                    data[i] = rand.Next(0,100);
                }
            }

            public void Print()
            {
                for(int i = 0; i < data.Length; i++)
                {
                    Console.Write(data[i] + " ");
                }

                Console.Write(Environment.NewLine);
            }
        }

        static void Main(string[] args)
        {
            var arr = new RandArray(15);
            Console.WriteLine("Before sort:");
            arr.Print();
            MergeSort(arr.data);
            Console.WriteLine("Sorted:");
            arr.Print();
        }

        public static void MergeSort(int[] arr)
        {
            if(arr.Length > 1)
            {

                int mid = arr.Length / 2;

                int[] left = new int[mid];
                int[] right = new int[arr.Length - mid];

                for (int i = 0; i < left.Length; i++)
                {
                    left[i] = arr[i];
                }

                for (int i = 0; i < right.Length; i++)
                {
                    right[i] = arr[mid + i];
                }

                MergeSort(left);
                MergeSort(right);

                int leftHead = 0;
                int rightHead = 0;
                int index = 0;

                while (leftHead < left.Length && rightHead < right.Length)
                {
                    if (left[leftHead] < right[rightHead])
                    {
                        arr[index] = left[leftHead];
                        leftHead++;
                    }
                    else
                    {
                        arr[index] = right[rightHead];
                        rightHead++;
                    }

                    index++;
                }

                while (leftHead < left.Length)
                {
                    arr[index] = left[leftHead];
                    leftHead++;
                    index++;
                }

                while (rightHead < right.Length)
                {
                    arr[index] = right[rightHead];
                    rightHead++;
                    index++;
                }
            }
        }
    }
}
