#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across range() to generate n UUIDs"""

# standard library import
# allows us to generate UUIDs
import uuid

def main():
    howmany = input("How many UUIDs should be generated? ")
    if not howmany.isdigit():
        print("Please enter numeric ")
        return

    print("Generating UUIDs...")

    # range is required because an int cannot be looped
    howmany = int(howmany)
    for rando in range(howmany):
        print( uuid.uuid4() )   # each time through the loop produce a UUID

if  __name__ == "__main__":
    main()

