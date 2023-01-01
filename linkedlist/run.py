from linked_list import LinkedList

def run():
     list=LinkedList()
     for i in range(1, 5):
        list.insert_end(i)
     list.print()

if __name__ == '__main__':
    run()
