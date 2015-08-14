import time
import sort

algor_list = [sort.insertion_sort, 
              sort.selection_sort]

def algor_time(algorithm):
    start_time = time.clock()
    value = algorithm
    print 'Done. Result: ', ''.join(value)
    print 'Sorted in', time.clock() - start_time, 'seconds\n'

def main():
    text = raw_input("Enter a word to sort, or type 'exit': ")
    if text == 'exit':
        print 'exiting...\nGood Bye!'
        return
    for i in algor_list:
        print 'Using', i.__name__, '.........'
        algor_time(i(text))
    main()
    
main()