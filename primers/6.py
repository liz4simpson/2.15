#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # open the text.txt in append mode. Create a new file if no such file exists.
    with open("text.txt", "w", encoding="utf-8") as fileptr:
        # appending the content to the file
        print(
            "UTF-8 is a variable-width character encoding used for electronic communication.",
            file=fileptr
        )
    print(
            "UTF-8 is capable of encoding all 1,112,064 valid character code points.",
            file=fileptr
    )
    print(
            "In Unicode using one to four one-byte (8-bit) code units.",
            file=fileptr
    )
