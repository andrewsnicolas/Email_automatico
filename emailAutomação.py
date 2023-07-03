import smtplib
import email.message

with open("./arquivos/Lista-De-Emails.txt", "r", encoding="utf-8") as arquivo:
    matriz = arquivo.readlines()
    nome = []
    emails = []
    n1 = ((len(matriz)) / 2) - 1
    for n2 in range(0, (len(matriz) - 1), 2):
        nome.append(matriz[n2])
        emails.append(matriz[(n2 + 1)])
    print(nome)
    print(emails)
for repetir in range(0, int(n1 * 2), 1):
    corpo = f"""<h1>Olá {nome[repetir]}! Tudo bem?</h1>\n<p>Gostariamos de te propor uma proposta de emprego na nossa empresa,\nsomos
    uma empresa que promete evoluir na programação e que querem ser melhores e evoluirem, você terá ajuda de instrutores\n
    para seus códigos, queremos a evolução sua e que você prospere! Retorne aqui pretender se aceitar!</p>"""
    msg = email.message.Message()
    msg["Subject"] = "Uma proposta de emprego!"
    msg["From"] = "xxxxxxxxxxxxxxxxxxxxxxxx"
    msg["To"] = emails[repetir]
    senha = "xxxxxxxxxxxxxxxxxxxx"
    msg.add_header("Content-Type", "text/html")
    msg.set_payload(corpo)
    extensão = smtplib.SMTP("smtp.gmail.com: 587")
    extensão.starttls()
    extensão.login(msg["From"], senha)
    extensão.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    print("enviado")
