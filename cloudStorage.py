import dropbox

class TransferData:
    def __init__(self,access_token):
       self.access_token=access_token   
    def uploadFile(self,filefrom,fileto):
        #link the our dropbox account to the application
        dx=dropbox.Dropbox(self.access_token)
        file = open(filefrom,'rb')
        #upload these contents to the dropbox using the files_upload() method
        dx.files_upload(file.read(),fileto)
        
def main():
    access_token = "sl.BF2umM3B2XVFJzrzavDDyi4I3Q4vuRa84IoY30zFU3ReUS-5BY9tTAmcW8wauHkAWCprqSLUEyr4kA0RmMiIqiYhSohLtZ5FOlgsGEGBWNp0CdRfTGDcVFpYFxrSFFVoGPFl3ZChhYI"
    td = TransferData(access_token)
    file_from = input("enter file transfer : ")
    file_to = input("enter file path : ")
    td.uploadFile(file_from,file_to)
    print("files have been moved successfully")
    
main()