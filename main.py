with open('text.txt', 'r') as file:
   lines = file.read().splitlines()
positions = [[] for _ in range(len(lines))]
for line_num, line in enumerate(lines):
    for i, char in enumerate(line):
        if not char.isdigit() and char != '.':
            positions[line_num].append((i+1, char))
def machine(positions, task_type):
    result = 0
    for line, pos in enumerate(positions):     #line Zeilennummer, Pos -alle Sonderzeichen der Zeile
        for single_pos in pos:                 #single_pos -alle Sonderzeichen einer Zeile
            if line > 0 and line < 139:
                print("-----------------------------------------------------")
                print("Machine in Zeile", line+1, "und Position", single_pos [0], "und Sonderzeichen", single_pos[1])
                border = [''.join(lines[i][j] for j in range(single_pos[0] - 4, single_pos[0] + 3)) for i in range(line - 1, line + 2)]
                print("Border vor  Bereinigung", border[0])
                print("                       ", border[1])
                print("                       ", border[2])
                print(" ")
                for i in range(3):
                    border[i] = border[i][:5] + '..' if border[i][4] == '.' else border[i]
                    border[i] = border[i][:6] + '.' if border[i][5] == '.' else border[i]
                    border[i] = '..' + border[i][2:] if border[i][2] == '.' else border[i]
                    border[i] = '.' + border[i][1:] if border[i][1] == '.' else border[i]
                print("Border nach Bereinigung",border[0])
                print("                       ",border[1])
                print("                       ",border[2])
                border[1] = border[1][:3] + '.' + border[1][-3:]
                f_border = []
                for i, set in enumerate(border):
                    numbers = set.split('.')
                    for number in numbers:
                        if number.isdigit():
                            f_border.append(int(number))
                print("An Machine grenzende Zahlen",f_border)
                if task_type == 'part1':
                    result += sum(f_border)
                    print("Summe vorher:",  result-sum(f_border),"Summe der Machine", sum(f_border), "Neue Gesamtsumme", result)
                elif task_type == 'part2' and len(f_border)==2:
                    result = result + f_border[0] * f_border[1]
                    print("Summe vorher:",  result-f_border[0]*f_border[1],"Produkt der Machine", f_border[0]*f_border[1], "Neue Gesamtsumme", result)
    print("*******************************************************")
    print("Ende. Das Ergebnis für", task_type, "ist",result)
machine(positions, 'part1')
machine(positions, 'part2')