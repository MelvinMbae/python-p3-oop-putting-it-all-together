#!/usr/bin/env python3

class Book:
    
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
        self.current_page = 0
        
    def get_page_count(self):   
        # print(self._page_count)   
        return self._page_count
        
    def set_page_count(self, page_count):
        if not isinstance (page_count, int):
            print("page_count must be an integer")
            
        else:
            self._page_count = page_count
        
    page_count = property(get_page_count, set_page_count,)
            
    def turn_page(self):
        self.current_page += 1
        print("Flipping the page...wow, you read fast!")
        # print(self.current_page)   
   
        
book = Book("And Then There Were None", 272)
book.page_count = "272"
book.turn_page()
book.turn_page()
