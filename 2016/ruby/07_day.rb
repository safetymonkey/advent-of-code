def find_tls(filename)
  valid_addresses = []

  File.foreach(filename, "\n") do |line|
    for i in 0...line.length do
      a, b, c, d = line[i], line[i + 1], line[i + 2], line[i + 3]
      next if b.nil? || c.nil? || d.nil?
      if abba?(a, b, c, d)
        bracket_abba = line.match(/\[\w*#{a + b + c + d}/) unless bracket_abba
        has_abba = true
      end
    end
    valid_addresses << line if has_abba && !bracket_abba
  end
  puts valid_addresses
  valid_addresses.count
end

def abba?(a, b, c, d)
  # Skip anything that returns a non-word character
  return false if a.match(/\W/) || b.match(/\W/) ||
                  c.match(/\W/) || d.match(/\W/)

  return false if a == b
  a + b == d + c
end

def find_ssl(filename)
  valid_addresses = []

  File.foreach(filename, "\n") do |line|
    # Split the line into substrings separated by either bracket end
    substrings = line.split(/\[|\]/)
    inside_brackets = []
    outside_brackets = []
    line_abas = []

    substrings.each do |substring|
      # Iterate through the length of the substring looking for ABA patterns
      for i in 0...substring.length do
        a, b, c = substring[i], substring[i + 1], substring[i + 2]
        next if b.nil? || c.nil? # cancel out if we're at the end of the string

        # If we match the ABA pattern...
        if aba?(a, b, c)
          aba = a + b + c
          # ... and the pattern appears inside brackets, add it to that list
          if line.match(/\[\w*#{aba}\w*\]/)
            inside_brackets << a + b + c unless inside_brackets.include? aba
          end
          # ... and the pattern appears OUTSIDE brackets, add it to that list
          if line.match(/\]\w*#{aba}\w*\[|^\w*#{aba}|#{aba}\w*$/)
            outside_brackets << a + b + c unless outside_brackets.include? aba
          end
        end
      end
    end

    # Loop through the list of ABA patterns inside brackets.
    outside_brackets.each do |aba|
      a, b = aba[0], aba[1]
      # Do they have a corresponding BAB pattern inside brackets
      valid_addresses << line if inside_brackets.include? (b + a + b)
    end
  end
  valid_addresses.count
end

def aba?(a, b, c)
  # This function should never get passed a bracket in the first place but you
  # never know.
  return false if a.match(/\W/) || b.match(/\W/) || c.match(/\W/)
  a != b && a == c
end

begin
  puts find_tls('inputs/07a.txt')
  puts "#{find_tls('inputs/07a-test.txt')} (Should be 2.)"
  puts find_ssl('inputs/07a.txt')
  puts find_ssl('inputs/07b-test.txt')
end
