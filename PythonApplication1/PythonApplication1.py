for a in range(1000,10000):
    qian = a//1000
    bai = (a//100)%10
    shi = (a//10)%10
    ge = a%10
    qian=qian*qian*qian
    bai=bai*bai*bai
    shi=shi*shi*shi
    ge=ge*ge*ge
    he=ge+shi+bai+qian
    if(he==a):
        print(a)