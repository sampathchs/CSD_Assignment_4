# drop a middle element
"""
Given a linked list, delete the node in which the given value is present

Your task is to drop the specified node and return the remaining linked list

Example 1:
input:
2=>3=>4=>5=>6
delnum: 4

output:
2=>3=>5=>6
"""

import unittest
import helper_llists as llists


def del_node(node, delnum):
    """
    ??? Write what needs to be done ???
    """
    pass
    init=node
    start_index=init.next
    list=[]
    while init:
        list.append(init.val)
        init=init.next
    if delnum==list[0]:
        return node.next
    else:
        while start_index:
            if start_index.next.val==delnum:
                break
            start_index=start_index.next
        start_index.next=start_index.next.next
        return node


# DO NOT TOUCH THE BELOW CODE
class TestDeleteNode(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            '{val:1,next:{val:2,next:{val:3,next:{val:4,next:{val:5,next:{val:6,next:None}}}}}}')
        delnum = 6
        modified_list_01 = llists.create_from_string(
            '{val:1,next:{val:2,next:{val:3,next:{val:4,next:{val:5,next:None}}}}}')
        self.assertEqual(del_node(node, delnum), modified_list_01)

    def test_02(self):
        node = llists.create_from_string(
            '{val:1,next:{val:2,next:{val:3,next:{val:4,next:{val:5,next:{val:6,next:None}}}}}}')
        delnum = 1
        modified_list_02 = llists.create_from_string(
            '{val:2,next:{val:3,next:{val:4,next:{val:5,next:{val:6,next:None}}}}}')
        self.assertEqual(del_node(node, delnum), modified_list_02)

    def test_03(self):
        node = llists.create_from_string(
            '{val:1,next:{val:2,next:{val:3,next:{val:4,next:{val:5,next:{val:6,next:None}}}}}}')
        delnum = 4
        modified_list_03 = llists.create_from_string(
            '{val:1,next:{val:2,next:{val:3,next:{val:5,next:{val:6,next:None}}}}}')
        self.assertEqual(del_node(node, delnum), modified_list_03)


if __name__ == '__main__':
    unittest.main(verbosity=2)
