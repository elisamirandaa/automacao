import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p> Olá Elisa, </p>

    <p>O teste de automação está <b>concluído.</b></p>

    <p>Att, </p>

    <p>Elisa Miranda</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Automação de Email"
    msg['From'] = 'elisa.mirandaa@gmail.com'
    msg['To'] = 'elisa.mirandaa@gmail.com'
    password = 'vuyshuidhcrftjaq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    #login credentials for sending the email
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
