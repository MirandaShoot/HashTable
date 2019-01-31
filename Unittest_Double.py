
from Double_Hashing import HashDoubleTable
import unittest


class HashTableTest(unittest.TestCase):

    def test_init(self):
        ht = HashDoubleTable()
        self.assertEqual( ht.getLength() , 7)

    def test_length(self):
        ht = HashDoubleTable()
        self.assertEqual(ht.getLength(), 7)
        ht.put(123, 1)
        self.assertEqual(ht.getLength(), 7)
        ht.put(213, 5)
        self.assertEqual(ht.getLength(), 7)
        ht.put(4, 10)
        self.assertEqual(ht.getLength(), 7)
        ht = HashDoubleTable()

        for i in range (10):
            ht.put(i,i)
        self.assertEqual(ht.getLength(), 17)


    def test_load_factor(self):
        ht = HashDoubleTable()
        ht.put(123, 1)
        ht.put(213, 5)
        ht.put(4, 10)
        self.assertGreater(ht.load(),0.40)
        ht.put(2, 1)
        self.assertLess(ht.load(),0.40)
        ht.put(5, 5)
        ht.put(1, 10)

        self.assertEqual(ht.getLength(), 37)







    def test_set_and_get(self):
        ht = HashDoubleTable()
        ht.put(123, 1)
        ht.put(213, 5)
        ht.put(4, 10)
        self.assertEqual(ht.get(123), 1)
        self.assertEqual(ht.get(213), 5)
        self.assertEqual(ht.get(4), 10)
        self.assertEqual(ht.get(555), None)
        assert ht.getLength() == 7

        #with self.assertRaises(KeyError):
            #ht.get(5555)  # Key does not exist

    def test_delete(self):
        ht = HashDoubleTable()
        ht.put(123, 1)
        ht.put(213, 5)
        ht.put(4, 10)
        self.assertEqual(ht.getLength(), 7)
        ht.delete(123)
        ht.delete(213)
        self.assertEqual(ht.getLength(), 7)
        self.assertEqual(ht.delete(123),None)
        self.assertEqual(ht.delete(213),None)


    def test_isprime(self):
        ht = HashDoubleTable()
        self.assertEqual(ht.isPrime(37),True)
        self.assertEqual(ht.isPrime(4),False)

    def test_getprime(self):
        ht=HashDoubleTable()
        self.assertEqual(ht.getPrimeNumber(6),7)
        self.assertEqual(ht.getPrimeNumber(5),5)


    def test_newsize(self):
        ht=HashDoubleTable()
        ht.resize(7)
        self.assertEqual(ht.getLength(),17)
        self.assertEqual(ht.new_size(7), 17)
        self.assertNotEquals(ht.new_size(7), 7)

    def test_hash_rehash(self):
        ht = HashDoubleTable()
        self.assertEquals(ht.hash_function(1, 7),1)
        self.assertEquals(ht.hash_function(2, 7),2)
        self.assertEquals(ht.hash_function(14, 7),0)
        self.assertEquals(ht.rehash(4, 27),22)
        self.assertNotEquals(ht.rehash(4, 27),21)





if __name__ == '__main__':
    unittest.main()
