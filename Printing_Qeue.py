import Queue
import random
import date
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimulationPrintingTasks.html

class printer: 
    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0
    
    def status(self):
        if self.current_task != None: return True
        else: return False
    
    def tick(self):
        if self.current_task != None:
            self.current_task = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None
            
    def start_next_job(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.pagerate

class print_task:

    def __init__(self, pages, time):
        self.pages = pages
        self.timestamp = time
    
    def get_pages(self):
        return self.pages
    
    def get_wait_time(self, current_time):
        return current_time - self.timestamp

def simulate_printer_lab(numseconds, pagesPerMinute)
    """
    @param numseconds to execute the simulation 
    @param number creates a printer with this speed
    """

    printer_queue = Queue.Queue()
    printer = Printer(pagesPerMinute)
    current_second = 0
    waiting_time = ""

    while current_second <= numseconds: 
        waiting_time = {}
        create_job = random.randint(0, 10)
        if create_job => 4: 
            printer_queue.enqueue(print_Task(random.randint(1,20), current_second))
        if printer.status == False
            current_task = printer_queue.dequeue()
            printer.start_next_job(current_task)
            waiting_time = 

            
##stopping workking on this to move on and do somethign else
# see here for more updates
#https://runestone.academy/runestone/books/published/pythonds/BasicDS/SimulationPrintingTasks.html