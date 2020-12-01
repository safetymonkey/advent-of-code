def decrypt_rooms(filename)
  # This is the sum of all the sector IDs we'll be returning later
  sector_sum = 0

  File.foreach(filename) do |line|
    # Break the line into its three discrete subcomponents
    room = line[/(.*)-\d+\[/, 1]
    sector = line[/.*-(\d+)\[/, 1].to_i
    checksum = line[/\[(\w{5})\]/, 1]

    # Build a hash table with the count of each character in the room name
    char_hash = Hash.new(0)
    room.each_char { |char| char_hash[char] += 1 unless char == '-' }

    # Now loop back through the hash we just made and make a reverse hash where
    # the key is the number of times it's in the room name
    reverse_hash = {}
    char_hash.each do |char, count|
      if reverse_hash[count].nil?
        reverse_hash[count] = [char]
      else
        reverse_hash[count] << char
        reverse_hash[count].sort! # Sort is to meet the tie-breaking requirement
      end
    end

    # Pull the top characters out of the reverse hash until we have at least 5
    top_chars = ''
    i = 0
    until top_chars.length >= 5
      # This next line is a little hard to parse. Reverse sorting the keys gives
      # us characters in descending order of appearance. Tied characters
      # are already alphabetized.
      top_chars << reverse_hash[reverse_hash.keys.sort.reverse[i]].join
      i += 1
    end

    # Add the sector number to the sum if the checksum matches our calculation.
    if checksum == top_chars[0...5]
      sector_sum += sector
      puts "Room: #{decrypt_room_name(room, sector)}\t// Sector: #{sector}"
    end
  end

  puts sector_sum
end

def decrypt_room_name(room, sector)
  decoded_name = ''
  room.each_char do |char|
    if char == '-'
      char = ' '
    else
      sector.times { char = char == 'z' ? 'a' : char.next }
    end
    decoded_name << char
  end
  decoded_name
end

begin
  decrypt_rooms('inputs/04-test.txt')
  # Output should be 1514

  decrypt_rooms('inputs/04.txt')
end
