from ast import Raise
import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable

def test_create_ht():
    hash = Hashtable()
    actual = hash.size
    expected = 1024
    assert actual == expected

def test_valid_hash():
    hash = Hashtable()
    index = hash.hash("fruitbat")
    assert index >= 0 < hash.size


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_collision():
    ht = Hashtable()
    ht.set("atm","Teller")
    ht.set("mat","Matt")
    ht.set("tam","Tims Tams")
    
    actual = ht.get("mat")
    expected = 'Matt'
    assert actual == expected

def test_update_key_value():
    ht = Hashtable()
    ht.set("afga",'Absolute fine go away')
    ht.set("gfaa",'Give fire and arson')
    ht.set("aagf",'Air and Golden Fleece')
    ht.set("afga",'As fine as a golden Adonis')

    actual = ht.get('afga')
    getkey = ht.keys()
    keys = {"afga", "gfaa", "aagf"} 
    
    expected = 'As fine as a golden Adonis'
    assert keys == getkey
    assert actual == expected

def test_keys():
    ht = Hashtable()
    ht.set("ahmad", 30)
    ht.set("listen", "to me")
    ht.set("silent", True)

    actual = ht.keys()
    expected = {'ahmad','listen','silent'}
    assert actual == expected

def test_invalid_key():
    with pytest.raises(Exception):
        ht = Hashtable()
        ht.get("banana")
          