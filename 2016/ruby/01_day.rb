INPUT = 'R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3'

def find_directions(input)
  facing = :north
  moves = input.split(', ')
  x = 0
  y = 0

  moves.each do |move|
    facing = turn(facing, move[0])
    blocks = move[1..move.length].to_i

    case facing
    when :north then y += blocks
    when :south then y -= blocks
    when :west then x -= blocks
    when :east then x += blocks
    end
  end

  total = x.abs + y.abs
  total
end

def find_directions2(input)
  facing = :north
  moves = input.split(', ')
  x = 0
  y = 0
  visited = [x.to_s + y.to_s]
  puts "Visited: #{visited}"

  moves.each do |move|
    facing = turn(facing, move[0])
    blocks = move[1..move.length].to_i

    for i in 1..blocks

      case facing
      when :north then y += 1
      when :south then y -= 1
      when :west then x -= 1
      when :east then x += 1
      end

      node = x.to_s + y.to_s

      if visited.include? node
        puts visited
        puts node
        return x.abs + y.abs
      else
        visited << node
      end
    end
  end

  x.abs + y.abs
end

def turn(facing, direction)
  case facing
  when :north
    direction == 'L' ? :west : :east
  when :east
    direction == 'L' ? :north : :south
  when :south
    direction == 'L' ? :east : :west
  when :west
    direction == 'L' ? :south : :north
  else
    raise "You passed in an invalid facing direction."
  end
end

begin
  find_directions(INPUT).to_s
end

# describe '.find_directions' do
#   it 'should handle three rights' do
#     directions = 'R2, R2, R2'
#     find_directions(directions).should eq(2)
#   end

#   it 'should handle one of each' do
#     directions = 'R2, L3'
#     find_directions(directions).should eq(5)
#   end

#   it 'should handle two of each' do
#     directions = 'R5, L5, R5, R3'
#     find_directions(directions).should eq(12)
#   end
# end
