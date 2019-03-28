def gen_time(start, end, step):
    current = start
    while True:
        current_h, current_min, current_sec = current
        step_h, step_min, step_sec = step
        end_h, end_min, end_sec = end

        current_sec += step_sec
        if current_sec >= 60:
            current_min += 1
            current_sec = current_sec % 60
        
        current_min += step_min
        if current_min >= 60:
            current_h += 1
            current_min = current_min % 60

        if current_h > end_h:
            break
        elif current_h == end_h:
            if current_min > end_min:
                break
            elif current_min == end_min:
                if current_sec >= end_sec:
                    break                

        current = (current_h, current_min, current_sec)
        yield current

for time in gen_time ((8, 10, 00), (10, 50, 15), (0, 15, 12)):
    print(time)