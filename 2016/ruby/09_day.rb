def decompress(input)
  input_array = input.split('')
  output_array = []

  # We're just going to keep popping the front characters off this array
  # until we're empty
  until input_array.empty?
    # If the current first character is a ( and it looks like we're coming up on
    # a marker...
    # Also: Curious about the length? In my output the longest char_count is 4
    # and the longest multiplier is 2
    if input_array[0] == '(' && input_array[0..9].join
                                                 .match(/\(\d{1,4}x\d{1,2}\)/)
      # Get the first number in the marker
      char_count = input_array[0..9].join.scan(/\((\d{1,4})x\d{1,2}\)/)
                                    .first.first.to_i
      multiplier = input_array[0..9].join.scan(/\(\d{1,4}x(\d{1,2})\)/)
                                    .first.first.to_i
      # We've got the decompression info so let's drop it from the input string
      marker = input_array.shift(char_count.to_s.length +
                                 multiplier.to_s.length + 3).join

      string = input_array.shift(char_count).join * multiplier
      output_array += string.split('')
    else
      # Pop it out of the input array and into the output array
      output_array << input_array.shift
    end
  end

  output_array.join
end

def recursive_decompress(input)
  input_array = input.split('')
  output_length = 0

  until input_array.empty?
    if input_array[0] == '(' && input_array[0..9].join
                                                 .match(/\(\d{1,4}x\d{1,2}\)/)
      # Get the first number in the marker
      char_count = input_array[0..9].join.scan(/\((\d{1,4})x\d{1,2}\)/)
                                    .first.first.to_i
      multiplier = input_array[0..9].join.scan(/\(\d{1,4}x(\d{1,2})\)/)
                                    .first.first.to_i
      # We've got the decompression info so let's drop it from the input string
      marker = input_array.shift(char_count.to_s.length +
                                 multiplier.to_s.length + 3).join

      string = input_array.shift(char_count).join
      length = recursive_decompress(string)
      output_length += length * multiplier
    else
      input_array.shift
      output_length += 1
    end
  end

    output_length
end

begin
  test1 = 'ADVENT' # decompresses to 'ADVENT'; decompressed length of 6.
  test1_output = decompress(test1)
  passed = test1_output == 'ADVENT' ? 'PASSED!  ' : 'FAILED!  '
  puts "#{'PASSED!  ' if passed}Test1 is '#{test1_output}', should be 'ADVENT'"

  test2 = 'A(1x5)BC' # becomes ABBBBBC for a decompressed length of 7.
  test2_output = decompress(test2)
  passed = test2_output == 'ABBBBBC' ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test1 is '#{test2_output}', should be 'ABBBBBC'"

  test3 = '(3x3)XYZ' # becomes XYZXYZXYZ for a decompressed length of 9.
  test3_output = decompress(test3)
  passed = test3_output == 'XYZXYZXYZ' ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test3 is '#{test3_output}', should be 'XYZXYZXYZ'"

  test4 = 'A(2x2)BCD(2x2)EFG' # becomes ABCBCDEFEFG; decompressed length of 11.
  test4_output = decompress(test4)
  passed = test4_output == 'ABCBCDEFEFG' ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test4 is '#{test4_output}', should be 'ABCBCDEFEFG'"

  test5 = '(6x1)(1x3)A' # becomes (1x3)A - decompressed length of 6.
  test5_output = decompress(test5)
  passed = test5_output == '(1x3)A' ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test5 is '#{test5_output}', should be '(1x3)A'"

  test6 = 'X(8x2)(3x3)ABCY' # becomes X(3x3)ABC(3x3)ABCY; length of 18)
  test6_output = decompress(test6)
  passed = test6_output == 'X(3x3)ABC(3x3)ABCY' ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test6 is '#{test6_output}', should be 'X(3x3)ABC(3x3)ABCY'"

  input = File.read('inputs/09a.txt')
  output = decompress(input)
  puts "Original length was #{input.length}, new length is #{output.length}."
  puts "97715 is too high, FYI."

  puts "-----------------------------------------------------------------------"

  test1 = '(3x3)XYZ' # decompresses to 'XYZXYZXYZ'; decompressed length of 6.
  test1_length = recursive_decompress(test1)
  passed = test1_length == 9 ? 'PASSED!  ' : 'FAILED!  '
  puts "#{'PASSED!  ' if passed}Test1 is '#{test1_length}', should be 9"

  test2 = 'X(8x2)(3x3)ABCY' # becomes XABCABCABCABCABCABCY for a decompressed length of 20.
  test2_length = recursive_decompress(test2)
  passed = test2_length == 20 ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test1 is '#{test2_length}', should be 20"

  test3 = '(27x12)(20x12)(13x14)(7x10)(1x12)A' # decompressed length of 241920.
  test3_output = recursive_decompress(test3)
  passed = test3_output == 241920 ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test3 is '#{test3_output}', should be 241920"

  test4 = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN' # decompressed length of 445.
  test4_output = recursive_decompress(test4)
  passed = test4_output == 445 ? 'PASSED!  ' : 'FAILED!  '
  puts "#{passed}Test4 is '#{test4_output}', should be 445"

  input = File.read('inputs/09a.txt')
  output = recursive_decompress(input)
  puts "v2 length is #{output}."
end
