#!/usr/bin/python3
""" Module to implement lockbox techniques
"""


def canUnlockAll(boxes):
    """ Function to check if all the boxes
    have the keys to open each other """

    box_keys = [0] * len(boxes)
    unlocked_boxes = 0

    # Unlock the first box
    box_keys[0] = 1
    unlocked_boxes += 1

    # Open all boxes as they unlock boxes
    for count in range(len(boxes)):
        # Set a value to use to monitor changes
        prev_unlocked = unlocked_boxes
        for box in range(len(boxes)):
            # Check if this box has a key saved or not
            if not box_keys[box]:
                continue
            # Save all the keys in the box
            keys = boxes[box]
            for x in keys:
                # Check if the key belongs to one of the boxes
                try:
                    box_keys[x] += 1
                except IndexError:
                    continue
                # If a box gets a key for the first time, its unlocked
                if box_keys[x] == 1:
                    unlocked_boxes += 1
        # Check if all boxes have been open, or if none were opened
        if ((prev_unlocked == unlocked_boxes) |
           (unlocked_boxes == len(boxes))):
            break
    # If any of the boxes haven't been opened
    if (0 in box_keys):
        return False
    return True
