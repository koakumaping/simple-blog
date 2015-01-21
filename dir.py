import os
import os.path
import MySQLdb

rootdir = 'D:\Desktop\EE'

conn = MySQLdb.connect(host = '127.0.0.1', user = 'twifi', passwd = 'twifi123$', db = 'twifi_dev')
cur = conn.cursor()

for parent, dirnames, filenames in os.walk(rootdir):
    
    
    for dirname in dirnames:
        print 'parent is:' + parent
        print 'dirname is:' + dirname
        
    for filename in filenames:
        if 'html' in filename:
            print 'parent is:' + parent
            print 'filename is:' + filename
            print 'the full name of file is:' + os.path.join(parent, filename)
            
cur.execute('select * from informations')
result = cur.fetchall()
print result
conn.close()