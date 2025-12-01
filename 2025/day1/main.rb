def first_part(filename)
  pos = 50
  zero_count = 0
  for line in open(filename).readlines
    direction = line[0]
    jump = Integer(line[1..])

    case direction
    when 'L'
      pos -= jump % 100
    when 'R'
      pos += jump % 100
    end

    if pos < 0
      pos += 100
    elsif pos > 99
      pos -= 100
    end

    if pos == 0
      zero_count += 1
    end
  end
  return zero_count
end

def second_part(filename)
  pos = 50
  zero_count = 0
  for line in open(filename).readlines
    direction = line[0]
    jump = Integer(line[1..])

    start_pos = pos

    case direction
    when 'L'
      pos -= jump % 100
    when 'R'
      pos += jump % 100
    end
    full_cycles = (jump / 100).floor

    pointed_at_zero = false

    if pos < 0
      pos += 100
      pointed_at_zero = true
    elsif pos > 99
      pos -= 100
      pointed_at_zero = true
    end

    if pos == 0 or (pointed_at_zero and start_pos != 0)
      zero_count += 1
    end
    zero_count += full_cycles
  end
  return zero_count
end

puts(first_part('example.txt'))
puts(first_part('input.txt'))
puts
puts(second_part('example.txt'))
puts(second_part('input.txt'))
