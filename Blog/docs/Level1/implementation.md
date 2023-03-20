--- 
hide:
  - footer
comments: true
---
# پیاده سازی

## توضیحات 
به طور کلی، روند حل سوال عملی، شامل ۲ بخش ارائه الگوریتم برای سوال و نوشتن کد الگوریتم ارائه داده شده می‌باشد. برای تقویت مهارت پیاده سازی، فقط تمرین بیشتر و نوشتن کد سوالات ساده نیاز است.

#### زبان برنامه نویسی

در المپیاد کامپیوتر ایران، تنها استفاده از زبان برنامه نویسی **سی پلاس پلاس** مجاز است.

!!! warning ""
    دقت کنید که در دوره های اخیر المپیاد کامپیوتر، تنها استفاده از c++ 11 مجاز بوده است.

توصیه می‌شود قبل از شروع یادگیری الگوریتم‌ها، به مفاهیم زیر در زبان سی پلاس پلاس تسلط کافی داشته باشید:

+ خواندن ورودی و خروجی
+ متغیر ها
+ عملگر های ریاضی
+ شرط ها و حلقه ها
+ آرایه
+ توابع

همچنین پس از یادگیری مفاهیم فوق، یادگیری استفاده از داده ساختار های زیر توصیه می‌شود:

+ [stack](https://cplusplus.com/reference/stack/stack/)
+ [queue](https://cplusplus.com/reference/queue/queue/)
+ [vector](https://cplusplus.com/reference/vector/vector/)
+ [deque](https://cplusplus.com/reference/deque/deque/)
+ [set](https://cplusplus.com/reference/set/set/)
+ [map](https://cplusplus.com/reference/map/map/)

در پایان، مطالعه در مورد بعضی از کتابخانه های سی پلاس پلاس مانند [algorithm](https://cplusplus.com/reference/algorithm/) و [cmath](https://cplusplus.com/reference/cmath/) می‌تواند مفید واقع شود.

#### چند منبع مفید برای یادگیری سی پلاس پلاس

+ [W3schools](https://www.w3schools.com/cpp/default.asp)
+ [C++ Tutorial for Beginners](https://www.youtube.com/watch?v=vLnPwxZdW4Y&vl=en)

#### چند بلاگ برای یادگیری توابع و نکات کاربردی سی پلاس پلاس در المپیاد

+ [C++ Tricks](https://codeforces.com/blog/entry/15643)
+ [Writing C++ like Python](https://codeforces.com/blog/entry/111253)
+ [C++ Tips and Tricks](https://codeforces.com/blog/entry/74684)
+ [C++17 - Competitive programming edition](https://codeforces.com/blog/entry/57729)

#### محیط کدنویسی

برای شروع، استفاده از ادیتور ها و ide هایی همچون Code::Blocks و ++DevC توصیه می‌شود، همچنین تکست ادیتور هایی مانند Visual Studio Code، Sublime Text و vim نیز می‌توانند کمک کننده باشند.

!!! warning ""
    در برخی دوره های المپیاد کامپیوتر ایران، استفاده از تکست ادیتور vim اجباری بوده! همچنین در تمامی آزمون های نهایی تابستان، از سیستم عامل Ubuntu استفاده می‌شود.

### تمرین بیشتر برای پیاده سازی

یکی از تمرین های مفید برای بهبود مهارت پیاده سازی، حل سوالات ساده سایت [Codeforces](https://codeforces.com/)  و [کوئرا](https://quera.org/) است، با ورود به این سایت ها و مرتب کردن سوالات بر حسب تعداد حل آنها، می‌توانید ساده ترین سوالات این ۲ سایت را حل کنید.

### ورودی و خروجی سریع تر

خواندن ورودی و نوشتن خروجی، در حالت عادی زمان زیادی را به خود می‌گیرد و اگر ورودی یا خروجی سوالات بزرگ باشند، می‌تواند دردسر ساز باشد. با استفاده از کد زیر، می‌توانید ورودی و خروجی گرفتن را در برنامه خود سریع تر کنید([مطالعه بیشتر](https://codeforces.com/blog/entry/90775))

```cpp
// ...

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    // ...
}
```

### ذخیره اعداد بزرگ(‌BigNum)

هیچ متغیری در سی پلاس پلاس، توانایی ذخیره اعداد بزرگتر از $2^{64}$ را ندارد. همچنین برخلاف زبان های برنامه نویسی همچون Java، هیچ کتابخانه ای در سی پلاس پلاس به این موضوع اختصاص داده نشده، اما در برخی از سوالات، به ذخیره و کار با چنین اعدادی نیاز می‌شود. توصیه می‌شود به عنوان تمرین پیاده سازی، داده ساختاری بسازید که بتواند اعداد به هر سایزی را در خود نگه دارد، بتواند روی آن‌ها عملیات های ساده ریاضی انجام دهد و همچنین بتواند ۲ عدد را مقایسه کند(می‌توانید کد خود را روی [این سوال](https://codeforces.com/problemsets/acmsguru/problem/99999/112) امتحان کنید) همچنین در سایر سوالات(بجز سوالات این بخش) در صورت نیاز، میتوانید از [این کد](https://gist.github.com/ar-pa/957297fb3f88996ead11) استفاده کنید.

!!! warning ""
    پیشنهاد می‌شود از کد آماده داده شده در سوالات این بخش استفاده نکنید و سعی کنید خودتان داده ساختار مورد نیاز را پیاده کنید!

## سوال ها 
| سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[a + b](https://codeforces.com/problemsets/acmsguru/problem/99999/100){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[فاکتوریل](https://quera.org/problemset/589/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li> <li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[اعداد فیثاغورثی](https://quera.org/problemset/9774/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[Distinc Digits](https://codeforces.com/contest/1228/problem/A){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[مثلث خیام پاسکال](https://quera.org/problemset/3410/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[توان ۲](https://quera.org/problemset/616/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[چاپ لوزی](https://quera.org/problemset/618/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[عدد خود مغلوب](https://quera.org/problemset/617/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[لوزی های ستاره ای](https://quera.org/problemset/9773/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[تک رقمی](https://quera.org/problemset/3539/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[مبنا](https://quera.org/problemset/594/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[مسابقه پیاده سازی کوئرا(همه سوالات)](https://quera.org/contest/assignments/42708/problems/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[مسابقه پیاده سازی کوئرا(همه سوالات)](https://quera.org/contest/assignments/35049/problems){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[a^b - b^a](https://codeforces.com/problemsets/acmsguru/problem/99999/112){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Spam Filter](https://codeforces.com/problemsets/acmsguru/problem/99999/274){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Lexicographic permutations](https://projecteuler.net/problem=24){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|[Project Euler](https://projecteuler.net/){:target="_blank"}|
|[1000-digit Fibonacci number](https://projecteuler.net/problem=25){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li> <li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|[Project Euler](https://projecteuler.net/){:target="_blank"}|
|[Factorial digit sum](https://projecteuler.net/problem=20){:target="_blank"}|1300|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|[Project Euler](https://projecteuler.net/){:target="_blank"}|
