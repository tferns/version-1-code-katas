# python .\2023_10_04_group3.py
# https://edabit.com/challenge/tgEWKRQD8hu5dD3pX

from typing import Optional

# Create a function that takes in a current mood and 
# return a sentence in the following format: "Today, I am feeling {mood}".
# However, if no argument is passed, return "Today, I am feeling neutral".
def mood_today_1(mood: str | None = "neutral") -> str:
    return f"Today, I am feeling {mood}"

def mood_today_2(mood: Optional[str] = "neutral") -> str:
    return f"Today, I am feeling {mood}"

def mood_today_3(mood = "neutral") -> str:
    return "Today, I am feeling {}".format(mood)


if __name__ == '__main__':
    assert mood_today_1("happy") == "Today, I am feeling happy"
    assert mood_today_1("sad") == "Today, I am feeling sad"
    assert mood_today_1() == "Today, I am feeling neutral"

    assert mood_today_2("happy") == "Today, I am feeling happy"
    assert mood_today_2("sad") == "Today, I am feeling sad"
    assert mood_today_2() == "Today, I am feeling neutral"

    assert mood_today_3("happy") == "Today, I am feeling happy"
    assert mood_today_3("sad") == "Today, I am feeling sad"
    assert mood_today_3() == "Today, I am feeling neutral"
    print("No error throw, woo it works!")