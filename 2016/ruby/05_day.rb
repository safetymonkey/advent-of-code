require 'digest'

def decrypt_password(door)
  index = 0
  password = ''
  until password.length == 8
    char = Digest::MD5.hexdigest(door + index.to_s)[0...6]
    if char =~ /^00000/
      password << char[5] if char =~ /^00000/
      puts "Found a match! Password is #{password}"
    end
    index += 1
  end

  puts password
end

def decrypt_password2(door)
  index = 0
  password = '.' * 8
  until password =~ /^[0-9a-f]{8}$/
    char = Digest::MD5.hexdigest(door + index.to_s)[0...7]
    if char =~ /^00000[0-7]/
      position = char[5].to_i
      password[position] = char[6] if password[position] == '.'
      puts "Found a match! Password is #{password}"
    end
    index += 1
  end

  puts password
end

begin
  # decrypt_password('abc') # Should result in 18f47a30
  # decrypt_password('ffykfhsq')
  decrypt_password2('ffykfhsq')
end
