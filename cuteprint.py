#!/usr/bin/env python
# encoding: utf-8
# This script is compatible with both Python 2 and 3

import sys
import threading
import time

class PrettyPrinter :

    # Colorized Output Functions

    def green(self, s):
        return '\033[1;32m{}\033[0m'.format(s)

    def red(self, s):
        return '\033[1;31m{}\033[0m'.format(s)

    def blue(self, s):
        return '\033[1;34m{}\033[0m'.format(s)

    def pink(self, s):
        return '\033[1;35m{}\033[0m'.format(s)

    def white(self, s):
        return '\033[1;37m{}\033[0m'.format(s)

    
    # Pretty-Print Contextual Functions 

    def custom_print(self, string, color, symbol, end, elapsed_time=None, replace_line=False):
        
        if elapsed_time:
            to_print = '{} {} {} {}'.format(color(symbol), str(string), 'in {} seconds'.format(elapsed_time), end)
        else:
            to_print = '{} {} {}'.format(color(symbol), str(string), end)

        if replace_line :
            to_print = '\r{}'.format(to_print)

        print(to_print)

    def print_good(self, s, end='\n', replace_line=False):
        self.custom_print(string=s, color=self.green, symbol='[+]', replace_line=replace_line, end=end)

    def print_bad(self, s, end='\n', replace_line=False):
        self.custom_print(string=s, color=self.red, symbol='[-]', replace_line=replace_line, end=end)

    def print_info(self, s, end='\n', replace_line=False, elapsed_time=None):
        self.custom_print(string=s, color=self.blue, symbol='[!]', replace_line=replace_line, elapsed_time=elapsed_time, end=end)

    def print_question(self, s, end='\n', replace_line=False):
        self.custom_print(string=s, color=self.white, symbol='[?]', replace_line=replace_line, end=end)

    def print_separator(self, length=150, suffix=None, separator='.', end='\n'):

        if suffix != None:
            final_len = length-len(suffix)-1
            print("{} {}".format(suffix, separator*final_len+end))
        else:
            print(separator*length+end)

    def print_title(self, title, top='=', bottom='=', left='>', right='<', caps=True):
        print('\n')
        print(self.white(top*(len(title)+4)))
        if caps :
            print(self.white("{} {} {} ".format(left,title.upper(),right)))
        else:
            print(self.white("{} {} {} ".format(left,title,right)))
        print(self.white(bottom*(len(title)+4))+'\n\n')

    def print_blank(self):
        print('\n')
    
    # Progress Dotted-Bar Functions 
    
    def progress(self, task, enable_dots, char):
        start_time = time.time()
        t = threading.currentThread()
        s = char
        self.print_info(task)
        while getattr(t, "load", True):
            if enable_dots:
                sys.stdout.write(s)
                sys.stdout.flush()
                time.sleep(1)
        self.print_info("Task << {} >> : Done".format(task), replace_line=True, elapsed_time=(time.time() - start_time), end="\n")

    def start_progress(self, task, enable_dots=True, char='.'):
        t = threading.Thread(target=self.progress, args=(task,enable_dots,char))
        t.daemon = True
        t.start()
        return t

    def stop_progress(self, loading_thread):
        loading_thread.load = False
        loading_thread.join()
    
if __name__ == '__main__':

    # PrettyPrinter Init
    p = PrettyPrinter()

    # Contextual Function Demo
    p.print_title("Contextual Pretty Print Functions Demo")
    p.print_good("This is Good")
    p.print_bad("This is Bad")
    p.print_info("This is an Information")
    p.print_question("Is this a Question ?")
    p.print_separator(length=100,separator="~")
    
    # Simple Loading Progress Bar Example
    p.print_title("Simple Loading Progress Bar Demo")
    t = p.start_progress(task="Loading templates ...")
    time.sleep(6)
    p.stop_progress(t)
    p.print_separator(length=100,separator="~")

    # Threaded Loading Examples (enable_dots set to False for better output)
    p.print_title("Threaded Loading Demo")
    t1 = threading.Thread(target=threadedExample, args=("thread1.com", 3))
    t2 = threading.Thread(target=threadedExample, args=("thread2.com", 5))
    t1.start()
    t2.start()

