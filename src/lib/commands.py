import json
import requests
from lib.validate import *

description = "\nDesenvolvedor: @spartancode 🎃\n\nO bot está em fase de desenvolvimento, em breve teremos mais opções. 🔰"

def help(update, context):
    link = "https://lh4.googleusercontent.com/tXrO-to4E1DfdlcCVLISdE0gx0nuDGlKRTJJwFeCHsj2hezu19qY1lOJJQVKlrRVXE8ZjmNpoZfZLnfavyT2=w1919-h946"
    text = f"Olá, {update.message.from_user.full_name}! 👤 Veja meus comandos abaixo:\n\n• /help\n• /cep 62375-000\n• /cnpj 00.360.305/0001-04\n• /fCNPJ 00.360.305/0001-04\n" + description
    context.bot.send_photo(chat_id=update.message.chat_id, photo=link, caption=text)

def cep(update, context):
    if len(context.args) != 1:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="[❗] Comando errado!\n\nVeja: /help.")
        return

    if valid_cep(context.args[0]) == False:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="[❗] CEP inválido!\n\nVeja: /help.")
        return

    response = requests.get(f"https://viacep.com.br/ws/{context.args[0]}/json")
    data = json.loads(response.content)

    text = "Consulta realizada pelo CEP. ✅\n\n"

    if data["localidade"] != "":
        text += f"• Cidade: {data['localidade']}\n"
    if data["uf"] != "":
        text += f"• Estado: {data['uf']}\n"
    if data["logradouro"] != "":
        text += f"• Endereço: {data['logradouro']}\n"
    if data["bairro"] != "":
        text += f"• Bairro: {data['bairro']}\n"
    if data["complemento"] != "":
        text += f"• Complemento: {data['complemento']}\n"
    if data["ibge"] != "":
        text += f"• IBGE: {data['ibge']}\n"
    if data["complemento"] != "":
        text += f"• Complemento: {data['complemento']}\n"
    if data["gia"] != "":
        text += f"• GIA: {data['gia']}\n"
    if data["ddd"] != "":
        text += f"• DDD: {data['ddd']}\n"
    if data["siafi"] != "":
        text += f"• SIAFI: {data['siafi']}\n"

    text += description
    context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=text)

def cnpj(update, context):
    if len(context.args) != 1:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="[❗] Comando errado!\n\nVeja /help.")
        return

    if valid_cnpj(context.args[0]) == False:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=f"[❗] CNPJ inválido!\n\nVeja: /help.")
        return

    delete = "./-"
    cnpj = context.args[0]

    for i in range(len(delete)):
        cnpj = cnpj.replace(delete[i], "")

    response = requests.get(f"http://receitaws.com.br/v1/cnpj/{cnpj}")
    data = json.loads(response.content)

    if data["status"] == "ERROR":
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=f"[❗] CNPJ \"{context.args[0]}\" rejeitado pela Receita Federal!\n")
        return

    text = "Consulta realizada pelo CNPJ. ✅\n\n"

    if data["nome"] != "":
        text += f"• Razão Social: {data['nome']}\n"
    if data["fantasia"] != "":
        text += f"• Fantasia: {data['fantasia']}\n"
    if data["situacao"] != "":
        text += f"• Situação: {data['situacao']}\n"
    if data["tipo"] != "":
        text += f"• Tipo: {data['tipo']}\n"
    if data["tipo"] != "":
        text += f"• EFR: {data['efr']}\n"
    if data["natureza_juridica"] != "":
        text += f"• Natureza Jurídica: {data['natureza_juridica']}\n"
    if data["porte"] != "":
        text += f"• Porte: {data['porte']}\n"
    if data["capital_social"] != "":
        text += f"• Capital Social: R$ {data['capital_social']}\n"
    if data['atividade_principal'][0]['text'] != "":
        text += f"• Atividade Principal: {data['atividade_principal'][0]['text']}\n"
    if data['atividade_principal'][0]['code'] != "":
        text += f"• Código: {data['atividade_principal'][0]['code']}\n"
    if data["municipio"] != "":
        text += f"• Cidade: {data['municipio']}\n"
    if data["uf"] != "":
        text += f"• Estado: {data['uf']}\n"
    if data["logradouro"] != "":
        text += f"• Endereço: {data['logradouro']}\n"
    if data["numero"] != "":
        text += f"• Número: {data['numero']}\n"
    if data["bairro"] != "":
        text += f"• Bairro: {data['bairro']}\n"
    if data["complemento"] != "":
        text += f"• Complemento: {data['complemento']}\n"
    if data["cep"] != "":
        text += f"• CEP: {data['cep']}\n"
    if data["cnpj"] != "":
        text += f"• CNPJ: {data['cnpj']}\n"
    if data["email"] != "":
        text += f"• E-mail: {data['email']}\n"
    if data["telefone"] != "":
        text += f"• Telefone: {data['telefone']}\n"
    if data["abertura"] != "":
        text += f"• Data de abertura: {data['abertura']}\n"
    if data["data_situacao"] != "":
        text += f"• Data de situação: {data['data_situacao']}\n"
    if data["ultima_atualizacao"] != "":
        text += f"• Última atualização: {data['ultima_atualizacao']}\n"

    text += f"\n[❗] Caso queira ver os funcionários da empresa, digite:\n\n/fCNPJ {context.args[0]}\n\nNão pude incluir essa função porque a mensagem ficaria muito grande e não poderia ser enviada.\n" + description
    context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=text)

def fCNPJ(update, context):
    if len(context.args) != 1:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="[❗] Comando errado!\n\nVeja /help.")
        return

    if valid_cnpj(context.args[0]) == False:
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=f"[❗] CNPJ inválido!\n\nVeja: /help.")
        return

    delete = "./-"
    cnpj = context.args[0]

    for i in range(len(delete)):
        cnpj = cnpj.replace(delete[i], "")

    response = requests.get(f"http://receitaws.com.br/v1/cnpj/{cnpj}")
    data = json.loads(response.content)

    if data["status"] == "ERROR":
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=f"[❗] CNPJ \"{context.args[0]}\" rejeitado pela Receita Federal!\n")
        return

    if data["qsa"][0]["qual"] == "" or data["qsa"][0]["nome"] == "":
        context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="[❗] Nenhum funcionário foi encontrado!")
        return

    text = "Consulta realizada pelo CNPJ (dados dos funcionários). ✅"

    for employee in data["qsa"]:
        text += f"\n\n• Cargo: {employee['qual']}\n• Nome: {employee['nome']}"

    text += "\n" + description
    context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text=text)

def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, reply_to_message_id=update.message.message_id, text="[❗] Comando inválido!\n\nVeja: /help.")
