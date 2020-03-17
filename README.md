# Gerador de Certificados para Diretórios Acadêmicos

Este foi um projeto desenvolvido para o Diretório Acadêmico de Enfermagem da Universidade Feevale, mas que decidi compartilhar o código-fonte para também ajudar outras pessoas. Note que, por enquanto, será necessário ter alguns conhecimentos de programação para pode utiliza-lo da melhor maneira. Sugiro que você chame algum amigo(a) que entenda o básico e tenho certeza que tudo vai dar certo! :)

## Como utilizar?

1. O primeiro passo é configurar a conta de e-mail do seu diretório para aceitar aplicativos menos seguros. Como a aplicação que desenvolvi (assim como qualquer outra desenvolvida por um mero mortal) não é "assinada digitalmente" ou que possui alguma conexão encriptada, será necessário habilitar aplicativos menos seguro. Clique [aqui](https://myaccount.google.com/security) e desative a opção **Acesso a app menos seguro**.

2. Agora você precisa clonar este repositório para poder utilizar.

```
$ git clone https://github.com/mateusmuller/gerador_certificados
$ cd gerador_certificados
```

3. Agora, você precisa criar um arquivo chamado **credenciais.json** com as seguintes informações:

```
{
    "e-mail" : "seuemail@gmail.com",
    "senha" : "suasenha",
    "servidor_smtp" : "smtp.gmail.com",
    "porta_smtp" : 587,
    "e-mail_titulo" : "Certificados da Palestra XXX",
    "e-mail_corpo" : "Segue o e-mail em anexo.",
    "planilha_participantes" : "lista_participantes.xlsx",
    "foto_template_certificado" : "template_certificado.png"
}
```

Mude os parâmetros conforme o nome dos seus arquivos.

4. Coisas que você precisa se atentar: A imagem do certificado e o arquivo de Excel.

* A imagem do certificado sempre se chama **template_certificado.png**, então renomeie o seu arquivo para o mesmo nome e coloque nessa pasta.
* O arquivo de Excel sempre se chama **lista_participantes.xlsx**, então você também pode renomear. Outra coisa interessante é que sempre segue o mesmo padrão, onde a coluna 1 é e-mail, coluna 2 é o nome completo e a coluna 3 é o nome que deve aparecer no certificado.
* Na linha 20 é definido a posição do nome que será escrito (640,1000). Talvez você precise mudar isso, dependendo do tamanho do seu certificado.

5. Finalizado, basta executar o script usando Docker (por conta das dependências):

```
$ docker build -t gerador_certificados:latest .
$ docker run --rm -v $(pwd)/credenciais.json:/app/credenciais.json gerador_certificados:latest
```

**OBS:** Usei o -v para passar o arquivo de credenciais, caso contrário, você teria que criar uma nova imagem a cada atualização neste arquivo.

## Dicas

Sugiro usar o Google Forms para gerar o formulário de inscrição das palestras e depois só baixar o .xlsx e atribuir ao script.

## Licença

Este projeto está sob a licença do MIT - Veja [LICENSE](LICENSE) para mais detalhes.

## Updates

As próximas atualizações serão:

1. Usar o arquivo de credencias como JSON.
2. Usar docker volumes para transportar o arquivo de credenciais.
