import time
# perf_counter
start = time.perf_counter()
print("Nhập 1 giá trị: ")
x = input()
print("Bạn đã nhập giá trị", x)
end = time.perf_counter()
duration = end - start
print(duration)

start = time.perf_counter()
for i in range(1000):
    print(i, end=' ')
print()
end = time.perf_counter()
duration = end - start
print(duration)

# sleep
for i in range(3):
    print(i, end=' ')
    time.sleep(3)
