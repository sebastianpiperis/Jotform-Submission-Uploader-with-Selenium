import save
import upload
import os



def main():
    subject = "Re: Test Form"
    data_list = save.save_attachments(subject)

    upload.uploadFile(data_list)

    


   
       

if __name__ == "__main__":
    main()
