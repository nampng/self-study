using System;

namespace CircularArray
{
    class Program
    {
        public class Circle
        {
            public int[] array;
            public int front;
            public int back;
            public int size;
            public int count;
            public Circle(int x)
            {
                array = new int[x];
                front = 0;
                back = 0;
                count = 0;
                size = x;
            }

            public void Enqueue(int value)
            {
                if (count == size)
                {
                    Console.WriteLine("Queue is full");
                    return;
                }

                Console.WriteLine("Inserting " + value + " at " + back);
                array[back] = value;
                back++;
                count++;

                if (back >= size)
                {
                    back = 0;
                }

                Console.WriteLine("Back is: " + back);
            }

            public void Dequeue()
            {
                if(count == 0)
                {
                    Console.WriteLine("Queue is empty.");
                    return;
                }

                Console.WriteLine("Removing " + array[front] + " at " + front);

                front++;

                if (front == size)
                {
                    front = 0;
                }

                Console.WriteLine("Front is: " + front);
                count--;
            }

            public void Iterate()
            {
                int current = front;
                while(true)
                {
                    Console.WriteLine("Value: " + array[current]);

                    current++;

                    if (current == size)
                    {
                        current = 0;
                    }

                    if (current == back)
                    {
                        break;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            Circle circle = new Circle(5);
            Console.WriteLine("Filling queue...");
            circle.Enqueue(0);
            circle.Enqueue(1);
            circle.Enqueue(2);
            circle.Enqueue(3);
            circle.Enqueue(4);
            circle.Iterate();
            Console.WriteLine("Dequeuing...");
            circle.Dequeue();
            circle.Iterate();
            circle.Dequeue();
            circle.Iterate();
            Console.WriteLine("Filling...");
            circle.Enqueue(5);
            circle.Enqueue(6);
            circle.Iterate();
            circle.Enqueue(999);
            Console.WriteLine("Freestyle");
            circle.Dequeue();
            circle.Dequeue();
            circle.Dequeue();
            circle.Dequeue();
            circle.Dequeue();
            circle.Dequeue();
            circle.Dequeue();
            circle.Enqueue(8321);
            circle.Enqueue(777);
            circle.Enqueue(3123);
            circle.Enqueue(1010);
            circle.Enqueue(444);
            circle.Enqueue(8888);
            circle.Iterate();
        }
    }
}
