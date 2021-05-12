using System;

namespace Stack
{
    class Program
    {
        // Create a stack

        public class Node
        {
            public int value;
            public Node next;
        }

        public class Stack
        {
            public Node head;
            public int count;

            public Stack(int val)
            {
                var newNode = new Node();
                newNode.value = val;
                newNode.next = null;
                head = newNode;
                count = 1;
            }

            public void Push(int val)
            {
                count++;

                var newNode = new Node();
                newNode.value = val;
                newNode.next = head;
                head = newNode;
            }

            public void Pop()
            {
                if (count == 0)
                {
                    Console.WriteLine("Stack is empty.");
                    return;
                }

                head = head.next;

                count--;
            }

            public int Length()
            {
                return count;
            }

            public void Print()
            {
                Node current = head;
                while(current != null)
                {
                    Console.WriteLine(current.value);
                    current = current.next;
                }
            }
        }
        static void Main(string[] args)
        {
            var stack = new Stack(0);
        }
    }
}
