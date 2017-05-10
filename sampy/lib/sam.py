import re

class Sam:

    @staticmethod
    def extract_sequence(line):
        """Extract and returns None or the sequence from a line."""
        fields = re.split(r'\t', line)
        return fields[9].upper() if fields.__len__() >= 9 else None

    @staticmethod
    def is_leading_match(sequence, subsequence):
        return sequence.startswith(subsequence)

    @staticmethod
    def is_trailing_match(sequence, subsequence):
        return sequence.endswith(subsequence)

    @staticmethod
    def is_midway_match(sequence, subsequence):
        return re.match(".?" + subsequence, sequence)

