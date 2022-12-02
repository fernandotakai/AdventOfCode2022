import sys


rock = 'a'
paper = 'b'
scissors = 'c'

convert_table = {
    'x': 'a',
    'y': 'b',
    'z': 'c',
}

matches = {
    (rock, rock): 3 + 1, (rock, paper): 0 + 1, (rock, scissors): 6 + 1,
    (paper, paper): 3 + 2, (paper, scissors): 0 + 2, (paper, rock): 6 + 2,
    (scissors, scissors): 3 + 3, (scissors, rock): 0 + 3, (scissors, paper): 6 + 3
}


def get_points_for_round(round: tuple[str]) -> int:
    return matches[convert_table[round[1]], round[0]]


with open(sys.argv[1]) as f:
    inputs = [line.strip().lower().split(' ') for line in f.readlines()]

print(sum(get_points_for_round(round) for round in inputs))
