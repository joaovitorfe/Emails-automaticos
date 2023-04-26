import smtplib

# Informações do remetente
remetente_email = 'seu_email@gmail.com'  # Insira seu endereço de e-mail
remetente_senha = 'sua_senha'  # Insira sua senha de e-mail

# Lista de destinatários
destinatarios_email = ['destinatario1@example.com', 'destinatario2@example.com', 'destinatario3@example.com']

# Configurações do servidor SMTP do Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Criação do objeto SMTP
smtp_obj = smtplib.SMTP(smtp_server, smtp_port)

# Inicia a conexão com o servidor SMTP
smtp_obj.ehlo()

# Habilita a criptografia TLS
smtp_obj.starttls()

# Efetua o login no servidor SMTP
smtp_obj.login(remetente_email, remetente_senha)

# Cria o corpo do e-mail
assunto = 'Assunto do e-mail'
corpo = 'Olá, destinatários! Este é um e-mail de teste enviado usando Python.'
mensagem = f'Subject: {assunto}\n\n{corpo}'

# Envia o e-mail para cada destinatário na lista
for destinatario_email in destinatarios_email:
    smtp_obj.sendmail(remetente_email, destinatario_email, mensagem)

# Encerra a conexão com o servidor SMTP
smtp_obj.quit()

print('E-mails enviados com sucesso!')