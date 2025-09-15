import re
text = """Hello,  
You can contact me on +1 (555) 123-4567 or on my UK number +44 20 7946 0958 or on my Egypt number +20 1234567891.  
My main email is john.smith@gmail.com and another one is support.team@company.org.  
For sales inquiries, write to sales@shop-example.net or call us at +20 100 123 4567.  
Visit our website at https://www.example.org or check the portal at http://localhost:3000/. 
My friend Maria lives at 123 Example Street, Apt 4B, New York, NY, 10001, USA.  
Her email is maria.garcia@correo.es and her backup email is maria.g@university.edu.eg 
Another colleague Ivan can be contacted via ivan.petrov@example.ru and his phone is +7 495 123-45-67.  
Our Egypt office is located at 12 Nile Street, Building 5, Floor 2, Cairo, 11511, Egypt.  
If needed, send files to files@datahub.example.com or open http://datahub.example.com/upload.  
HR team uses hr@company-example.com and phone +971 50 123 4567.  
The Paris office is at 3 Rue de l’Exemple, 75001 Paris, France.  
You can also call our backup line at 020-7946-0011 or email backup@archive.example.co.  
Emergency contact is +33 612 345 678 and email emergency@service.fr.  
For payments use payments@fin-example.com, website https://fin-example.com/pay, or call +49 30 123456.  
John Doe’s personal email is john.doe@example.com and his Canadian number is +1-800-555-1212.  
Check the blog at https://blog.example.com/2025/09/15/article-title or write to webmaster@site-example.com.  
Our Dubai office is at P.O. Box 1234, Downtown, Dubai, UAE, 00000.  
For registry information, contact registry@example.org or phone +61 2 1234 5678.  
Customer care can be reached at care@support-example.io and hotline +91 98765 43210.  
"""
def re_expres(pattern,string):
    for match in re.finditer(pattern,string):
        print(match.group())
pattern_phone=r"\+\d[\d\s\-\(\)]{7,}"  
pattern_emails=r"\w+[\.\@]\w+[\@\-]\w+(\.\w+)+"
pattern_URL=r"https?://[^\s]+" 
print(f"This All phones.\n{re_expres(pattern_phone,text)}")    
print(f"This All Emails.\n{re_expres(pattern_emails,text)}")  
print(f"This All URL.\n{re_expres(pattern_URL,text)}")