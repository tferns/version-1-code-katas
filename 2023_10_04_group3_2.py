# python .\2023_10_04_group3.py
# https://edabit.com/challenge/gt9LLufDCMHKMioh2

# Write a function that stutters a word as if someone is
# struggling to read it. The first two letters are repeated twice 
# with an ellipsis ... and space after each, and then the word
# is pronounced with a question mark ?.


def stutter(word: str) -> str:
    first_2_characters = word[0:2]
    return f"{first_2_characters}... {first_2_characters}... {word}?"

def stutter_paul(word: str) -> str:
    return f"{word[0]}{word[1]}... {word[0]}{word[1]}... {word}?"

if __name__ == '__main__':
    assert stutter("incredible") == "in... in... incredible?"
    assert stutter("enthusiastic") == "en... en... enthusiastic?"
    assert stutter("outstanding") == "ou... ou... outstanding?"

    assert stutter_paul("incredible") == "in... in... incredible?"
    assert stutter_paul("enthusiastic") == "en... en... enthusiastic?"
    assert stutter_paul("outstanding") == "ou... ou... outstanding?"

    print("No error throw, woo it works!")