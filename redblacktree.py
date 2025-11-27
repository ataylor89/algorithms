# ###### Introduction ######
#
# I'm watching TV and relaxing, as I said I would
#
# I did some research on red-black trees today
# They are really cool
#
# Red-black trees are fancy, and they are really hard to implement
#
# What's the point of taking all the trouble to implement a red-black tree?
#
# Well the point is that red-black trees are self balancing
#
# If you refer to bst.py, in the very same repository, you will see that the current implementation is not self-balancing
# (In the future this might change...)
#
# You have to manually call the balance() method to balance the tree
#
# But we want to write a self-balancing binary search tree, that balances itself whenever needed
#
# We don't want a binary search tree to look like 1(2(3(4))), which has four nodes and a height of four
#
# (I'm using prefix expressions / parenthetical notation to represent a binary search tree in string form)
#
# Rather, we want a binary search tree to look like 1(2)(3(4)), which has four nodes and a height of three
#
# The second binary search tree is more balanced
#
# We don't want to have to balance the first tree, in order to get it to look like the second tree
#
# We want our tree to be self-balancing, so that, every time we add a new node, the tree balances itself if needed
#
# Also, every time we delete a node, we want our tree to balance itself if needed
#
# In the red-black tree implementation, the insert() method has a helper method called insert_fix()
#
# The insert_fix() method fixes any violations of the red-black tree properties that might take place after an insertion
#
# Similarly, the delete() method has a helper method called delete_fix()
#
# The delete_fix() method fixes any violations of the red-black tree properties that might take place after a deletion
#
# There are five properties that characterize a red-black tree
#
# These properties are:
#
# (1) Every node is red or black
# (2) The root node is always black
# (3) Every NIL node is black
# (4) If a node is red, then both its children must be black
# (5) For every node, all paths from that node to a NIL node must contain the same number of black nodes
#
# It is hard to remember these properties
#
# It is even harder to remember all of the implementation details of a red-black tree
#
# Red-black trees are a very useful type of binary search tree, because they are efficient and self-balancing
#
# It is hard to design a self-balancing binary search tree... especially one that is efficient
#
# That is why red-black trees are so useful
#
# I think that... we can be less concerned with memorizing the implementation of a red-black tree... and more concerned with understanding how they work in general... since we can always look up an implementation... but it helps to have a general understanding
#
# It helps to know that red-black trees are based on the five properties listed above
#
# These properties help ensure that the red-black tree is balanced
#
# If an insertion or deletion violates any one of these properties, then the fix method reorganizes the tree so that it satisfies all of the conditions laid out in these five properties
#
# I think it helps to summarize what we have learned
#
# Red-black trees are a self-balancing type of binary search tree
#
# This means that we don't have to balance the tree manually... it balances itself automatically whenever it needs to balance itself
#
# Red-black trees are based on the five properties we described above
#
# These properties help ensure that the tree is balanced
#
# If one of these properties is violated, then the insert_fix or delete_fix methods will rebalance the tree
#
# It's nice that these methods are called at the end of the insert() and delete() methods, respectively, because it means that the tree balances itself automatically and we don't have to do it manually
#
# I want to point out a few more things before I wrap this up
#
# First of all, you might notice that the bst.py file contains a recursive implementation of a binary search tree
#
# This file, on the contrary, uses iteration more often than recursion
#
# Almost all of the methods contained in this file use iteration to accomplish their objectives
#
# At the time of writing, only the str() method uses recursion
#
# In the future, I might convert the str() method to an algorithm that uses iteration
#
# I had some difficulty finding an iterative implementation of the str() method, so I stuck with the recursive implementation that I used in bst.py, because it works, and ultimately I want an implementation that works
#
# Fortunately, I was able to find an iterative implementation of many methods, including to_list(), size(), height(), etc
#
# The advantage of recursion is that it is often easier, simpler, more elegant, and easier to commit to memory
#
# The advantage of iteration is that it is often more efficient with respect to speed and memory
#
# I like to be consistent, so it would be nice to convert the str() method to an iterative algorithm
#
# I think it's nice that the bst.py file shows how we can use recursion to implement a binary search tree, and the redblacktree.py file shows how we can use iteration to implement a binary search tree
#
# Both recursion and iteration are very useful
#
# Recursion means that a function is calling itself
#
# Iteration means that we are using a loop to repeat a set of instructions (iteration implies loops)
#
# So I think it's time to wrap things up
#
# Red-black trees are a very useful type of binary search tree, because they are efficient and self-balancing
#
# When a binary search tree is self-balancing, it saves us the work of balancing it... this is a very useful and practical feature
#
# Let's think of an example use case
#
# Suppose we write a relational database
#
# The database would parse a SQL query and execute the query
#
# The database would organize data into tables
#
# What if we want to index a table?
#
# We can use a red-black tree to index a table
#
# The red-black tree would reduce the time it takes to search for a record in our table, if the select query uses our index
#
# The index would be stored in memory, or on file, as a red-black tree (it would be stored on file in some form and loaded into memory as a red-black tree)
#
# The indexed columns would be the key for each node in our tree
#
# We would use the key to organize our tree... if two records have the same key, they would get assigned to the same node
#
# (In both binary search trees and hash maps, we use linked lists to handle collisions)
#
# If a record has a key of A and the root node has a key of R, and A < R, then the record with the key of A would get inserted somewhere in the left subtree of the root node
#
# If a record has a key of B and the root node has a key of R, and B > R, then the record with the key of B would get inserted somewhere inthe right subtree of the root node
#
# You can see how we use a key to organize a red-black tree (or more generally, a binary search tree)
#
# We can create a key from a set of indexed columns either by concatenating the columns, creating a hash code, or by some other means
#
# We need the key to be comparable, so that for two keys A and B, one of the following holds true: A < B, A == B, or A > B
#
# We can create a key from a set of indexed columns by concatenating the columns, generating a hash code, or by some other means
#
# I don't want to be too repetitive, but sometimes repetition helps
#
# I think we have rounded off this subject (which means, we have brought it to a conclusion)
#
# It's important to remember that red-black trees are self-balancing
#
# You can think of red-black trees as a superhero
#
# They have a superpower you should be aware of
#
# The superpower of every red-black tree is that the red-black tree is self-balancing
#
# You don't have to balance it yourself
#
# It takes care of the work for you
#
# Today is Wednesday, November 26, 2025
#
# Tomorrow is Thanksgiving
#
# I am planning to watch some of my favorite TV shows tomorrow and relax
#
# I am going to eat vegan food
#
# I am vegan
#
# I want to remind everyone that I'm a vegan, an animal rights activist, and a plant rights activist
#
# I care deeply about the animal rights movement and the plant rights movement... I am proud to be a member of these movements
#
# I want to remind everyone that animal rights are as important as civil rights
#
# Hillary Clinton said, "Women's rights are human rights"
#
# I agree with Hillary
#
# This rhetoric inspires many similar sayings
#
# I like to say, "Animal rights are human rights"
#
# I like to say, "Animal rights are women's rights"
#
# I like to say, "Animal rights are as important as civil rights"
#
# Everyone has a duty to stand up for animals, and treat them as our equals
#
# It's important to know that humans and animals are equals
#
# Animals have every right that humans have
#
# I'm really glad I said that, because every time I say it, it helps
#
# I'm a vegan, an animal rights activist, a plant rights activist
#
# I'm a software engineer and I'm also a devout Christian
#
# I wish everyone a nice Thanksgiving tomorrow
#
# I'm going to watch some of my favorite TV shows and relax
#
# I have a lot of work to do so I'd like to have a restful day tomorrow, and catch up on my TV shows
#
# Happy holidays
#
# Andrew

