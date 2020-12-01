INPUT = 1350

class Node
  attr_accessor :x, :y, :steps

  def initialize(x, y, steps)
    @x = x
    @y = y
    @steps = steps
  end
end

def find_adjacent(node)
  x, y, steps = node.x, node.y, node.steps
  adjacent_nodes = []
  adjacent_nodes << Node.new(x - 1, y, steps + 1) if space_open(x - 1, y)
  adjacent_nodes << Node.new(x + 1, y, steps + 1) if space_open(x + 1, y)
  adjacent_nodes << Node.new(x, y - 1, steps + 1) if space_open(x, y - 1)
  adjacent_nodes << Node.new(x, y + 1, steps + 1) if space_open(x, y + 1)
  adjacent_nodes
end

def space_open(x, y, input = INPUT)
  return false if x < 0 || y < 0
  temp = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + input
  binary = temp.to_s(2)
  ones = 0

  binary.split('').each { |value| ones += value.to_i }
  ones.even?
end

def find_shortest_path(destination, start = [1, 1])
  queue = [Node.new(start[0], start[1], 0)]
  visited = []
  visited_under_50 = []
  until queue.empty? # In theory we'll break out of this loop before being empty
    node = queue.shift
    next if visited.include? [node.x, node.y]
    puts "Checking node [#{node.x.to_s + ', ' + node.y.to_s}] :: steps: #{node.steps}"
    visited << [node.x, node.y]
    visited_under_50 << node if node.steps <= 50
    break if node.x == destination[0] && node.y == destination[1]
    # break if node.steps > 5
    queue += find_adjacent(node)
  end
  puts node.steps # 92
  puts visited_under_50.length # 124
end

begin
  find_shortest_path([31, 39])
end
