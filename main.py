class Resource:
    def __init__(self, identifier, title, subject, rental_price, num_copies):
        self.identifier = identifier
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.num_copies = num_copies
        self.lent_out = 0

    def lend(self):
        if self.num_copies > self.lent_out:
            self.lent_out += 1
            return True
        return False

    def receive_back(self):
        if self.lent_out > 0:
            self.lent_out -= 1
            return True
        return False

    def is_available(self):
        return self.num_copies > self.lent_out

    def __str__(self):
        return f"{self.identifier}, {self.title}, {self.subject}, {self.rental_price:.2f}, {self.num_copies - self.lent_out}/{self.num_copies}"

class Book(Resource):
    def __init__(self, isbn, title, book_format, subject, rental_price, num_copies):
        super().__init__(isbn, title, subject, rental_price, num_copies)
        self.book_format = book_format

    def __str__(self):
        return f"Book - {super().__str__()}, {self.book_format}"

class Magazine(Resource):
    def __init__(self, magazine_number, title, print_type, subject, rental_price, num_copies):
        super().__init__(magazine_number, title, subject, rental_price, num_copies)
        self.print_type = print_type

    def __str__(self):
        return f"Magazine - {super().__str__()}, {self.print_type}"

class EducationalDVD(Resource):
    def __init__(self, dvd_number, title, subject, rental_price, num_copies):
        super().__init__(dvd_number, title, subject, rental_price, num_copies)

    def __str__(self):
        return f"Educational DVD - {super().__str__()}"

class LectureCD(Resource):
    def __init__(self, cd_number, title, subject, rental_price, num_copies):
        super().__init__(cd_number, title, subject, rental_price, num_copies)

    def __str__(self):
        return f"Lecture CD - {super().__str__()}"

class Library:
    def __init__(self):
        self.resources = {'book': [], 'magazine': [], 'educational_dvd': [], 'lecture_cd': []}

    def add_resource(self, resource_type, resource):
        if resource_type in self.resources:
            self.resources[resource_type].append(resource)
            print(f"{resource} added to the library.")
        else:
            print("Invalid resource type.")

    def remove_resource(self, resource_type, identifier):
        if resource_type in self.resources:
            for resource in self.resources[resource_type]:
                if resource.identifier == identifier:
                    self.resources[resource_type].remove(resource)
                    print(f"{resource} removed from the library.")
                    return
            print("Resource not found.")
        else:
            print("Invalid resource type.")

    def view_resources(self, resource_type, available_only=True):
        if resource_type in self.resources:
            for resource in self.resources[resource_type]:
                if available_only and resource.is_available():
                    print(resource)
                elif not available_only and not resource.is_available():
                    print(resource)
        else:
            print("Invalid resource type.")

    def view_resources_by_subject(self, subject):
        for resource_type, resources in self.resources.items():
            for resource in resources:
                if resource.subject == subject:
                    print(resource)

    def lend_resource(self, resource_type, identifier):
        if resource_type in self.resources:
            for resource in self.resources[resource_type]:
                if resource.identifier == identifier:
                    if resource.lend():
                        print(f"{resource} lent out.")
                        return
                    else:
                        print("No available copies to lend.")
                        return
            print("Resource not found.")
        else:
            print("Invalid resource type.")

    def update_resource_received(self, resource_type, identifier):
        if resource_type in self.resources:
            for resource in self.resources[resource_type]:
                if resource.identifier == identifier:
                    if resource.receive_back():
                        print(f"{resource} received back.")
                        return
                    else:
                        print("No copies were lent out.")
                        return
            print("Resource not found.")
        else:
            print("Invalid resource type.")

# Example usage
library = Library()

# Adding resources
library.add_resource('book', Book('ISBN1234', 'The Solar System', 'Hardcover', 'Science', 15.00, 5))
library.add_resource('magazine', Magazine('01', 'History of Cricket', 'color', 'Sports', 5.00, 7))
library.add_resource('educational_dvd', EducationalDVD('10', 'Birth of the Solar System', 'Astronomy', 2.50, 10))
library.add_resource('lecture_cd', LectureCD('21', 'Basics of Western Music', 'Music', 1.50, 11))

# Viewing resources
print("\nCurrently available books:")
library.view_resources('book', available_only=True)

print("\nCurrently unavailable magazines:")
library.view_resources('magazine', available_only=False)

# Lending resources
print("\nLending a book:")
library.lend_resource('book', 'ISBN1234')

print("\nViewing all resources with subject 'Science':")
library.view_resources_by_subject('Science')

# Receiving back resources
print("\nReceiving back a book:")
library.update_resource_received('book', 'ISBN1234')
