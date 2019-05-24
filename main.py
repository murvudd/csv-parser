from sys import argv

"""
!! this script does not check if there are values which have decimal separator, equal to neither of delimiters.
"""


# def create_output_csv(file, header: List[str], delimiter: str = ';', encoding: str = 'utf-8-sig'):
#     with open(file, mode='w', encoding=encoding) as out:
#         writer = csv.DictWriter(out, fieldnames=header, delimiter=delimiter)
#         writer.writeheader()


def main(in_file: str, out_file: str, in_delimiter: str, out_delimiter: str, encoding: str = 'utf-8-sig'):
    """

    :param in_file: str of file path
    :param out_file: str of file path
    :param in_delimiter:
    :param out_delimiter:
    :param encoding:
    :return:
    """
    with open(in_file, mode='r', encoding=encoding) as inf:
        with open(out_file, mode='w', encoding=encoding) as out:

            while True:
                try:
                    # row = reader.__next__().split(in_delimiter)
                    row = inf.readline().split(in_delimiter)

                    [out.write("{}{} ".format(x, out_delimiter)) for x in row[:-1]]
                    out.write(row[-1])
                except StopIteration:
                    break
                except Exception as e:
                    print(e)
                    raise

    return


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3], argv[4])
