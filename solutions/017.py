#!/usr/bin/python3
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is
in compliance with British usage.
'''

from helpers import print_memory_usage_report, print_time_elapsed
from time import time
import tracemalloc


def main():
    # Keep track of time elapsed and memory used
    start_time = time()
    tracemalloc.start()

    # ********** Solution begins here ********** #

    DIGITS = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    TEENS = [
        '', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    total_letters = 0
    for num in range(1, 1000):
        if num > 99:
            total_letters += len(DIGITS[num // 100]) + len('hundred')

            num %= 100
            if num:  # The spelling will include 'and'
                total_letters += 3

        # At this point, 0 <= num <= 99

        if 10 < num < 20:
            total_letters += len(TEENS[num - 10])

        else:
            if num == 10 or 20 <= num:
                total_letters += len(TENS[num // 10])

                num %= 10

            total_letters += len(DIGITS[num])

    total_letters += len('one') + len('thousand')

    print(f'Letters used in spelling out all integers from 1 to 1000 (inclusive):\n\n\t{total_letters}\n')

    # ********** Solution ends here ********** #

    # Stop tracking time and memory
    snapshot = tracemalloc.take_snapshot()
    end_time = time()
    tracemalloc.stop()

    # Print time elapsed and memory used
    print_time_elapsed(start_time, end_time)
    print_memory_usage_report(snapshot)


if __name__ == '__main__':
    main()
