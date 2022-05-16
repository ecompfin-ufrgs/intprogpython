from openpyxl import Workbook

wb = Workbook()

for planilha in ["receitas", "despesas", "resultado"]:
    wb.create_sheet(planilha)

wb.save("orcamento.xlsx")
