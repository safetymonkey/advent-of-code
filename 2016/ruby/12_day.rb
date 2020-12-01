def process(filename, register)
  line_array = []

  File.foreach(filename, "\n") do |line|
    line_array << line
  end

  i = 0
  line = line_array[i]
  i2 = 0

  until line.nil?
    command, x, y = line.split

    if command == 'cpy'
      x = x.match(/[abcd]/) ? register[x.to_sym].to_i : x.to_i
      register[y.to_sym] = x
      i += 1
    elsif command == 'inc'
      register[x.to_sym] += 1
      i += 1
    elsif command == 'dec'
      register[x.to_sym] -= 1
      i += 1
    elsif command == 'jnz'
      x = x.match(/[abcd]/) ? register[x.to_sym].to_i : x.to_i

      i += (x.to_i == 0) ? 1 : y.to_i
    end
    line = line_array[i]
    i2 += 1
  end

  puts "Loops: #{i2}"
  puts register
end

begin
  register = { a: 0, b: 0, c: 0, d: 0 }
  process('inputs/11.txt', register)

  register = { a: 0, b: 0, c: 1, d: 0 }
  process('inputs/11.txt', register)
end
