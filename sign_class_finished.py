# Class for the sign that students will be looking at
# Last edited 01-12-2023 by Jackson Loughmiller
# things to add to sign class
# 
class sign_node:
    def __init__(self, image):
        '''
        '''
        self.image = image
        self.next = None

    def __repr__(self):
        '''
        Repr to return image
        '''
        return str(self.image)

class cycle_sign:
 
    def __init__(self, viewing_time: int, run_time: int, is_running = False):
        '''
        inputs:
        viewing_time - determines how many simulated seconds an image stays on the sign
        run_time - determines how many weeks to cycle for
        is_running - determines if the sign is cycling or not, True means it is, False it is not. Default to False.
        '''
        # create the head of the list and current image, both default as None.
        self.head = None
        self.current_image = None
        self.viewing_time = viewing_time
        self.run_time = run_time
        self.is_running = is_running

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

    def cycle_image(self):
        '''
        Cycles through the images, leaving each image as current_image for [viewing time] 
        '''
        global cycle_time
        cycle_time = 0
        self.current_image = self.head
        # tracks number of weeks passed during the current runtime
        self.num_weeks = 0
        # loop through linked list, pausing for the inputted viewing time on each node. 
        while self.is_running:
            for second in range (604801):
                self.current_second = second
                # move to the next image every [viewing_time] increments
                # print(self.current_image)
                if second%self.viewing_time == 0:
                    self.current_image = self.current_image.next
                    cycle_time = 0
                else:
                    cycle_time += 1
            self.num_weeks += 1
            # stop cycling once desired run_time is reached
            if self.num_weeks == self.run_time:
                self.is_running = False


testing_sign = cycle_sign(5, 1, True)
tracker = 0 
for thing in range(20):
    tracker += 1
    bro = sign_node(tracker)
    testing_sign.append(bro)
testing_sign.cycle_image()
    # print(testing_sign.current_image)


# testing_sign.cycle_image()
# print(testing_sign)


