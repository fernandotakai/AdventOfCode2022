import sys


rock = 'a'
paper = 'b'
scissors = 'c'

win = 'z'
lose = 'x'
draw = 'y'

result_table = {
    (rock, lose): scissors, (rock, draw): rock, (rock, win): paper,
    (paper, lose): rock, (paper, draw): paper, (paper, win): scissors,
    (scissors, lose): paper, (scissors, draw): scissors, (scissors, win): rock,
}

matches = {
    (rock, rock): 3 + 1, (rock, paper): 0 + 1, (rock, scissors): 6 + 1,
    (paper, paper): 3 + 2, (paper, scissors): 0 + 2, (paper, rock): 6 + 2,
    (scissors, scissors): 3 + 3, (scissors, rock): 0 + 3, (scissors, paper): 6 + 3
}


def get_points_for_round(their_choice: str, result: str) -> int:
    my_choice = result_table[(their_choice, result)]
    print(my_choice, their_choice, matches[(my_choice, their_choice)])
    return matches[(my_choice, their_choice)]


with open(sys.argv[1]) as f:
    inputs = [line.strip().lower().split(' ') for line in f.readlines()]

print(sum(get_points_for_round(*round) for round in inputs))
