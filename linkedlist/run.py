from linked_list import LinkedList

def run():
     list=LinkedList()
     for i in range(0, 10):
        list.insert_end(i)
     list.print()


if __name__ == '__main__':
    run()
