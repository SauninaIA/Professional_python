import types


list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]


class FlatIterator:

    def __init__(self, list_of_list):
        self.list = list_of_list

    def __iter__(self):
        self.cursor = -1
        self.flat_list = iter([])
        return self

    def __next__(self):
        try:
            item = next(self.flat_list)
        except StopIteration:
            self.cursor += 1
            if self.cursor == len(self.list):
                raise StopIteration
            self.flat_list = iter(self.list[self.cursor])
            item = next(self.flat_list)
        return item


# def test():
#
#     list_of_lists_1 = [
#         ['a', 'b', 'c'],
#         ['d', 'e', 'f', 'h', False],
#         [1, 2, None]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             FlatIterator(list_of_lists_1),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def flat_generator(list_of_lists):
    for item in list_of_lists:
        if type(item) == list:
            for att_item in flat_generator(item):
                yield att_item
        else:
            yield item


# def test_2():
#
#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#
#     assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)



if __name__ == '__main__':
    # test()
    # flat_iterator = FlatIterator(list_of_lists)
    # flat_list = [item for item in flat_iterator]
    # print(flat_list)
    flat_list = [item for item in flat_generator(list_of_lists_2)]
    print(flat_list)
    # test_2()
