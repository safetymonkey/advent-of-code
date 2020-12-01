def parse_captcha(input, part)
  sum = 0
  input_array = input.to_s.split(//).map{|chr| chr.to_i}
  length = input_array.length
  for i in 0...length
    cur_item = input_array[i]
    if part == 1
      next_item = (i < (input_array.length - 1)) ? input_array[i + 1] : input_array[0]
    elsif part == 2
      i2 = (length / 2) + i
      i2 = i2 < length ? i2 : i2 - length
      next_item = input_array[i2]
    end
    sum += cur_item if cur_item == next_item
  end
  puts "Input: #{input_array.length > 20 ? 'superlong' : input} // Sum: #{sum}"
end

def part1(input)
  puts "Part 1\n#{'=' * 80}"
  parse_captcha(1122, 1)
  parse_captcha(1111, 1)
  parse_captcha(1234, 1)
  parse_captcha(91212129, 1)
  parse_captcha(input, 1)
end

def part2(input)
  puts "\nPart 2\n#{'=' * 80}"
  parse_captcha(1212, 2)
  parse_captcha(1221, 2)
  parse_captcha(123425, 2)
  parse_captcha(123123, 2)
  parse_captcha(12131415, 2)
  parse_captcha(input, 2)
end

begin
  input = 9513446799636685297929646689682997114316733445451534532351778534251427172168183621874641711534917291674333857423799375512628489423332297538215855176592633692631974822259161766238385922277893623911332569448978771948316155868781496698895492971356383996932885518732997624253678694279666572149831616312497994856288871586777793459926952491318336997159553714584541897294117487641872629796825583725975692264125865827534677223541484795877371955124463989228886498682421539667224963783616245646832154384756663251487668681425754536722827563651327524674183443696227523828832466473538347472991998913211857749878157579176457395375632995576569388455888156465451723693767887681392547189273391948632726499868313747261828186732986628365773728583387184112323696592536446536231376615949825166773536471531487969852535699774113163667286537193767515119362865141925612849443983484245268194842563154567638354645735331855896155142741664246715666899824364722914296492444672653852387389477634257768229772399416521198625393426443499223611843766134883441223328256883497423324753229392393974622181429913535973327323952241674979677481518733692544535323219895684629719868384266425386835539719237716339198485163916562434854579365958111931354576991558771236977242668756782139961638347251644828724786827751748399123668854393894787851872256667336215726674348886747128237416273154988619267824361227888751562445622387695218161341884756795223464751862965655559143779425283154533252573949165492138175581615176611845489857169132936848668646319955661492488428427435269169173654812114842568381636982389224236455633316898178163297452453296667661849622174541778669494388167451186352488555379581934999276412919598411422973399319799937518713422398874326665375216437246445791623283898584648278989674418242112957668397484671119761553847275799873495363759266296477844157237423239163559391553961176475377151369399646747881452252547741718734949967752564774161341784833521492494243662658471121369649641815562327698395293573991648351369767162642763475561544795982183714447737149239846151871434656618825566387329765118727515699213962477996399781652131918996434125559698427945714572488376342126989157872118279163127742349
  part1(input)
  part2(input)
end
