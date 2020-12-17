"""
This is a helper class to create & print Linked_lists
Needed to run other linked list programs
"""

# DO NOT TOUCH THE CODE IN THIS FILE
# If you would like to play around copy this code to another file

import json


class LinkedList:

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        # Linked List String
        return self.linked_list_string(self)

    def __repr__(self):
        # Represents Linked List
        return str(self.val)

    def linked_list_string(self, linked_list):
        """ Actual Linked List String Implementation """

        if linked_list is not None:
            root_str = str(linked_list.val) + " => "
            next_str = self.linked_list_string(linked_list.next)

            return root_str + next_str
        return 'None'

    def __eq__(self, other):
        # Two Linked List Comparions for Equality
        if self is None and other is None:
            return True

        if self is not None and other is not None:
            return (self.val == other.val) and self.next.__eq__(other.next)

        return False


def create_from_dict(data):
    """Create Linked List From Dictionary"""

    new_linked_list = LinkedList(data["val"])

    if data.get("next") is not None:
        new_linked_list.next = create_from_dict(data["next"])

    return new_linked_list


def create_from_string(root_str):
    """Create Linked List From String"""

    root_dict = root_str.replace(',next:None', '').replace(
        'val:', '"val":').replace('next:', '"next":').replace("'",'"')

    data = json.loads(root_dict)

    return create_from_dict(data)


if __name__ == '__main__':
    node = create_from_string(
        '{val:1,next:{val:2,next:{val:3,next:{val:4,next:{val:5,next:{val:6,next:None}}}}}}')
    print(node)
