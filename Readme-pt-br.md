# QR Code Generator

Este repositório contém um script Python para gerar QR Codes de texto/URL e QR Codes de Wi-Fi de forma interativa, com menu no terminal e saída em PNG.

---

## 📚 Sumário

- [Funcionalidades](#funcionalidades)  
- [Pré-requisitos](#pré-requisitos)  
- [Instalação](#instalação)  
- [Uso (PT-BR)](#uso-pt-br)  
- [Usage (EN)](#usage-en)  
- [Exemplos](#exemplos)  
- [Contribuição](#contribuição)  
- [Licença](#licença)  

---

## Funcionalidades

- 🎯 **Modo Interativo** com menu para escolher entre QR Code de texto/URL e QR Code de Wi-Fi.  
- 🔐 🚀 Geração de QR Code Wi-Fi: insira SSID, tipo de segurança (WPA/WEP/nopass) e senha.  
- 🎨 Terminal colorido e com ícones usando **Rich**.  
- 📦 Saída em arquivo PNG configurável.  

---

## Pré-requisitos

- Python 3.7 ou superior  
- [pip](https://pip.pypa.io/)  

---

## Instalação

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/qr-code-generator.git
   cd qr-code-generator
   ```

2. Instale as dependências:  
   ```bash
   pip install qrcode[pil] rich
   ```

---

## Uso (PT-BR)

1. Para rodar em modo interativo:  
   ```bash
   python qrcode_generator.py -i
   ```

2. Siga o menu no terminal:

   ```
   🚀 Interactive QR Code Generator

   ┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
   ┃ Number ┃ QR Code Type     ┃
   ┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
   │   1    │ Text or URL      │
   │   2    │ Wi-Fi            │
   └────────┴──────────────────┘

   Select an option [1/2]:
   ```

3. **Opção 1 – Texto ou URL**  
   - Digite o texto ou URL a ser codificado.  
   - Informe o nome do arquivo de saída (padrão: `qrcode.png`).  

4. **Opção 2 – Wi-Fi**  
   - Informe o SSID (nome da rede).  
   - Informe a senha (deixe vazio para rede aberta).  
   - Escolha o tipo de segurança: `WPA`, `WEP` ou `nopass`.  
   - Informe o nome do arquivo de saída (padrão: `wifi_qrcode.png`).  

5. O QR Code será gerado e salvo no diretório atual.  


## Exemplos

```bash
# Gerar QR Code de texto
python qrcode_generator.py -i
# → escolha 1, digite https://example.com, salve como example_qr.png

# Gerar QR Code de Wi-Fi
python qrcode_generator.py -i
# → escolha 2, SSID: HomeNetwork, senha: mypass123, segurança: WPA, salve como wifi_qr.png
```

---

## Contribuição

1. Fork este repositório  
2. Crie uma branch feature: `git checkout -b feature/nova-funcionalidade`  
3. Commit suas alterações: `git commit -m "Adicionar nova funcionalidade"`  
4. Push para a branch: `git push origin feature/nova-funcionalidade`  
5. Abra um Pull Request  

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
