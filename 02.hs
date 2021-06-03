fibo 1 = 1
fibo 2 = 2
fibo n = fibo(n-1) + fibo(n-2)

fibo_list = [ fibo n | n<-[1..], fibo n < 4000000]
fibo_list_even_sum = sum $ filter (\x -> mod x 2 == 0) fibo_list