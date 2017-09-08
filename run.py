#!/usr/bin/env python3
"""checka a porra toda"""
from sys import argv
from scrappy import check

try:
    DEST = argv[3]
    PASSWD = argv[4]
except IndexError:
    DEST = "0"
    PASSWD = "0"

try:
    CPF = argv[1]
    PROTO = argv[2]
    URL = "https://servicos.dpf.gov.br/sinpa/consultarSituacaoSolicitacao.do\
?dispatcher=consultarSituacaoSolicitacao&protocolo=" + PROTO + "&cpf=" + CPF + "\
&email1=&email2=&url="
    check(URL, DEST, PASSWD)
except IndexError:
    print("Usage %s CPF protocol [email passwd]", argv[0])
