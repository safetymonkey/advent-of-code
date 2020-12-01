def decode(filename, modified = false)
  length = File.foreach(filename).first.length
  array_of_hashes = []
  for i in 0...length do
    array_of_hashes[i] = Hash.new(0)
  end
  File.foreach(filename) do |line|
    array_of_hashes.each_with_index do |hash, index|
      hash[line[index]] += 1
    end
  end

  decoded_string = ''
  array_of_hashes.each do |hash|
    reverse_hash = {}
    hash.each do |char, count|
      if reverse_hash[count].nil?
        reverse_hash[count] = [char]
      else
        reverse_hash[count] << char
      end
    end

    if modified
      decoded_string << reverse_hash[hash.values.sort!.first].first
    else
      decoded_string << reverse_hash[hash.values.sort!.reverse.first].first
    end
  end

  # puts array_of_hashes
  puts decoded_string
end

begin
  decode('inputs/06-test.txt') # Should be 'easter'
  decode('inputs/06.txt')
  decode('inputs/06.txt', true)
end
