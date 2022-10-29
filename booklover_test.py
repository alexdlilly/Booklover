from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        BL = BookLover('Alex','email@email.com','fantasy') 
        BL.add_book('The Hobbit',4.5)
        outcome = (BL.book_list['book_name'].eq('The Hobbit')).any()
        assert outcome == True

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        BL = BookLover('Alex','email@email.com','fantasy') 
        BL.add_book('The Hobbit',4.5)
        BL.add_book('The Hobbit',4.5)
        count = (BL.book_list['book_name'].eq('The Hobbit')).any().sum()
        assert count == 1

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        BL = BookLover('Alex','email@email.com','fantasy') 
        BL.add_book('The Hobbit',4.5)
        assert (BL.has_read('The Hobbit')) == True

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        BL = BookLover('Alex','email@email.com','fantasy') 
        BL.add_book('The Hobbit',4.5)
        assert (BL.has_read('The Lord of the Rings')) == False

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        BL = BookLover('Alex','email@email.com','fantasy') 
        BL.add_book('The Hobbit',4.5)
        BL.add_book('The Lord of the Rings',4.6)
        BL.add_book('The Silmarillion',4.4)
        assert BL.num_books == 3

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        BL = BookLover('Alex','email@email.com','fantasy') 
        BL.add_book('The Hobbit',4.5)
        BL.add_book('The Lord of the Rings',4.6)
        BL.add_book('Harry Potter & The Prisoner of Azkaban', 2.9)
        assert len(BL.fav_books()) == 2

if __name__ == '__main__':

    unittest.main(verbosity=3)