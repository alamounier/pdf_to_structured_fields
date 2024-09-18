import os 
import camelot
import pandas as pd
import matplotlib 
import matplotlib.pyplot as plt



file_name = 'corretora_jornada_de_dados (1)'
path = os.path.abspath(f"pdf/files/{file_name}.pdf")


tables = camelot.read_pdf(
    path,
    pages='1-end',
    flavor='stream',
    table_areas=['65, 558, 500, 298'], #área da tabela em cada uma de suas extremidades
    columns=['65, 107,156, 212, 280, 336, 383, 450'], #ponto de inicio de cada coluna
    strip_text=" .\n"
)

print(tables[0].parsing_report)

# camelot.plot(tables[0], kind="contour")
# plt.show()

print(tables[0].df)

print("Pause")