#Kanv Kumar:-)
import smtplib,os
from getpass import getpass#to get password
from email import Encoders
from email.MIMEMultipart import MIMEMultipart#for sending
from email.MIMEBase import MIMEBase#for sending
from email.MIMEText import MIMEText#for sending
from email.Utils import formatdate,COMMASPACE#for sending


def mailscript(send_from,send_to,subject,text,files=[]):#send
	msg=MIMEMultipart()#dictionary
	msg['From']=send_from
	msg['To']=COMMASPACE.join(send_to)
	msg['Date']=formatdate(localtime=True)
	msg['subject']=subject

	msg.attach(MIMEText(text))#attaches text
	try:
		for f in files:
			part=MIMEText('application', "octet-stream")
			part.set_payload(open(f,"rb").read())
			Encoders.encode_base64(part)#encoding to quoted plain-text format
			part.add_header('Content-Disposition', 'attachment; filename="%s"'%os.path.basename(f))
			msg.attach(part)

	except:
		print 'There is some error in attaching given attachments.'			

	server=smtplib.SMTP('smtp.gmail.com:25')#port 587
	server.starttls()#start server
	server.login(username,password)#login
	server.sendmail(fromaddr,toaddrs,msg.as_string())
	server.quit()

def checkpath(p):# to check file path
	command="if [ -f "+p+" ]; \nthen\necho '1' \nelse\n echo '0'\nfi"
	return int(os.popen(command).read())

def takeattach():#attachments
	lst=[]
	ans=raw_input("Do you want to attach something ?(y/n): ")
	while ans=='y':
		p=raw_input("Enter file path to attach: ").strip()#white spaces removed
		if checkpath(p):
			lst.append(p)
		ans=raw_input("Do you want to attach more(y/n): ")
	return lst


username=fromaddr=raw_input("Enter username: ")#from
password=getpass()

toaddrs=raw_input("Enter list of recipents separated by a comma: ").split(',')#to



subject=raw_input("Enter subject of mail:")#subject
z=raw_input("Enter Mail Body(press Enter to start):")
os.system('sublime-text temp3.txt')# using editor
text=open('temp3.txt').read()#text
attachments=takeattach()#attachments
print 'Sending Mail......'
mailscript(fromaddr,toaddrs,subject,text,attachments)
os.system('rm temp3.txt')
print 'Mail Sent to ' + ','.join(toaddrs)
