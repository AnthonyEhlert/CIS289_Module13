"""
Program Name: Data_Pipeline_Assignment_Ehlert.py
Author: Tony Ehlert
Date: 11/15/2023

Program Description: This program utilizes a data pipeline to stream book data contained in two separate text files to
a queue and then counts how many words are contained in each file and prints than information to the console.
"""
import re
import time
import multiprocessing
from multiprocessing import Process
import threading

def stream_two_books(book_stream_queue):
    def stream_two_cities():
        with open('A tale of two cities.txt', encoding="UTF-8") as book:
            for line in book:
                if not "THE END" in line:
                    output_str = re.sub('[^A-Za-z0-9\']+', ' ', line)
                    output_str = output_str.strip()
                    if output_str == "":
                        continue
                    if output_str is not None:
                        for word in output_str.split():
                            #print (word)
                            book_stream_queue.put({"two_cities":word.lower()},block=True)
                else:
                    break
        return
    def stream_dracula():
        with open('Dracula.txt', encoding="UTF-8") as book:
            for line in book:
                if not "THE END" in line:
                    output_str = re.sub('[^A-Za-z0-9\']+', ' ', line)
                    output_str = output_str.strip()
                    if output_str == "":
                        continue
                    if output_str is not None:
                        for word in output_str.split():
                            #print(word)
                            book_stream_queue.put({"dracula":word.lower()},block=True)
                else:
                    break
        return


    thread1 = threading.Thread(target = stream_two_cities)
    thread2 = threading.Thread(target = stream_dracula)
    #thread2.daeman = True
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # while not book_stream_queue.empty():
    #     print(book_stream_queue.get())
    # print("threads complete")


def read_two_books_stream(book_stream_queue):
    time.sleep(4)
    dracula_count = 0
    count = 0
    while not book_stream_queue.empty():
        book_dict = book_stream_queue.get()
        for key in book_dict:
            if key == 'dracula':
                dracula_count += 1
            else:
                count += 1
            print(count)
            print('Dracula count = ' + str(dracula_count))



if __name__ == "__main__":
    book_stream_queue = multiprocessing.Queue()
    p1 = Process(target=stream_two_books,args=(book_stream_queue,))
    p2 = Process(target=read_two_books_stream,args=(book_stream_queue,))
    p1.start()
    p2.start()
    p1.join()
    #p2.join()

#### Run code as it is to see queue get filled & printed out. You can see ea. word of the books is tagged w/ the book title.


#### Write the read_two_books_stream process to read the queue & count how many words are in each of the books. (leaving in the 4 second delay will help avoid some empty queue issues)


#### Print the final word counts


#### Once all is working, remove interim prints of queue so that the program as submitted will only determine final count