import random
import time
import argparse
import ast

class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
        self.frequency = 1

    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent

    def sibling(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left

    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()

    def __str__(self):
        return f'{self.value}{self.color}'

class RedBlackTree:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            for value in arr:
                self.insert(value)

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.insert_fix(node)
            return
        current = self.root
        while True:
            if value == current.value:
                current.frequency += 1
                return
            elif value < current.value:
                if current.left is None:
                    current.left = node
                    node.parent = current
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    node.parent = current
                    break
                else:
                    current = current.right
        self.insert_fix(node)

    def insert_fix(self, node):
        while node.parent and node.parent.color == 'red':
            if node.parent == node.grandparent().left:
                uncle = node.uncle()
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.grandparent().color = 'red'
                    node = node.grandparent()
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 'black'
                    node.grandparent().color = 'red'
                    self.rotate_right(node.grandparent())
            else:
                uncle = node.uncle()
                if uncle and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.grandparent().color = 'red'
                    node = node.grandparent()
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 'black'
                    node.grandparent().color = 'red'
                    self.rotate_left(node.grandparent())
        self.root.color = 'black'

    def delete(self, value):
        node = self.search(value)
        if node is None:
            return
        if node.left is None or node.right is None:
            self.replace_node(node, node.left or node.right)
        else:
            successor = self.find_min(node.right)
            node.value = successor.value
            self.replace_node(successor, successor.right)
        self.delete_fix(node)

    def delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.rotate_right(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.right:
                        sibling.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left is None or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.rotate_left(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.left:
                        sibling.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child

    def replace_node(self, old_node, new_node):
        if old_node.parent is None:
            self.root = new_node
        else:
            if old_node == old_node.parent.left:
                old_node.parent.left = new_node
            else:
                old_node.parent.right = new_node
        if new_node is not None:
            new_node.parent = old_node.parent

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def to_list(self):
        sorted_list = []
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            for _ in range(current.frequency):
                sorted_list.append(current.value)
            current = current.right
        return sorted_list

    def size(self):
        node_count = 0
        value_count = 0
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            node_count += 1
            value_count += current.frequency
            current = current.right
        return (node_count, value_count)

    def height(self):
        if self.root is None:
            return 0
        queue = []
        queue.append(self.root)
        height = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            height += 1
        return height

    def _str(self, node):
        if node is None:
            return ''
        elif node.left is None and node.right is None:
            return f'{node.value}'
        elif node.left and node.right is None:
            leftchild = self._str(node.left)
            return f'{node.value}({leftchild})'
        elif node.left is None and node.right:
            rightchild = self._str(node.right)
            return f'{node.value}({rightchild})'
        else:
            leftchild = self._str(node.left)
            rightchild = self._str(node.right)
            return f'{node.value}({leftchild})({rightchild})'

    def str(self):
        return self._str(self.root)

    def __str__(self):
        return self.str()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='redblacktree.py', description='Red black tree')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', '--inputfile', type=str)
    group.add_argument('-n', '--numbers', nargs='+', type=int) 
    group.add_argument('-r', '--random', action='store_true')
    parser.add_argument('-s', '--size', type=float, default=10)
    parser.add_argument('-min', '--minimum', type=float, default=0)
    parser.add_argument('-max', '--maximum', type=float, default=100)
    parser.add_argument('-t', '--test', nargs='+', type=int)
    parser.add_argument('-o', '--outputfile', type=str)
    args = parser.parse_args()
    if args.inputfile:
        with open(args.inputfile, 'r') as file:
            contents = file.read()
            arr = ast.literal_eval(contents)
    elif args.numbers:
        arr = args.numbers
    elif args.random:
        size, min, max = int(args.size), int(args.minimum), int(args.maximum)
        arr = [random.randint(min, max) for i in range(size)]
    if len(arr) <= 1000:
        print(f'Unsorted list')
        print('------------------------------')
        print(f'{arr}\n')
    tree = RedBlackTree(arr)
    root_value = tree.root.value
    node_count, value_count = tree.size()
    height = tree.height()
    print('Statistics')
    print('------------------------------')
    print(f'Root value: {root_value} Node count: {node_count} Value count: {value_count} Height: {height}')
    prefix_expression = tree.str()
    if node_count <= 1000:
        print('')
        print('String representation')
        print('------------------------------')
        print(prefix_expression)
    if args.test:
        print('')
        print('Linear search results')
        print('------------------------------')
        for i in range(len(args.test)):
            value = args.test[i]
            start_time = time.time()
            found = False
            for j in range(len(arr)):
                if value == arr[j]:
                    found = True
                    break
            time_elapsed = 1000 * (time.time() - start_time)
            print(f'{value} is present' if found else f'{value} is missing')
            print(f'The linear search took {time_elapsed:.4f} milliseconds')
            if i < len(args.test) - 1:
                print('')
        print('')
        print('Binary search results')
        print('------------------------------')
        for i in range(len(args.test)):
            value = args.test[i]
            start_time = time.time()
            found = tree.search(value)
            time_elapsed = 1000 * (time.time() - start_time)
            print(f'{value} is present' if found else f'{value} is missing')
            print(f'The binary search took {time_elapsed:.4f} milliseconds')
            if i < len(args.test) - 1:
                print('')
    if args.outputfile:
        with open(args.outputfile, 'w') as file:
            file.write(prefix_expression)
