using System;

namespace BinarySearchTree
{
    class Program
    {
        public class Node
        {
            public int value;
            public Node right;
            public Node left;
        }
        public class BST
        {
            public Node root;

            public BST(int rootValue)
            {
                root = new Node();
                root.value = rootValue;
            }

            public Node Insert(int value, Node current)
            {
                if(current == null)
                {
                    Console.WriteLine("Empty spot found. Inserting value: " + value);
                    Node newNode = new Node();
                    newNode.value = value;
                    current = newNode;
                }

                if (value > current.value)
                {
                    Console.WriteLine("Moving right.");
                    current.right = Insert(value, current.right);
                }
                else if (value < current.value)
                {
                    Console.WriteLine("Moving left.");
                    current.left = Insert(value, current.left);
                }

                return current;
            }

            public void Search(int value, Node current)
            {
                if (current == null)
                {
                    Console.WriteLine("Value DNE.");
                    return;
                }

                if (value == current.value)
                {
                    Console.WriteLine("Value found!");
                    return;
                }

                if (value > current.value)
                {
                    Console.WriteLine("Searching right.");
                    Search(value, current.right);
                }
                else if (value < current.value)
                {
                    Console.WriteLine("Searching left.");
                    Search(value, current.left);
                }
            }
        }
        static void Main(string[] args)
        {
            BST tree = new BST(30);
            tree.Insert(25, tree.root);
            tree.Insert(42, tree.root);
            tree.Insert(38, tree.root);
            tree.Insert(47, tree.root);
            tree.Insert(2, tree.root);
            tree.Insert(28, tree.root);
            tree.Insert(1, tree.root);
            tree.Insert(29, tree.root);
            tree.Insert(100, tree.root);
            tree.Insert(43, tree.root);

            tree.Search(2, tree.root);
            tree.Search(30, tree.root);
            tree.Search(999, tree.root);
        }
    }
}
