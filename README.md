# 🔬 Keylogger Malware Research Lab

> A controlled red+blue team cybersecurity research project.  
> Built on Kali Linux | Python 3 | YARA | strace

## ⚠️ Disclaimer
This project is for **educational and research purposes only**.  
All testing was conducted in an **isolated local environment**.  
No live systems, real networks, or production environments were involved.

## 📋 Project Overview
End-to-end malware research cycle:
1. **Built** a Python keylogger as a controlled research sample
2. **Analyzed** it using static (strings, hashes) and dynamic (strace, /proc) techniques  
3. **Authored** 4 YARA detection rules validated against the sample
4. **Documented** findings in a professional threat intelligence report

## 🛠️ Tools Used
| Tool | Purpose |
|---|---|
| Python 3 + pynput | Sample development |
| strace | System call tracing |
| Wireshark | Network traffic analysis |
| YARA | Detection rule authoring |
| strings / sha256sum | Static analysis |

## 📁 Repository Structure
keylogger-research-lab/

├── keylogger.py                              # Research sample

├── analysis/

│   ├── keylogger_detection.yar              # 4 YARA detection rules

│   ├── strace_output.txt                    # Dynamic analysis trace

│   └── hashes.txt                           # SHA256 + MD5

├── reports/

│   └── Keylogger_Threat_Report.pdf          # Full threat intelligence report

└── logs/                                    # Sample output (gitignored in real use)


## 🎯 MITRE ATT&CK Mapping
- **T1056.001** — Input Capture: Keylogging

## 📄 Threat Intelligence Report
Full PDF report included in `/reports/` — covers static analysis,  
dynamic tracing findings, security findings, and YARA rule validation.

## 👤 Author
**Harshil Chheda** — M.Sc. Cybersecurity, BTU Cottbus | CEH v12  
[LinkedIn](https://linkedin.com/in/harshil-chheda-11783325b) · [GitHub](https://github.com/Harshil-chheda)
