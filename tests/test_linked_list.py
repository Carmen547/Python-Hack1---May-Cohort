import sys
import os
import pytest

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from linked_list import LinkedList

def test_linked_list_find_max():
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    assert ll.find_max() == 4
    
    empty_ll = LinkedList()
    with pytest.raises(ValueError):
        empty_ll.find_max()

