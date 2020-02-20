from undirectional_list import Node, UndirectionalList


def main():
    l = UndirectionalList()
    l.insert_to_begin(Node(1))
    l.insert_to_begin(Node(2))
    l.insert_to_end(Node(3))
    l.insert_to_end(Node(4))
    l.insert_to_middle(Node(5), 2)
    l.insert_to_middle(Node(6), 3)
    print()
    l.display()
    l.sub_from_middle(Node(7), 3)
    print()
    l.display()


if __name__ == '__main__':
    main()
