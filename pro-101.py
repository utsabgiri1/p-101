import os 
import dropbox

class uploadFiles :
    def __init__(self , accessToken):
        self.aToken = accessToken

    def transferFiles(self , source , destination):
        db = dropbox.Dropbox(self.aToken)

        f = open(source , 'rb')
        
        db.files_upload(f.read() , destination)



def main():
    access_token = 'sl.BMewsGH_t7WHFANe93DzzyeeXrgq81IThVs8gc7YgRu1jX61Qcmv6Pq7N3gSB15aK44sUjHh7uvbGm6um4gu7bGiSsmZTGYhi_hTYcFIS_nTos2-fg4K5aFHsAgv7-hAXj-YYzN70hT5'
    transferData = uploadFiles(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    transferData.transferFiles(file_from, file_to)
    print("file has been moved !!!")


main()














