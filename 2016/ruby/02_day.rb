def process_screen(filename, screen_array, position)
  code = []

  File.foreach(filename, "\n") do |line|
    line.split('').each do |input|
      case input
      when 'U'
        unless position[0] == 0 ||
               (screen_array[position[0] - 1][position[1]]).nil?
          position[0] -= 1
        end
      when 'D'
        unless position[0] + 1 == screen_array.first.length ||
               (screen_array[position[0] + 1][position[1]]).nil?
          position[0] += 1
        end
      when 'L'
        unless position[1] == 0 ||
               (screen_array[position[0]][position[1] - 1]).nil?
          position[1] -= 1
        end
      when 'R'
        unless position[1] + 1 == screen_array.first.length ||
               (screen_array[position[0]][position[1] + 1]).nil?
          position[1] += 1
        end
      end
    end
    code << screen_array[position[0]][position[1]]
  end

  puts code.join
end

begin
  screen_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  screen_array2 = [[nil, nil, 1, nil, nil], [nil, 2, 3, 4, nil],
                   [5, 6, 7, 8, 9], [nil, 'A', 'B', 'C', nil],
                   [nil, nil, 'D', nil, nil]]

  position = [1, 1]
  position2 = [3, 0]
  process_screen('inputs/02.txt', screen_array, position)
  process_screen('inputs/02.txt', screen_array2, position2)
end
