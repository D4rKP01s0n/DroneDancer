#########################################################################
#     search.py - A python script which makes Parrot drones dance.
#     Author - D4rKP01s0n
#     Requirements - wifi
#########################################################################


#########################################################################
#     Change these variables
interface = 'wlan0' # Managed wifi interface (monitor-mode is not used, as a wifi network scan is substituted for a packet scan)
#########################################################################


import logging
import time
from wifi import Cell, Scheme
#import subprocess

#class colors: # These allow for color-coded output
#    HEADER = '\033[95m'    #    An example of using this would be as follows
#    OKBLUE = '\033[94m'    #    print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
#    OKGREEN = '\033[92m'   #    Credit: Joeld of StackOverflow: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'       #    End every colored line with this, or else everything following will be the same color
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'


def main():
    try:
        # Set up basic logging
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='dronedance.log',level=logging.DEBUG) #setup logging to file
        logging.info('\n'+'Drone Discovery Initialized'+ '\n') #announce that it has started to log file with yellow color
    except:
        print('Failed to set up logging')
    try:
        print('\n' + '\033[93m' + 'Drone Discovery Initialized' + '\033[0m' + '\n') #announce that it has started to command line with yellow color
        while 1=1:
            # Scan
            networks = Cell.all(interface) # Has to be run as root
    except KeyboardInterrupt:
        print('Stopping')
        
if __name__ == '__main__':
    main()
