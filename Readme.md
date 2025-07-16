# QR Code Generator

This repository contains a Python script to generate text/URL QR Codes and Wi‑Fi QR Codes interactively, with a terminal menu and PNG output.

---

## 📚 Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Examples](#examples)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- 🎯 **Interactive Mode** with a menu to choose between text/URL QR Codes and Wi‑Fi QR Codes.  
- 🔐 🚀 Wi‑Fi QR Code generation: enter SSID, security type (WPA/WEP/nopass), and password.  
- 🎨 Colored terminal output and icons using **Rich**.  
- 📦 Configurable PNG output file.  

---

## Requirements

- Python 3.7 or higher  
- [pip](https://pip.pypa.io/)  

---

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/qr-code-generator.git
   cd qr-code-generator
   ```

2. Install dependencies:  
   ```bash
   pip install qrcode[pil] rich
   ```

---

## Usage

1. To run in interactive mode:  
   ```bash
   python qrcode_generator.py -i
   ```

2. Follow the on-screen menu:

   ```
   🚀 Interactive QR Code Generator

   ┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
   ┃ Number ┃ QR Code Type     ┃
   ┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
   │   1    │ Text or URL      │
   │   2    │ Wi‑Fi            │
   └────────┴──────────────────┘

   Select an option [1/2]:
   ```

3. **Option 1 – Text or URL**  
   - Enter the text or URL to encode.  
   - Provide the output file name (default: `qrcode.png`).  

4. **Option 2 – Wi‑Fi**  
   - Provide the SSID (network name).  
   - Provide the password (leave empty for an open network).  
   - Choose the security type: `WPA`, `WEP`, or `nopass`.  
   - Provide the output file name (default: `wifi_qrcode.png`).  

5. The QR Code will be generated and saved in the current directory.  

---

## Examples

```bash
# Generate a text QR Code
python qrcode_generator.py -i
# → choose 1, enter https://example.com, save as example_qr.png

# Generate a Wi‑Fi QR Code
python qrcode_generator.py -i
# → choose 2, SSID: HomeNetwork, password: mypass123, security: WPA, save as wifi_qr.png
```

---

## Contributing

1. Fork this repository  
2. Create a feature branch: `git checkout -b feature/new-feature`  
3. Commit your changes: `git commit -m "Add new feature"`  
4. Push to the branch: `git push origin feature/new-feature`  
5. Open a Pull Request  

---

## License

This project is licensed under the [MIT License](LICENSE).
