require 'digest'

def find_path(input, v2 = false)
  current_room = [1, 1]
  path = ''
  queue = [[current_room, path]]
  valid_paths = []

  until queue.empty?
    current_room, path = queue.shift
    key = Digest::MD5.hexdigest(input + path)[0...4]

    key.split('').each_with_index do |char, index|
      if ('bcdef'.include? char) && current_room != [4, 4]
        if index == 0 && current_room[1] > 1
          # Up
          queue << [[current_room[0], current_room[1] - 1], path + 'U']
        elsif index == 1 && current_room[1] < 4
          # Down
          queue << [[current_room[0], current_room[1] + 1], path + 'D']
        elsif index == 2 && current_room[0] > 1
          # Left
          queue << [[current_room[0] - 1, current_room[1]], path + 'L']
        elsif index == 3 && current_room[0] < 4
          # Right
          queue << [[current_room[0] + 1, current_room[1]], path + 'R']
        end
      end
    end

    valid_paths << path if current_room == [4, 4]
    return path if current_room == [4, 4] && !v2
  end

  valid_paths.sort_by(&:length).reverse.first if v2
end

def run_test(input, expected)
  result = find_path(input)
  puts "#{'Success! -- ' if result == expected}Test 1 Result: #{result}, should be #{expected}."
end

begin
  run_test('ihgpwlah', 'DDRRRD')
  run_test('kglvqrro', 'DDUDRLRRUDRD')
  run_test('ulqzkmiv', 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

  result = find_path('vkjiggvb')
  puts "Result: #{result}"

  result = find_path('vkjiggvb', true)
  puts "v2 Result: #{result}"
end
