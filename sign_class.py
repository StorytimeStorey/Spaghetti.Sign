# Class for the sign that students will be looking at
# Last edited 01-12-2023 by Jackson Loughmiller

import time
# things to add to sign class
# 
class sign_node:
    def __init__(self, image):
        self.image = image
        self.next = None

    def __repr__(self):
        '''
        Repr to return image
        '''
        return str(self.image)

class cycle_sign:

    # create the head of the list and current image, both default as None
    def __init__(self):
        self.head = None
        self.current_image = None

    def __repr__(self):
        '''
        repr method that returns each item in the linked list with arrows showing links
        '''
        str_to_return = str(self.head)
        current_node = self.head
        # loop through linked list and print each item in order with arrows pointing to their next value
        while current_node.next is not self.head:
            str_to_return += f' --> {current_node.next}'
            current_node = current_node.next
        return str_to_return

    # append function for linked list
    def append(self, image):
        '''
        append method for linked list, adds the input image to the end of the linked list, making the 
        image.next value self.head
        '''
        # if there is not a head, make the input image the head
        if not self.head:
            self.head = sign_node(image)
            self.head.next = self.head
        # if there is already a head, add the input image to the end of the linked list
        else:
            current = self.head
            # cycles to the end of the linked list, makes the input image the .next of the current last node and 
            #makes the input image.next the head
            while current.next != self.head:
                current = current.next
            new_node = sign_node(image)
            new_node.next = self.head
            current.next = new_node

    def cycle_image(self, viewing_time):
        '''
        
        '''
        self.current_image = self.head
        # loop through linked list, pausing for the inputted viewing time on each node. 
        while self.current_image:
            time.sleep(viewing_time)
            self.current_image = self.current_image.next
            if self.current_image == self.head:
                break

testing_sign = cycle_sign()
tracker = 0 
for thing in range(20):
    tracker += 1
    thing = sign_node(str(tracker))
    testing_sign.append(thing)
    print(thing)
print(testing_sign)


