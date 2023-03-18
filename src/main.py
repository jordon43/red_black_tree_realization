from RedBlackTree import RedBlackTree


if __name__ == "__main__":
    bst = RedBlackTree()
    while True:
        print("Укажите метод который хотите вызвать:\n 1 - Поиск элемента\n 2 - Вставка элемента\n 3 - Выход")
        word_in = str(input())
        match word_in:
            case "1":
                print("Введите число которое вы хотите найти", end=":")
                input_w = int(input())
                result_search = bst.search(input_w)
                if result_search.item != 0:
                    print("Такой элемент есть в дереве")
                else:
                    print("Такого элемента нет в красно-черном дереве")
            case "2":
                print("Введите число которое вы хотите вставить", end=":")
                input_w = int(input())
                bst.insert(input_w)
            case "3":
                break
