import os
import sys
import ghostscript

def convert_eps_to_cmyk(input_file, output_file):
    args = [
        "-dNOPAUSE", "-dBATCH", "-dSAFER",
        "-sDEVICE=eps2write",
        "-sProcessColorModel=DeviceCMYK",
        "-dOverrideICC",
        "-sColorConversionStrategy=CMYK",
        "-dConvertCMYKImagesToK",  # Versucht Schwarz als 100% K zu speichern
        "-sOutputFile=" + output_file,
        input_file

    ]
    
    try:
        ghostscript.Ghostscript(*args)
        print(f"Konvertierung abgeschlossen: {output_file}")
    except Exception as e:
        print(f"Fehler bei der Konvertierung: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Verwendung: python convert_eps_cmyk.py <input.eps> <output.eps>")
        sys.exit(1)
    
    input_eps = sys.argv[1]
    output_eps = sys.argv[2]
    
    if not os.path.exists(input_eps):
        print("Fehler: Eingabedatei existiert nicht.")
        sys.exit(1)
    
    convert_eps_to_cmyk(input_eps, output_eps)
