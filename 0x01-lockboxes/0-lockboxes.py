#usr/bin/python3
""" Module to implement lockbox techniques
"""

def canUnlockAll(boxes):
    box_keys = [0] * len(boxes)
    unlocked_boxes = 0

    # Unlock the first box
    box_keys[0] = 1
    unlocked_boxes += 1

    # Open all boxes as they unlock boxes
    for count in range(len(boxes)):
        prev_unlocked = unlocked_boxes
        print(prev_unlocked)
        for box in range(len(boxes)):
            if not box_keys[box]:
                continue
            keys = boxes[box]
            for x in keys:
                box_keys[x] += 1
                if box_keys[x] == 1:
                    unlocked_boxes += 1
        if ((prev_unlocked == unlocked_boxes) | (unlocked_boxes == len(boxes))):
            break

    print(unlocked_boxes)

    if (0 in box_keys):
        return False
    return True
