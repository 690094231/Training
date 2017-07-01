
## ���߳�&�����&ͨ�Ž�����ҵ

### �Ķ�����
5��12�ձ����Ĵ��ģ��������WannaCry��ع�Ϊ��֪����ͼ�Ǹ������������İ�Ľ��档���������ҵ����ʵ��һ���ָò����ļ򻯰湦�ܡ�Tips:
��������ֻ����ϰ��;�������ز�Ҫ�����κδ����ƻ����ʵĶ������ر��Ƕ������Ǽ����������������һ����������
![wanna](wannacry.png)

Ϊʲô�ڿ������Լ��ļ����β������أ���ʵ���ϻ���ȡ����RSA�����㷨�Ŀɿ��ԡ������������������һ��ʮ�ּ򵥵����顣��������nλ���������ҵ�O(n^log3)
���Ӷȵķ����㷨���෴����һ���������������ֽ⽫��һ����Ϊ���ѵ�����RSA����
������һ���ǡ�����RSA2048(2048bit���ĳ˻�)��˵���������޿ɴ�2030�꣬�������λ�������Ļ���һ���޽���������˶��ڲ����ı�д�ߣ�
ʹ��RSA�����ܿ���˵����ʮ�㡣

RSA�ɹ�Կ��˽Կ��ɴ���ڽ����п��Կ���������ͨ�����ܰ�ť������һЩ�ļ������й����û���ʾ�������á���һ������Ϊ�ܿ���������ԭ��
RSA��˽Կ�����ܻ��没��������ֻ���ܱ����˹�Կ��Ҫ����ܱ���Ҫͨ�����������ߵķ����������߸���ͨ�ŷ�ʽ�����ṩ�Լ��Ĺ�Կ����������������ṩ˽Կ��
��˿ɼ���ʵ���Ͽ�����һ���򵥵�ͨ�Ź�����ʵ�֡�һ�ֿ��ܵ�����ͼ�������£�
![process](pro.png)

�����Ķ����ϵ��˽��������Ŵ��ѧ����ɢ����ȫ�������RSA�㷨������RSA�㷨��ϸ�ڿ���ȥ�����ѡ�
## ��������

RSA�㷨�İ�ȫ�Ժܴ�̶���ȡ���������Ե�ѡȡ������ѡȡ�ķ���������Ҫ���������Լ��顣Ϊ�������
���������ʹ����򵥵������������жϡ����������һ�ε��̼߳���1-100000���������Ĵ��롣�����������ɶ��̵߳�ʵ�֣�
```
import threading
import math
import time
import queue

read = queue.Queue()  # ��ŵȴ��жϵ���
write = queue.Queue() # �������
def is_prime(m):
    isprime = True
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            isprime = False
            break
    return isprime


def main():
    global read
    mult_thread=False
    if(not mult_thread):
        prime=[]
        for i in range(2,100000):
            if is_prime(i):
                prime.append(i)
        print(len(prime))
    else:
        #��������ɶ��̵߳�ʵ�֣�����������write��


if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print("runs %f s" % (end - start))
```

����ԱȽ�һ�µ��̺߳Ͷ��̵߳������ٶȣ���ܿ��ܻᷢ�ֶ��߳�ԶԶ���ڵ��̣߳�˼��һ��ԭ��

## ǿ���Ƽ���ѡ������

��Ȼ���Լ��������ⲿ����ıȽ��ѣ�������ѡ��һ����ôдWannacry23333����ص�ͨ�Ŵ���ǿ�ҽ���ֱ�Ӵ�����copyȻ��ġ�

���˹���RSA�Ҹ�����һ��ʮ�ּ򵥵Ĵ��롣�����ֱ�ӵ��ýӿڣ�Ҳ�����Լ�����ʵ����ϰһ�£�����C++���������Ҫ����ʵ�֡�
����C++�˶��ڴ����Ĳ����Ƚϲ��㣬������޸�RSAģ��Ĭ�ϵ���������C++��д��
����������£�����֮ǰ������ͼ����python����ΪServer, C++����ΪClient�������ӡ�Python��ѡ��һ�������Բ�����Կ��˽Կ��Ȼ���͹�Կ��C++�˽���ĳ���ļ��ļ���,
Ȼ�������ʾ�ļ������ܣ���Ҫ`Ůװ`���ܽ��ܡ�C++���ٸ�Python�˷���һ���źţ�������ʲô��������Լ�������������ascii�ַ�������`boss_iu_nz.jpg`��Python��
�յ����C++�˷���˽Կ��C++���յ�����ļ����н��ܡ�
```
class RSA:
    # This is a prime number pair for rsa768
    def __init__(
    self,
    p=33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489,
    q=36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917,
                 e=65537
                 ):
        self.p = p
        self.q = q
        self.e = e
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.d = self.ext_euclid(e, self.phi)[1] % self.phi

    # extended euclid algorithm
    def ext_euclid(self, a, b):
        if b == 0:
            return (a, 1, 0)
        d, x, y = self.ext_euclid(b, a % b)
        return (d, y, x - a // b * y)

    # fast mod
    def mod(self, a, n, c):
        pow = 1
        while (n):
            if (n & 1):
                pow = (pow * a) % c
            a = (a * a) % c
            n >>= 1
        return pow

    # encrypt a number or a char
    def encrypt_number(self,c):
        if type(c)==int:
            return self.mod(c,self.e,self.n)
        if type(c)==str:
            # use ascii code
            return self.mod(ord(c), self.e, self.n)

    # decrypt a number
    def decrypt_number(self, pw):
        return self.mod(pw, self.d, self.n)

    # encrypt a string by ascii code.
    def encrypt_string(self, s):
        return list(map(self.encrypt_number,s))

    # decrypt a list.
    def decrypt_array2array(self, array):
        return list(map(self.decrypt_number, array))

    # decrypt a list and join it to a string.
    def decrypt_array2str(self, array):
        return "".join(map(lambda x:chr(x),self.decrypt_array2array(array)))

#demo
def main():
    rsa768=RSA()
    test=[1,2,3,4]
    encrypt=rsa768.encrypt_string(test)
    decrypt=rsa768.decrypt_array2array(encrypt)
    print(encrypt)
    print(decrypt)
    test2="wannacry"
    encrypt=rsa768.encrypt_string(test2)
    decrypt=rsa768.decrypt_array2str(encrypt)
    print(encrypt)
    print(decrypt)
    
    
if __name__ == '__main__':
    main()
    
```

