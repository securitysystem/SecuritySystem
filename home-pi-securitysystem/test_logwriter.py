import os
import datetime

now = datetime.datetime.now()
logs = '''
Test Log
'''+str(now)+'\n'
logfile = open('logfile.log','w+')
cc = logfile.read()
contents = cc+logs
logfile.write(contents)
logfile.close()
print(contents)

triggerPath = ''
if (os.path.isfile(triggerPath)):
    triggerFile = open(triggerPath,'w+')
    triggerFile.write(contents)
    triggerFile.close()
