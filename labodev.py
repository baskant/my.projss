class Book:
    def __init__(self, name, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return f"Kitap Adı: {self.name}, Yazar: {self.author}, Yayın Yılı: {self.year}"

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()


class Library:
    def __init__(self):
        self.books = []

    def control_name(self, name):
        if isinstance(name, str) and name.strip():
            return name
        else:
            raise ValueError("Kitap adı boş olamaz. Lütfen geçerli bir kitap adı girin.")

    def control_author(self, author):
        if isinstance(author, str) and author.strip() and author.replace(" ", "").isalpha():
            return author
        else:
            raise ValueError("Geçersiz yazar adı. Lütfen geçerli bir yazar adı girin.")

    def control_year(self, year):
        try:
            year = int(year)
            if year <= 0:
                raise ValueError("Yayın yılı 0'dan küçük olamaz.")
            return year
        except ValueError:
            raise ValueError("Geçersiz yıl. Lütfen geçerli bir yıl girin.")

    def add_book(self, name, author: str, year: int):
        while True:
            try:
                name = self.control_name(name)
                author = self.control_author(author)
                year = self.control_year(year)
                new_book = Book(name, author, year)

                if new_book in self.books:
                    print("Bu kitap zaten mevcut! Aynı kitabı bir kez daha ekleyemezsiniz.")
                    break
                else:
                    self.books.append(new_book)
                    print("Kitap başarıyla eklendi.")
                    break
            except ValueError as e:
                print(e)
                name = input("Kitap Adı: ")
                author = input("Yazar: ")
                year = input("Yayın Yılı: ")

    def remove_book(self, name):
        for book in self.books:
            if book.name.lower() in book.name.lower():
                self.books.remove(book)
                print("Kitap başarıyla silindi.")
                return
        print("Kitap bulunamadı.")

    def search_by_name(self, name):
        found_books = []
        for book in self.books:
            if name.lower() in book.name.lower():
                found_books.append(book)

        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Kitap bulunamadı.")

    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if author.lower() in book.author.lower():
                found_books.append(book)

        if found_books:
            for book in found_books:
                print(book)
        else:
            print("Yazar bulunamadı.")

    def list_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("Kütüphanede hiç kitap yok.")


def main():
    library = Library()

    while True:
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Ara (İsme Göre)")
        print("4. Kitap Ara (Yazara Göre)")
        print("5. Tüm Kitapları Listele")
        print("6. Çıkış")

        choice = input("Bir işlem seçin (1-6): ")

        if choice == "1":
            name = input("Kitap Adı: ")
            author = input("Yazar: ")
            year = input("Yayın Yılı: ")
            library.add_book(name, author, year)

        elif choice == "2":
            name = input("Silmek istediğiniz kitabın adını girin: ")
            library.remove_book(name)

        elif choice == "3":
            name = input("Aramak istediğiniz kitabın adını girin: ")
            library.search_by_name(name)

        elif choice == "4":
            author = input("Aramak istediğiniz yazarı girin: ")
            library.search_by_author(author)

        elif choice == "5":
            print("Kütüphanedeki tüm kitaplar:")
            library.list_books()

        elif choice == "6":
            print("Uygulama kapatılıyor...")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
