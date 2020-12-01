def count_triangles(filename)
  valid = 0

  File.foreach(filename) do |line|
    a, b, c = line.split
    a = a.to_i
    b = b.to_i
    c = c.to_i

    valid += 1 if valid_triangle?(a, b, c)
  end
  puts valid
end

def count_triangles2(filename)
  valid = 0
  col1, col2, col3 = [], [], []

  File.foreach(filename) do |line|
    a, b, c = line.split
    col1 << a.to_i
    col2 << b.to_i
    col3 << c.to_i

    if col1.length == 3
      valid += 1 if valid_triangle?(col1[0], col1[1], col1[2])
      valid += 1 if valid_triangle?(col2[0], col2[1], col2[2])
      valid += 1 if valid_triangle?(col3[0], col3[1], col3[2])
      col1, col2, col3 = [], [], []
    end
  end
  puts valid
end

def valid_triangle?(a, b, c)
  (a + b > c) && (a + c > b) && (b + c > a)
end

begin
  count_triangles('inputs/03.txt')
  count_triangles2('inputs/03.txt')
end
