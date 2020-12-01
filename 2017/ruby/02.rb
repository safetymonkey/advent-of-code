def checksum_sheet(sheet)
  checksum = 0
  sheet.each do |row|
    checksum += (row.max - row.min)
  end
  checksum
end

def checksum_sheet2(sheet)
  checksum = 0
  sheet.each do |row|
    for j in 0...row.length
      x = row[j]
      for i in 0...row.length
        next if i == j
        y = row[i]
        if x >= y && x % y == 0
          checksum += (x / y)
        end
      end
    end
  end
  checksum
end

def part1(input)
  puts "Part 1\n#{'=' * 80}"
  test_sheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
  test_sum = 18
  result = checksum_sheet(test_sheet)
  puts "Test expected value: #{test_sum} // Actual: #{result}"

  sheet = []
  File.foreach(input) { |line| sheet << line.split(/\s/).map(&:to_i) }
  result = checksum_sheet(sheet)
  puts "Result: #{result}"
end

def part2(input)
  puts "\nPart 2\n#{'=' * 80}"
  test_sheet = [[5, 2, 9, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
  test_sum = 9
  result = checksum_sheet2(test_sheet)
  puts "Test expected value: #{test_sum} // Actual: #{result}"

  sheet = []
  File.foreach(input) { |line| sheet << line.split(/\s/).map(&:to_i) }
  result = checksum_sheet2(sheet)
  puts "Result: #{result}"
end

begin
  input = 'inputs/day2.txt'
  part1(input)
  part2(input)
end
