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
        prev_unlocked = unlocked_boxes
        for box in range(len(boxes)):
            if not box_keys[box]:
                continue
            keys = boxes[box]
            for x in keys:
                try:
                    box_keys[x] += 1
                except IndexError:
                    continue
                if box_keys[x] == 1:
                    unlocked_boxes += 1
        if ((prev_unlocked == unlocked_boxes) |
           (unlocked_boxes == len(boxes))):
            break

    if (0 in box_keys):
        return False
    return True
