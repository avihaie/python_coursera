"""
Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

max_value = 0
sender_count = dict()
name = raw_input("Enter file name:")
if len(name) < 1 :
    print "no file name inserted , default file mbox-short.txt will be used instead \n"
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "file name that was inserted was",name+"\nfile name invalid or does not exist\n","please check current directory for valid text file names"   
    exit() 
    
#create dictionary sender_count that counts each sender mail count 
for line in handle:
    if line.startswith('From ') == False :continue
    line_list = line.split()
    #print line_list[1]
    sender_count[line_list[1]] = sender_count.get(line_list[1],0) + 1

#print 'directory looks like this:',sender_count
for key,value in sender_count.items():
    if  value < max_value:continue
    max_key = key
    max_value = value

print max_key,max_value 
    



