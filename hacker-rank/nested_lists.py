if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    records.sort(key=lambda x: (x[1],x[0]))
    sls = sorted(list(set([x[1] for x in records])))[1]
    slr = [r[0] for r in records if r[1]==sls]
    print("\n".join(slr))

