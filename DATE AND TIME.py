#Program  to display DATE and TIME
import time

localtime = time.asctime( time.localtime( time.time()))
globaltime = time.asctime( time.gmtime( time.time()))

print( "The Local Time is :",localtime)
print( "The Global Time is :",globaltime)