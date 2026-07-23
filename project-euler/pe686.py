import math, time

start_time = time.time()

def z_calc(initseg, y):
    lb = math.log(initseg,2) + y * math.log(10, 2)
    ub = math.log(initseg+1,2) + y * math.log(10, 2)
    return (lb, ub)

def is_hit(initseg, y):
    (l, u) = z_calc(initseg, y)
    return (math.floor(l) < math.floor(u) or math.floor(l) == l)

hit_count = 0
test_val = 1
init_seg = 123
while (hit_count < 678910):
    if is_hit(init_seg, test_val):
        hit_count += 1
        if hit_count % 100000 == 78910:
            print(hit_count, ": ", math.floor(z_calc(init_seg, test_val)[1]))
    test_val += 1
    
print("Time (s): ", time.time() - start_time)
