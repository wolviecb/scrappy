"""email related codes"""
def email(body, sub, dest, gmail_passwd):
    """send email about the status through gmail"""
    import smtplib
    subj = 'Passport Status ' + sub
    text = '\n'.join(body)
    raw_email = '\r\n'.join(['From: %s' % dest, 'To: %s' % dest, 'Subject: %s' % subj, '', text])
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(dest, gmail_passwd)
    server.sendmail(dest, dest, raw_email.encode("utf_8"))
    server.quit()
