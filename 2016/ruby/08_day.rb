class Screen
  def initialize(width = 50, height = 6, pixel_default = false)
    @screen_array = Array.new(width) { Array.new(height, pixel_default) }
  end

  def activate(x, y)
    for ix in 0...x do
      for iy in 0...y do
        @screen_array[ix][iy] = true
      end
    end
  end

  def rotate_horizontal(row, number)
    number.times do
      temp = @screen_array.last[row]
      for i in 0...(@screen_array.length - 1) do
        @screen_array.reverse[i][row] = @screen_array.reverse[i + 1][row]
      end
      @screen_array.first[row] = temp
    end
  end

  def rotate_vertical(column, number)
    @screen_array[column].rotate!(number * -1)
  end

  def count_pixels
    count = 0
    @screen_array.each do |sub|
      sub.each do |value|
        count += value ? 1 : 0
      end
    end
    count
  end

  def printout
    for iy in 0...@screen_array.first.length do
      row = ''
      for ix in 0...@screen_array.length do
        row << (@screen_array[ix][iy] ? '#' : '.')
      end
      puts row
    end
  end
end

def decode_screen(filename)
  screen = Screen.new

  File.foreach(filename) do |line|
    command, secondary = line.split(' ')[0], line.split(' ')[1]
    if command == 'rect'
      # Activate
      x, y = line.scan(/\d+/)
      screen.activate(x.to_i, y.to_i)
    elsif command == 'rotate' && secondary == 'column'
      # Rotate vertical
      x = line[/x=(\d+)/, 1]
      number = line[/by (\d+)/, 1]
      screen.rotate_vertical(x.to_i, number.to_i)
    elsif command == 'rotate' && secondary == 'row'
      # Rotate horizontal
      y = line[/y=(\d+)/, 1]
      number = line[/by (\d+)/, 1]
      screen.rotate_horizontal(y.to_i, number.to_i)
    else
      raise "Didn't recognize input line: #{line}"
    end
  end
  puts screen.count_pixels
  screen.printout
end

begin
  decode_screen('inputs/08a.txt')
end
