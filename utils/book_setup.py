from typing import List
import logging
from books import Book

logging = logging.getLogger(__name__)

def validate_books(book_rows: List) -> List:
    """
    Create Book objects from rows of csv book data, 
    validate that all required attributes exist.

    Args:
        book_rows (List): Rows from csv representing book data
    Returns:
        List: List of Book objects

    """
    books = []
    for row in book_rows:
        try:
            book = Book.create(
                title=row['title'],
                author=row['author'],
                own_rating=float(row['own_rating']),
                avg_rating=float(row['avg_rating']),
                num_pages=int(row['num_pages']),
                pub_year=int(row['pub_year']),
                read_date=row.get('read_date'),
                date_added=row.get('date_added'),
                rev=row.get('rev'),
                read_count=int(row.get('read_count', 0))
            )
            books.append(book)
        except KeyError as e:
            logging(f"Missing required field: {e}")
        except ValueError as e:
            logging(f"Invalid value: {e}")

    return books