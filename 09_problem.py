# Search for an Author
"""
A dedicated librarian has collected all the names of authors, who authored the
the books or articles in his library.

He then stored this list of author names as linked list. 

Now he approached you to write a program to help a user find whether
the specified author name is present in the list or not, and give the node number,
as the node number helps the user to find the related books.

your task is to return in which node the author exist.

Example 1:

input:
linked list: 'eshwar'=>'kranthi'=>'rohini'=>'surya'=>'vikas'
search key : 'kranthi'
output: 
4

"""

import unittest
import helper_llists as llists


def search_linked_list(node, sk):
    """
    ??? Write what needs to be done ???
    """
    pass
    init=node
    count=1
    while init:
        if init.val==sk:
            break
        count+=1
        init=init.next
    return count


class TestSearchLinkedList(unittest.TestCase):

    def test_01(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'babu',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'john'
        nodenumber = 3
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_02(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'babu',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'surya'
        nodenumber = 6
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_03(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'balu',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'arun'
        nodenumber = 1
        self.assertEqual(search_linked_list(node, search_key), nodenumber)

    def test_04(self):
        node = llists.create_from_string(
            "{val:'arun',next:{val:'arun madhav',next:{val:'john',next:{val:'kavya',next:{val:'raheem',next:{val:'surya',next:None}}}}}}")
        search_key = 'arun madhav'
        nodenumber = 2
        self.assertEqual(search_linked_list(node, search_key), nodenumber)


if __name__ == '__main__':
    unittest.main(verbosity=2)
