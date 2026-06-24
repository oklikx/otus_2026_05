"""Скрипт, считывающий данные по книгам из файла books.csv
и данные по пользователям из файла users.json.
Далее распределяет книги по пользователям и формирует новый файл result.json"""

import csv
import json

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

books = []

with open("books.csv", "r", encoding="utf-8") as file:

    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        books.append(row)

with open("users.json", "r", encoding="utf-8") as json_file:
    users = json.load(json_file)

TOTAL_BOOKS = len(books)
total_users = len(users)

base_books_per_user = TOTAL_BOOKS // total_users
extra_books = TOTAL_BOOKS % total_users

current_book_index = 0
result_data = []


def format_user(user_data):
    """Форматирует данные пользователя.
    Оставляет только необходимые поля и добавляет поле books"""
    return {
        "name": user_data["name"],
        "gender": user_data["gender"],
        "address": user_data["address"],
        "age": user_data["age"],
        "books": []
    }


def format_book(book_data):
    """Форматирует данные по книге.
    Оставляет только необходимые поля и приводит их названия
    в нужный формат (нижний регистр)."""
    try:
        pages = int(book_data["Pages"])
    except (ValueError, TypeError):
        pages = 0

    return {
        "title": book_data["Title"],
        "author": book_data["Author"],
        "pages": pages,
        "genre": book_data['Genre'],
    }


for i, user in enumerate(users):
    books_count = base_books_per_user + (1 if i < extra_books else 0)

    user_books = books[current_book_index: current_book_index + books_count]
    current_book_index += books_count

    formatted_user = format_user(user)

    for book in user_books:
        formatted_user["books"].append(format_book(book))

    result_data.append(formatted_user)


with open("result.json", mode="w", encoding="utf-8") as result_file:
    json.dump(result_data, result_file, ensure_ascii=False, indent=4)
