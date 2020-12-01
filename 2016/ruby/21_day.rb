def scramble(filename, input)
  File.foreach(filename) do |line|
    if line =~ /^swap position/
      x = line.scan(/position (\d+)/).first.first.to_i
      y = line.scan(/position (\d+)/).last.last.to_i
      temp = input[x]
      input[x] = input[y]
      input[y] = temp
    elsif line =~ /^swap letter/
      x = line.scan(/letter (\w{1})/).first.first
      y = line.scan(/letter (\w{1})/).last.last
      input.tr!(x + y, y + x)
    elsif line =~ /^rotate (left|right)/
      direction = line.split(' ')[1]
      steps = line.split(' ')[2].to_i
      unless direction == 'left' then steps *= -1 end
      input = input.split('').rotate!(steps).join
    elsif line =~ /^rotate based/
      i = input.index(line.split(' ').last)
      i += i >= 4 ? 2 : 1
      i *= -1
      input = input.split('').rotate!(i).join
    elsif line =~ /^reverse positions/
      x = line.split(' ')[2].to_i
      y = line.split(' ')[4].to_i
      reverse = input[x..y].reverse
      input.gsub!(input[x..y], reverse)
    elsif line =~ /^move position/
      x = line.split(' ')[2].to_i
      y = line.split(' ')[5].to_i
      char = input[x]
      input.delete!(char)
      input.insert(y, char)
    end
  end
  input
end

# NOTE: I know that brute forcing it is the wrong approach, but it was easy
# and I was up late and it worked, so... so, yeah.
def descramble(filename, result)
  final = ''
  until final == result
    temp = result.split('').shuffle.join
    final = scramble(filename, temp)
  end
  temp
end

begin
  puts "Final: #{scramble('inputs/21-test.txt', 'abcde')}" # decab
  puts "Final: #{scramble('inputs/21.txt', 'abcdefgh')}" # dbfgaehc
  puts "Final descramble: #{descramble('inputs/21.txt', 'fbgdceah')}"
end
