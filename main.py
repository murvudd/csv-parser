from sys import argv

"""
!! this script does not check if there are values which have decimal separator, equal to neither of delimiters.
"""


# def create_output_csv(file, header: List[str], delimiter: str = ';', encoding: str = 'utf-8-sig'):
#     with open(file, mode='w', encoding=encoding) as out:
#         writer = csv.DictWriter(out, fieldnames=header, delimiter=delimiter)
#         writer.writeheader()

def progress(i: int, no_lines: int):
    print("{} out of {}".format(i, no_lines))
    print("percentage {0:.2f}".format((i / no_lines) * 100))


def main(in_file: str, out_file: str, in_delimiter: str, no_of_lines: int, out_delimiter: str = '\t', encoding: str = 'utf-8-sig'):
    """

    :param in_file: str of file path
    :param out_file: str of file path
    :param in_delimiter:
    :param out_delimiter:
    :param no_of_lines:
    :param encoding:
    :return:
    """
    i = 0
    with open(in_file, mode='r', encoding=encoding) as inf:
        with open(out_file, mode='w', encoding=encoding) as out:
            while True:
                try:

                    row = inf.__next__().split(in_delimiter)
                    # row = inf.readline(no_of_lines).split(in_delimiter)
                    [out.write("{}{} ".format(x, out_delimiter)) for x in row[:-1]]
                    out.write(row[-1])
                    i += 1
                    if i < 100 and i % 10 == 0:
                        progress(i, no_of_lines)
                    if i < 1000 <= 20000 and i % 1000 == 0:
                        progress(i, no_of_lines)
                    if i > 20000 and i % 10000 == 0:
                        progress(i, no_of_lines)

                except StopIteration:
                    break
                except Exception as e:
                    print(e)
                    raise


if __name__ == '__main__':
    # main(argv[1], argv[2], argv[3], argv[4], int(argv[5]))
    main(argv[1], argv[2], argv[3], int(argv[4]))
