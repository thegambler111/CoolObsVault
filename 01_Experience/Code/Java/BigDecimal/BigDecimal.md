# BigDecimal
- When handling number with high precision (many number after decimal point), you can use `BigDecimal` if `double` can not provide enough precision
```java  
double a = 1.05;  
double b = 2.55;  
BigDecimal c = new BigDecimal("1.05");  
BigDecimal d = new BigDecimal("2.55");  
System.out.println(a+b); // 3.5999999999999996
System.out.println(c.add(d)); // 3.60
```


# 

---
- Status: #done 

- Tags: 

- References:
	- [Source]()

- Related:
