#coding:utf8


def counter_list(db,result):
    dic = {}
    d = []
    for x in db:
      no = result.count(x)
      d.append(str((x,no)))
      k = "N%s" % no
      if not dic.has_key(k):
        dic[k]=[]
      dic[k].append(x)
    return dic

if __name__ == "__main__":
    print(counter_list())
