import subprocess
import os
import re

class PdfConverter:
  def __init__(self, original_excel_file: str) -> None:
    if not os.path.isfile(original_excel_file):
      raise FileNotFoundError
    if not re.search(r'.xlsx$', original_excel_file):
      raise Exception("Please input .xlsx format file")
    self.__base_name: str = os.path.splitext(os.path.basename(original_excel_file))[0]

  def convertExcelToPdf(self) -> None:
    cmd: list = []
    cmd.append("libreoffice")
    cmd.append("--headless")
    cmd.append("--nologo")
    cmd.append("--nofirststartwizard")
    cmd.append("--convert-to")
    cmd.append("pdf")
    cmd.append("--outdir")
    cmd.append("/app/files")
    cmd.append(f"/app/files/{self.__base_name}.xlsx")
    subprocess.run(" ".join(cmd), shell=True)

  def __pdfCompress(self) -> None:
    cmd: list = []
    cmd.append("-sDEVICE=pdfwrite")
    cmd.append("-dPDFSETTINGS=/printer")
    cmd.append("-dBATCH")
    cmd.append("-dNOPAUSE")
    cmd.append("-dSAFER")
    cmd.append(f"-sOUTPUTFILE=/app/files/{self.__base_name}.pdf")
    cmd.append(f"/app/files/{self.__base_name}.pdf")

    # ghostscript.Ghostscript(*cmd)

if __name__ == "__main__":
  pdfConverter = PdfConverter("./files/SA.xlsx")
  pdfConverter.convertExcelToPdf()
  