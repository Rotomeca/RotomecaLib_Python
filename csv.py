import copy


class RImportedCsv:
    def __init__(self, path, type=';', has_headers=True) -> None:
        self.__columns = {}
        self.__array = []
        self.__original_path = path
        self.__has_headers = has_headers
        if path is not None:
            self.__import_csv(type)

    def import_csv(self, type):
        file = open(self.__original_path, 'r')
        raw = file.read()
        file.close()

        columns = {}
        datas = []

        splited_raw = raw.split('\n')

        it = 0
        for item in splited_raw:
            raw_datas = item.split(type)
            if it == 0 and self.__has_headers:
                i = 0
                for d in raw_datas:
                    columns[d] = i
                    i += 1
            else:
                datas.append(raw_datas)
            it += 1

        self.__array = datas
        self.__columns = columns

    __import_csv = import_csv

    def __getitem__(self, pos) -> list | any:
        column, row = pos
        if column in self.__columns:
            column = self.__columns[column]

        if row is None:
            tmp = []
            it = 0
            for i in self.__array:
                if it == column:
                    tmp.append(i)
                it += 1
            return tmp
        else:
            return self.__array[row][column]

    def col_count(self):
        return len(self.__columns.keys())

    def row_count(self):
        return len(self.__array)

    def clone(self):
        return copy.deepcopy(self)

    def get_array(self):
        return self.__array

    def get_cols(self):
        return self.__columns

    def path(self):
        return self.__original_path


class Rcsv(RImportedCsv):
    def __init__(self, path=None, separator=';', has_headers=True):
        super().__init__(path, separator, has_headers)
        self.__imported_from_path = None
        self.separator = separator

    @staticmethod
    def from_array(array, cols=None):
        csv = Rcsv()
        if cols is not None:
            csv.__columns = cols
        csv.__array = array
        return csv
