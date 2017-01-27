fh = open("text.txt", "x")

fh.write("Þetta er prufa ")
fh.write("Má ég fara heim ")

fh.close()

fh = open("text.txt", "a")

fh.write("Þetta er að bætast við ")
fh.write("Þetta er líka bæting ")
fh.write("Forritun er skemmtileg")

fh.close()
