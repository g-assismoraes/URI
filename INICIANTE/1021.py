parteInteira, parteDecimal = map(float, input().split("."))

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % int(parteInteira//100))
print("%d nota(s) de R$ 50.00" % int(parteInteira%100//50))
print("%d nota(s) de R$ 20.00" % int(parteInteira%100%50//20))
print("%d nota(s) de R$ 10.00" % int(parteInteira%100%50%20//10))
print("%d nota(s) de R$ 5.00" % int(parteInteira%100%50%20%10//5))
print("%d nota(s) de R$ 2.00" % int(parteInteira%100%50%20%10%5//2))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % int(parteInteira%100%50%20%10%5%2))
print("%d moeda(s) de R$ 0.50" % int(parteDecimal//50))
print("%d moeda(s) de R$ 0.25" % int(parteDecimal%50//25))
print("%d moeda(s) de R$ 0.10" % int(parteDecimal%50%25//10))
print("%d moeda(s) de R$ 0.05" % int(parteDecimal%50%25%10//5))
print("%d moeda(s) de R$ 0.01" % int(parteDecimal%50%25%10%5))
