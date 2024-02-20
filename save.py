import os
import win32com.client
import script

path = os.path.expanduser(r"C:/Users/sebas/Downloads/forms")  # location of file

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")  # opens outlook
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items


def save_attachments(subject):
    data_list = []  # Store data from multiple messages
    counter = 0
    for message in messages:
        if message.Subject == subject and message.Unread:  # Check if the message is both matching the subject and is unread
            for attachment in message.Attachments:
                # Get the submission ID from the attachment filename
                submissionID = os.path.splitext(attachment.FileName)[0]
                # Save the attachment file with the correct job number name
                job_number = script.get_submission_data(submissionID)['content']['answers']['4']['answer']
                attachment_filename = f"{job_number}.pdf"
                attachment_path = os.path.join(path, attachment_filename)
                attachment.SaveAsFile(attachment_path)
                print(f"File renamed in save to: {attachment_filename}")
                # Mark the email as read (no longer unread)
                message.Unread = False

                data = script.get_submission_data(submissionID)
                data_list.append(data)  # Store data in the list
                counter += 1
                print(f"counter: {counter}")
    return data_list
    
