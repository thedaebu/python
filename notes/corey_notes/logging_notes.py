## logging

# import logging module
import logging
# basicConfig method changes configurations for logging
# filename is file where logs get saved
# level changes debugging level (debug, info, warning, error, critical)
# format changes format of logs saved
logging.basicConfig(filename='test_log.log', level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

def getSum(args):
    summ = 0
    for i in range(len(args)):
        summ += args[i]

    return summ

result = getSum([1,2,3,4,5])
logging.debug(f'result is {result}')