STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with', '\n'
]


class FileReader:
    def __init__(self, filename):
        self.poem = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        self.poem = open(self.poem, "r")
        return self.poem.readlines()
        file.close()
        # raise NotImplementedError("FileReader.read_contents")


class WordList:
    def __init__(self, text):
        self.text = text
        self.words = []
        self.clean_words = {}

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        for i in self.text:
            x = i.split()
            # words.append(x)
            for y in x:
                y = y.lower()
                self.words.append(y)
        return self.words

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~-'''
        for i in self.words:
            if i[-1] in punc:
                i = i.replace(i, i[0:-1])
            elif i[0] in punc:
                i = i.replace(i, i[1:-1])
            if i in STOP_WORDS:
                pass
            elif i in self.clean_words:
                self.clean_words[i] += 1
            else:
                self.clean_words[i] = 1


    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        return self.clean_words


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        for i in sorted(self.freqs, key=self.freqs.get, reverse=True):
            print(i, '|', self.freqs[i])
        # raise NotImplementedError("FreqPrinter.print_freqs")


read = FileReader("one-today.txt")
w_list = WordList(read.read_contents())
extracted_words = w_list.extract_words()
stop_words_removed = w_list.remove_stop_words()
frequency = w_list.get_freqs()



if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
