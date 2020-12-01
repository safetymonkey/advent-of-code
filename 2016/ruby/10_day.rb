class Bot
  attr_accessor :number

  def initialize(low_to, high_to, number)
    @low_to = low_to
    @high_to = high_to
    @number = number
    @holding = []
  end

  def receive(chip)
    @holding << chip
    raise "A bot has too many chips!" if @holding.length > 2
  end

  def process
    if @holding.length == 2
      puts "!!!! Bot #{self.number} is holding 17 & 61!" if @holding.sort == [17, 61]
      delivery = [[@low_to, @holding.min], [@high_to, @holding.max]]
      @holding = []
      return delivery
    end
  end
end

class Bin
  attr_accessor :holding

  def initialize
    @holding = []
  end

  def receive(chip)
    @holding << chip
  end
end

def count_output_bins(bin_collection)
  items = 0
  bin_collection.values.each { |bot| items += bot.holding.length }
  items
end

def run_robots(bot_collection, bin_collection)
  until count_output_bins(bin_collection) == 21
    delivery_queue = []
    bot_collection.each do |_, bot|
      delivery_queue = bot.process
      next if delivery_queue.nil?
      delivery_queue.each do |delivery|
        puts "Bot #{bot.number} delivering chip #{delivery[1]} to #{delivery[0]}"
        dest_type, dest_number = delivery[0].split(' ')
        if dest_type == 'bot'
          bot_collection[dest_number].receive(delivery[1])
        elsif dest_type == 'output'
          bin_collection[dest_number.to_i].receive(delivery[1].to_i)
        else
          raise "I don't know how you got here, kid."
        end
      end
    end
  end
  answer = 1
  for i in 0..2 do
    answer *= bin_collection[i].holding.first
  end
  puts "Bins 0..2 multiplied: #{answer}"
end

def setup(filename)
  bot_collection = {}
  bin_collection = {}
  input_array = []

  File.readlines(filename).map { |line| input_array << line }
  input_array.sort!

  input_array.each do |line|
    if line.split(' ').first == 'bot'
      bot_number = line[/^bot (\d+) gives/, 1]
      low_to = line[/gives low to (\w+ \d+) and/, 1]
      high_to = line[/high to (\w+ \d+)$/, 1]
      bot_collection[bot_number] = Bot.new(low_to, high_to, bot_number)
    elsif line.split(' ').first == 'value'
      bot_collection[line[/bot (\d+)$/, 1]].receive(line[/^value (\d+) goes/, 1].to_i)
    end

    for i in 0...30 do
      bin_collection[i] = Bin.new
    end
  end
  return bot_collection, bin_collection
end

begin
  input = 'inputs/10.txt'
  bot_collection, bin_collection = setup(input)
  # puts bin_collection
  run_robots(bot_collection, bin_collection)
end
