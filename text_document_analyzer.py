class Textdocument:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        splitting = self.text.split()
        words_number = len(splitting)
        return f"This is the number of words: {words_number}"

    def unique_words(self):
        unique = []
        splitting = self.text.split()

        for word in splitting:
            if word not in unique:
                unique.append(word)

        return f"This is the number of unique words: {len(unique)}"

    def most_common(self):
        most_frequent = []
        frequency = {}
        splitting = self.text.split()

        for word in splitting:
            frequency[word] = frequency.get(word, 0) + 1

        most = max(frequency.values())

        for key, value in frequency.items():
            if value == most:
                most_frequent.append(key)

        return f"These are the most frequent words: {most_frequent}"
