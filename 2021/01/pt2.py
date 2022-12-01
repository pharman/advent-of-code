import csv

def main():
    cnt = 0

    try:
        with open("input") as f:
            reader = csv.reader(f)
            a = b = c = d = count = 0
            a_sum = b_sum = c_sum = d_sum = 0
            index = 1
            for line in reader:
                num = int(line[0])
                if index % 4 == 0:
                    a_sum = a
                    a = 0
                    if a_sum > d_sum and a_sum > 0:
                        count += 1
                else:
                    a += num
                if (index -1) % 4 == 0:
                    b_sum = b
                    b = 0
                    if b_sum > a_sum and b_sum > 0:
                        count +=1
                elif index > 0:
                    b += num
                if (index -2) % 4 == 0:
                    c_sum = c
                    c = 0
                    if c_sum > b_sum and c_sum > 0:
                        count +=1
                elif index > 1:
                    c += num
                if (index -3) % 4 == 0:
                    d_sum = d
                    d = 0
                    if d_sum > c_sum and d_sum > 0:
                        count +=1
                elif index > 2:
                    d += num
                index += 1
        print(count)

    finally:
        f.close()

if __name__ == "__main__":
    main()