import os

from . import Sam

class SamSearcher:

    def __init__(self, filepath, subsequence, match_type):
        self.filepath = filepath
        self.subsequence = subsequence.upper()
        self.match_type = match_type
        self.sam = Sam()
        if not os.path.isfile(self.filepath):
            raise Exception(self.filepath + " not found")

    def count(self):
        if self.match_type == 'leading':
            return self.count_leading()
        elif self.match_type == 'trailing':
            return self.count_trailing()
        elif self.match_type == 'midway':
            return self.count_midway();
        else:
            raise Exception("Unknown match type")

    def matches(self):
        if self.match_type == 'leading':
            return self.leading_matches()
        elif self.match_type == 'trailing':
            return self.trailing_matches()
        elif self.match_type == 'midway':
            return self.midway_matches();
        else:
            raise Exception("Unknown match type")

    def leading_matches(self):
        matches = []
        sam_file = open(self.filepath, 'r')
        for line in sam_file.readlines():
            seq = self.sam.extract_sequence(line)
            if seq and self.sam.is_leading_match(seq, self.subsequence):
                matches.append(seq)
        sam_file.close()
        return matches

    def trailing_matches(self):
        matches = []
        sam_file = open(self.filepath, 'r')
        for line in sam_file.readlines():
            seq = self.sam.extract_sequence(line)
            if seq and self.sam.is_trailing_match(seq, self.subsequence):
                matches.append(seq)
        sam_file.close()
        return matches

    def midway_matches(self):
        matches = []
        sam_file = open(self.filepath, 'r')
        for line in sam_file.readlines():
            seq = self.sam.extract_sequence(line)
            if seq and self.sam.is_midway_match(seq, self.subsequence):
                matches.append(seq)
        sam_file.close()
        return matches

    def count_leading(self):
        count = 0
        sam_file = open(self.filepath, 'r')
        for line in sam_file.readlines():
            seq = self.sam.extract_sequence(line)
            if seq and self.sam.is_leading_match(seq, self.subsequence):
                count += 1
        sam_file.close()
        return count

    def count_trailing(self):
        count = 0
        sam_file = open(self.filepath, 'r')
        for line in sam_file.readlines():
            seq = self.sam.extract_sequence(line)
            if seq and self.sam.is_trailing_match(seq, self.subsequence):
                count += 1
        sam_file.close()
        return count

    def count_midway(self):
        count = 0
        sam_file = open(self.filepath, 'r')
        for line in sam_file.readlines():
            seq = self.sam.extract_sequence(line)
            if seq and self.sam.is_midway_match(seq, self.subsequence):
                count += 1
        sam_file.close()
        return count
