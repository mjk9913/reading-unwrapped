from flask import Flask, jsonify
import csv

from book_analysis import analyze_book_data 

app = Flask(__name__)

@app.route("/fetch_book_data")
def fetch_book_data():
    """
        Converts Goodreads/Book data CSV into readable format and applies needed analysis for the app

        Returns:
            book_data(json): json array containing book data information
    """
    # bookCsv = request.files.get('file') -> future feature: to enable users to upload csv

    with open("book-files/goodreads_library_export.csv", newline='', encoding='utf-8') as csvfile: #TODO: CONVERT FILENAME TO GLOBAL ENV
        reader = csv.DictReader(csvfile)
        book_data = list(reader)
    book_data = analyze_book_data
    return jsonify(book_data)

if __name__ == "__main__":
    app.run(debug=True)