def find_lowest(input, low)
  blocked_ranges = []
  File.foreach(input) do |line|
    blocked_ranges << line.split('-').map(&:to_i)
  end
  blocked_ranges.sort!

  blocked_ranges.each do |range_low, range_high|
    # Make the high end of our blocked range the new minimum if the range
    # either includes the current min or if the ranges is contiguous
    if low.between?(range_low, range_high) || range_low == (low + 1)
      low = range_high
    end
  end

  low + 1
end

def find_all(input, low, high)
  allowed = []
  until low >= high
    low = find_lowest(input, low)
    allowed << low unless low > high
  end
  allowed.uniq
end

begin
  time1 = Time.now
  test = find_lowest('inputs/20-test.txt', 0)
  puts "Test: #{test}" # 3
  # puts "Blocked range length: #{test.length}"
  puts "Runtime: #{Time.now - time1}s"

  time1 = Time.now
  final = find_lowest('inputs/20.txt', 0)
  puts "Part 1: #{final}" # 32259706
  puts "Runtime: #{Time.now - time1}s"

  time1 = Time.now
  final2 = find_all('inputs/20.txt', 0, 4_294_967_295)
  puts "Part 2: #{final2.length}" # 113
  puts "Runtime: #{Time.now - time1}s"
end
