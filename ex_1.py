luong = [5000, 6000, 7000, 8000, 9000, 10000, 10000, 11000]

luong.sort(reverse=True)
luong_cao_nhat = max(luong)

luong_cao_thu_hai = None
for salary in luong:
    if salary < luong_cao_nhat:
        luong_cao_thu_hai = salary
        break

luong_cao_thu_hai = [salary for salary in luong if salary == luong_cao_thu_hai]

print(luong_cao_thu_hai)
