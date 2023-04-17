from tkinter import filedialog, Tk
import os


def get_folder_dialog(initial_directory):
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(initialdir=initial_directory, title="Selecione uma pasta")
    return folder_path


# Exibe a caixa de diálogo de seleção de pasta e obtém a pasta selecionada
folder = get_folder_dialog(os.getcwd())
if not folder:
    print("Nenhuma pasta selecionada, por favor selecione uma pasta")
    exit()

# Obtém todos os arquivos .exe na pasta selecionada e os instala em fila
files = [f for f in os.listdir(folder) if f.endswith(('.exe', '.msi'))]
files.sort()
for file in files:
    print(f"Instalando arquivo {file} ...")
    os.startfile(os.path.join(folder, file))

print("Arquivos instalados com sucesso!")
