from logs import logDecorator as lD 
import jsonref, pprint

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.module3.module3'

from modules.module3 import utils

configM = jsonref.load(open('../config/modules/module3.json'))['params']


@lD.log(logBase + '.doSomething')
def doSomething(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''

    print('We are in module3')
    utils.func3()
    print( configM )

    return

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for module3
    
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
    print('Main function of module3')
    print('='*30)
    print('We get a copy of the result dictionary over here ...')
    pprint.pprint(resultsDict)

    if configM['TODO']['func1']:
        utils.func1()
    if configM['TODO']['func2']:
        utils.func2()
    if configM['TODO']['func3']:
        utils.func3()

    print('Getting out of module3')
    print('-'*30)

    return

