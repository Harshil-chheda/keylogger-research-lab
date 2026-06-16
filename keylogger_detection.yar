import "hash"

/*
    YARA Rule Set: Keylogger Detection
    Author: Harshil Chheda
    Project: Keylogger Malware Research Lab
    Date: 2026-06-16
    Description: Detection rules derived from static + dynamic analysis
                 of a Python-based keylogger research sample
    SHA256: 1c23f8cc07dc8d548493b836e5345e8ce342ab1465d260a67dd53613eab28a60
*/

rule Keylogger_Research_Sample_Exact {
    meta:
        description   = "Matches exact research keylogger sample by hash"
        author        = "Harshil Chheda"
        severity      = "HIGH"
        sample_sha256 = "1c23f8cc07dc8d548493b836e5345e8ce342ab1465d260a67dd53613eab28a60"

    condition:
        hash.sha256(0, filesize) == "1c23f8cc07dc8d548493b836e5345e8ce342ab1465d260a67dd53613eab28a60"
}

rule Python_Keylogger_Pynput_Hook {
    meta:
        description = "Detects Python scripts using pynput for keyboard interception"
        author      = "Harshil Chheda"
        severity    = "HIGH"
        technique   = "T1056.001 - Input Capture: Keylogging (MITRE ATT&CK)"

    strings:
        $import_pynput = "from pynput import keyboard" ascii
        $listener      = "keyboard.Listener"           ascii
        $on_press      = "on_press"                    ascii
        $key_char      = "key.char"                    ascii

    condition:
        $import_pynput and 2 of ($listener, $on_press, $key_char)
}

rule Keylogger_FileWrite_Pattern {
    meta:
        description = "Detects keylogger log file write behaviour"
        author      = "Harshil Chheda"
        severity    = "MEDIUM"
        note        = "May FP on legitimate loggers — combine with Rule 2"

    strings:
        $logfile    = "keylog.txt" ascii nocase
        $write_mode = "\"a\""      ascii
        $log_path   = "logs"       ascii
        $timestamp  = "strftime"   ascii

    condition:
        $logfile and $write_mode and ($log_path or $timestamp)
}

rule Generic_Python_Input_Capture {
    meta:
        description   = "Broader rule — catches Python scripts doing input capture + file write"
        author        = "Harshil Chheda"
        severity      = "MEDIUM"
        falsepositive = "Legitimate accessibility tools, macro recorders"

    strings:
        $pynput     = "pynput"    ascii
        $keyboard   = "keyboard"  ascii
        $file_write = "open("     ascii
        $append     = "\"a\""     ascii
        $listener2  = "Listener"  ascii

    condition:
        $pynput and $keyboard and $file_write and $append and $listener2
}
