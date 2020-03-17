#!/usr/bin/env python3

from xlrd import open_workbook,cellname
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import re
import json

class Certificate_Generator ():
    def __init__ (self):
        credentials_file = open("credentials.json","r")
        data_credentials_file = json.load(credentials_file)
        self.email                        = data_credentials_file["email"]
        self.password                     = data_credentials_file["password"]
        self.smtp_server                  = data_credentials_file["smtp_server"]
        self.smtp_port                    = data_credentials_file["smtp_port"]
        self.email_subject                = data_credentials_file["email_subject"]
        self.email_body                   = data_credentials_file["email_body"]
        self.students_sheet               = data_credentials_file["students_sheet"]
        self.picture_certificate_template = data_credentials_file["picture_certificate_template"]
        credentials_file.close()

    def generate_certificate (self, certificate_name, file_name): 
        certificate_file_name  = "certificate_" + file_name.replace(" ","_") + ".png"
        certificate_image      = Image.open(self.picture_certificate_template)
        certificate_image_draw = ImageDraw.Draw(certificate_image)
        certificate_font       = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 200, encoding="unic")
        certificate_image_draw.text((640,1000), certificate_name, font=certificate_font, fill=(0,0,0))
        certificate_image.save(certificate_file_name, "PNG", resolution=100.0)
        return certificate_file_name

    def send_email (self, email_to, certificate_name):
        msg = MIMEMultipart()
        msg['From']    = self.email
        msg['To']      = email_to
        msg['Subject'] = self.email_subject
        msg.attach(MIMEText(self.email_body, 'plain'))
        attachment = open(certificate_name, "rb")
        part = MIMEBase('image', 'png')
        part.set_payload(attachment.read())
        part.add_header('Content-Disposition', 'attachment', filename=certificate_name)
        encoders.encode_base64(part)
        msg.attach(part)
        email_text = msg.as_string()
        self.smtp_connection.sendmail(self.email, email_to, email_text)
    
    def smtp_connect(self):
        try:
            self.smtp_connection = smtplib.SMTP(self.smtp_server, self.smtp_port)
            self.smtp_connection.set_debuglevel(2)
            self.smtp_connection.starttls()
            self.smtp_connection.login(self.email, self.password)
            print("Connected.")
        except Exception as e:
            print(e)

    def read_sheet (self):
        self.smtp_connect()
        students_sheet = open_workbook(self.students_sheet) # Which Excel file?
        page_students_sheet = students_sheet.sheet_by_index(0) # Which page of the sheet?
        for line_students_sheet in range(1,page_students_sheet.nrows):
            student_certificate_name = page_students_sheet.row_values(line_students_sheet)[3] # Column 3
            student_file_name        = page_students_sheet.row_values(line_students_sheet)[2] # Column 2
            student_email            = page_students_sheet.row_values(line_students_sheet)[1] # Column 1
            certificate_name = self.generate_certificate(student_certificate_name, student_file_name) 
            self.send_email(student_email, certificate_name) 

if __name__ == "__main__":
    certificate_generator = Certificate_Generator()
    certificate_generator.read_sheet()