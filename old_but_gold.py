with open('text.txt', 'r') as file:
   lines = file.read().splitlines()
positions = [[] for _ in range(len(lines))]
for line_num, line in enumerate(lines):
    for i, char in enumerate(line):
        if not char.isdigit() and char != '.':
            positions[line_num].append((i+1, char))
number_array = []
for line_num, line in enumerate(lines):
    numbers = []
    current_number = ''
    current_number_start = None
    for i, char in enumerate(line):
        if char.isdigit():
            if current_number_start is None:
                current_number_start = i
            current_number += char
        elif current_number:
            numbers.append((int(current_number), current_number_start))
            current_number = ''
            current_number_start = None
    if current_number:
        numbers.append((int(current_number), current_number_start))
    number_array.append(numbers)
print(number_array)
def part1(numbers, positions):
   print(positions)
   sum = 0
   j=0
   for line_numbers, line_positions in zip(numbers, positions):
      for number, number_start in line_numbers:
         pot_position_index = []
         found = False
         for i in range(len(str(number))+2):
            pot_position_index.append(number_start + i)
         # print("Number", number, "positions", pot_position_index)
         if j > 0 and j < 139:
            if any(num in pot_position_index for num, _ in positions[j]) or any(num in pot_position_index for num, _ in positions[j+1]) or any(num in pot_position_index for num, _ in positions[j-1]):
               found = True
               #print("found",number)
         elif j == 139:
            if any(num in pot_position_index for num, _ in positions[j]) or any(num in pot_position_index for num, _ in positions[j-1]):
               found = True
               #print("found",number)
         else:
            if any(num in pot_position_index for num, _ in positions[j]) or any(num in pot_position_index for num, _ in positions[j+1]):
               #print("found", number)
               found = True
         if found == True:
            sum += number
            #print ("Neue Ergebnis",sum)
      j += 1
def part2(numbers, positions):
   sum=0
   line = 0  #Line 1 is line 0
   for pos in positions:
      for single_pos in pos:
         pos = int(single_pos[0])
         print("********************************************************************")
         if line > 0 and line < 139:
            stemp = single_pos[1]
            print(stemp)
            border = [''.join(lines[i][j] for j in range(pos-4, pos+3)) for i in range(line-1, line+2)]
            print(border)
            final_border = []
            #edgecases
            for i in range(3):
               if border[i][4] == '.':
                  border[i] = border[i][:5] + '..'
               if border[i][5] == '.':
                  border[i] = border[i][:6] + '.'
               if border[i][2] == '.':
                  border[i] = '..' + border[i][2:]
               if border[i][1] == '.':
                  border[i] = '.' + border[i][1:]
            border[1] = border[1][:3] + '.' + border[1][-3:]
            print (border)
            for set in border:
               numbers = set.split('.')
               print("Number",numbers)

               for number in numbers:
                  if number.isdigit():
                     final_border.append(int(number))
            print(final_border, " + len: ", len(final_border) )
            if len(final_border)==2:
               product = final_border[0] * final_border[1]
               sum += product
               print("Summe vorher:",sum-product,"Produkt:", product, "Neue summe:", sum)


            for i in range(line - 1, line + 2):
               print(lines[i][pos - 4], lines[i][pos - 3], lines[i][pos - 2], lines[i][pos - 1], lines[i][pos],
                     lines[i][pos+1], lines[i][pos+2])
            print("********************************************************************")
      line += 1
   print(sum)
part1(number_array, positions)    #result must be 557705
part2(number_array, positions)    #result must be 84266818