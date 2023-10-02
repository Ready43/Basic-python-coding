import os
import csv

def merge_csv_files(input_folder, output_file):
    # Sprawdzenie, czy folder istnieje
    if not os.path.exists(input_folder):
        print(f"Folder '{input_folder}' nie istnieje.")
        return

    # Lista przechowująca dane do scalenia
    data_to_merge = []

    # Przeglądanie plików w folderze
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            with open(file_path, "r", encoding="ansi") as csv_file:
                # Odczytanie zawartości pliku CSV i dodanie go do listy danych
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    data_to_merge.append(row)

    # Zapisanie scalonych danych do nowego pliku CSV
    with open(output_file, "w", newline="", encoding="ansi") as output_csv:
        csv_writer = csv.writer(output_csv)
        csv_writer.writerows(data_to_merge)

    print(f"Pliki CSV z folderu '{input_folder}' zostały scalone w pliku '{output_file}'.")

if __name__ == "__main__":
    # Nazwa folderu, w którym znajdują się pliki CSV
    input_folder = "."  # "." oznacza bieżący folder

    # Nazwa pliku wynikowego
    output_file = "merged.csv"

    merge_csv_files(input_folder, output_file)
