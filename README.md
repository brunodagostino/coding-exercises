# coding-exercises
 These solutions are written in Python and the analysis of the algorithms have been made using the Big O Notation. #brunodagostino


## Topic | Arrays & Strings
### A Very Big Sum
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

### Designer PDF Viewer
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently.

There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

### Left Rotation
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

### Reverse Words in a String
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


## Topic | Lists
### Insert a Node at a Position Given in a List
Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its data attribute, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.

### Cycle Detection
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1. Otherwise, return 0.


## Topic | Stacks & Queues
### Balanced Brackets
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

    - It contains no unmatched brackets.
    - The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.

Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

### Queue Using Two Stacks
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

    - Enqueue: add a new element to the end of the queue.
    - Dequeue: remove the element from the front of the queue and return it.

In this challenge, you must first implement a queue using two stacks. Then process q queries, where each query is one of the following 3 types:

    1: Enqueue element x into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.


## Topic | Hash & Maps
### Ice Cream Parlor
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example. m = 6  cost = [1, 3, 4, 5, 6]
The two flavors that cost 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.

### Colorful Number
Given a number, find out whether it's colorful or not.

When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number.


## Topic | Sorting Algorithms
### Insertion Sort
In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.

### Quicksort
When partition is called on an array, two parts of the array get 'sorted' with respect to each other. If partition is then called on each sub-array, the array will now be split into four parts. This process can be repeated until the sub-arrays are small. Notice that when partition is called on just one of the numbers, they end up being sorted.

Can you repeatedly call partition so that the entire array ends up sorted?

In this challenge, print your array every time your partitioning method finishes, i.e. whenever two subarrays, along with the pivot, are merged together.

    - The first element in a sub-array should be used as a pivot.
    - Partition the left side before partitioning the right side.
    - The pivot should be placed between sub-arrays while merging them.
    - Array of length  or less will be considered sorted, and there is no need to sort or to print them.


## Topic | Trees
### Binary Tree Insertion
You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the values into their appropriate position in the binary search tree and return the root of the updated binary tree.

### Height of a Binary Tree
The height of a binary tree is the number of edges between the tree's root and its furthest leaf.

The Height of binary tree with single node is taken as zero.

Node values are inserted into a binary search tree before a reference to the tree's root node is passed to your function. In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value.

### QHeap
Basic heap operations.

There are 3 types of query:

    - "1 v" - Add an element v to the heap.
    - "2 v" - Delete the element v from the heap.
    - "3" - Print the minimum of all the elements in the heap.
    
NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.


## Topic | Graphs (BFS & DFS)
### Breath First Search
Consider an undirected graph where each edge weighs 6 units. Each of the nodes is labeled consecutively from 1 to n.

You will be given a number of queries. For each query, you will be given a list of edges describing an undirected graph. After you create a representation of the graph, you must determine and report the shortest distance to each of the other nodes from a given starting position using the breadth-first search algorithm (BFS). Return an array of distances from the start node in node number order. If a node is unreachable, return -1 for that node.