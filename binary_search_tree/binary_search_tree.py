# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, new_node):

        if new_node < self.value:
            # print(new_node, 'new node <', self.value)

            if self.left is None:
                self.left = BinarySearchTree(new_node)

            else:
                self.left.insert(new_node)

        else:
            # print(new_node, 'new node >', self.value)

            if self.right is None:
                self.right = BinarySearchTree(new_node)

            else:
                self.right.insert(new_node)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if target == self.value:
            return True
        
        elif target < self.value:

            if self.left is None:
                return False

            else:
                # print(target, 'less then', self.value, 'moving left')
                return self.left.contains(target)

        elif target > self.value:

            if self.right is None:
                return False

            else:
                # print(target, 'greater then', self.value, 'moving right')
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        
        if self.right is None:
            return self.value
        else:
            # print(self.value, 'can move right')
            return self.right.get_max()















    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass










test2 = BinarySearchTree(5)

# def test():
#     test2.insert(2)
#     test2.insert(3)
#     test2.insert(7)
#     test2.insert(6)
#     test2.insert(2)
#     test2.insert(10)
# #     test2.contains(4)
#     test2.get_max()
# print(test(), 'result')












    # # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
