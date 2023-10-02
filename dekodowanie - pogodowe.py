import csv
import openpyxl

def split_csv_to_excel(csv_filename, excel_filename):
    # Tworzymy nowy arkusz Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    with open(csv_filename, 'r', encoding='ANSI') as csvfile:  # Używamy kodowania UTF-8
        csv_reader = csv.reader(csvfile)
        for i, row in enumerate(csv_reader, start=1):
            # Rozbijamy komórkę względem przecinków i zapisujemy do arkusza Excel
            for j, value in enumerate(row, start=1):
                cell_values = value.split(',')
                for k, cell_value in enumerate(cell_values, start=1):
                    sheet.cell(row=i, column=j+k-1, value=cell_value)

    # Zapisujemy zawartość arkusza Excel do pliku
    workbook.save(excel_filename)

if __name__ == "__main__":
    csv_filename = "merged.csv"
    excel_filename = "wynik.xlsx"
    split_csv_to_excel(csv_filename, excel_filename)