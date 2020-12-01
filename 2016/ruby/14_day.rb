class Disc
  attr_accessor :positions, :time0

  def initialize(positions, time0)
    @positions = positions.to_i
    @time0 = time0.to_i
  end

  def open_at?(time)
    (@time0 + time) % positions == 0
  end
end

def all_open?(time, disc_array)
  for i in 0...disc_array.length
    return false unless disc_array[i].open_at?(time + i + 1)
  end
  return true
end

def find_opening(filename, second=false)
  disc_array = []
  File.foreach(filename) do |line|
    disc_array << Disc.new(line[/has (\d+) /, 1], line[/position (\d+)./, 1])
  end
  disc_array << Disc.new(11, 0) if second

  time = 0
  until false
    break if all_open?(time, disc_array)
    time += 1
  end

  puts time
end

begin
  find_opening('inputs/14.txt')
  find_opening('inputs/14.txt', true)
end
