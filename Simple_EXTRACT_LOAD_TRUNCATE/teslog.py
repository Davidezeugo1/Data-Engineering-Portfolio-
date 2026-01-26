#import logging

#ogging.basicConfig(filename="logs.log",
#                   level=logging.DEBUG,
#                    format= '%(asctime)s - %(levelname)s - %(message)s',
#                    filemode='w')


#logger=logging.getLogger(__name__)
#handler=logging.FileHandler('test.log')
#formatter= logging.Formatter( '%(asctime)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)



#logging.debug("show debug messagey")
#logging.info("Show INFO as messgaey")
#logging.warning("Show WARNING as messagey")
#logging.error("Show ERROR as messagey")
#logging.critical("Show CRITICAL as messagey")

#logger.info('test the new loggery')

import logging 

# Basic logging configuration
logging.basicConfig(
    filename="logs.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # Append to the file
)

# Create a logger instance
Datalog = logging.getLogger(__name__)  
Datalog.propagate = False  

# Optional: Add an extra file handler if needed
Datalog.setLevel(logging.DEBUG) 
handler=logging.FileHandler('test.log', mode='w',)
formatter= logging.Formatter( '%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
Datalog.addHandler(handler) 

logging.info("lOVE LOVE LOVE i love me a good sandwhich")
Datalog.info("HATE HATE HATE usong this show")


logging.info("high street")
Datalog.info("middel school")

logging.info("jump high ")
Datalog.info("i need a chicken") 

num=4+6
Datalog.debug(f'what is 4+6:{num}')
Datalog.info(f'The number your looking for is {num}')

