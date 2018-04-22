# cuteprint
A Pretty Print Utils Library

## Example Usage

```python

from cuteprint import PrettyPrinter

# PrettyPrinter Init
p = PrettyPrinter()

# Contextual Function Demo
p.print_title("Contextual Pretty Print Functions Demo")
p.print_good("This is Good")
p.print_bad("This is Bad")
p.print_info("This is an Information")
p.print_question("Is this a Question ?")
p.print_separator(len=100,separator="~")

# Simple Loading Progress Bar Example
p.print_title("Simple Loading Progress Bar Demo")
t = p.start_progress(task="Loading templates ...")
time.sleep(6)
p.stop_progress(t)
p.print_separator(len=100,separator="~")

# Threaded Loading Examples (enable_dots set to False for better output)
p.print_title("Threaded Loading Demo")
t1 = threading.Thread(target=threadedExample, args=("thread1.com", 3))
t2 = threading.Thread(target=threadedExample, args=("thread2.com", 5))
t1.start()
t2.start()
```
