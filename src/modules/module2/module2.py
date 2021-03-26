from logs import logDecorator as lD 
import jsonref, pprint

from modules.module2 import utils

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module2.module2'


@lD.log(logBase + '.doSomething')
def doSomething(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''

    print('We are in module2')
    utils.func1()
    

    return

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for module2
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''

    print('='*30)
    print('Main function of module2')
    print('='*30)
    print('We get a copy of the result dictionary over here ...')
    pprint.pprint(resultsDict)

    doSomething()

    print('Getting out of module2')
    print('-'*30)

    return

