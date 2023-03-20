--- 
hide:
  - footer
comments: true
---
# الگوریتم های حریصانه

## توضیحات 
الگوریتم های حریصانه یا گریدی دسته ای از الگوریتم ها هستند که ما در هر مرحله سعی میکنیم همواره بهترین گزینه را انتخاب کنیم. کاربرد این الگوریتم ها بسیار زیاد و متنوع است. در ادامه چند مسئله که به کمک این الگوریتم ها حل میشوند آمده است.
### مسئله کوله پشتی (مایع)
در این مسئله ما 
$n$
مایع داریم که از مایع 
$i$
ام ‍
$L_i$
لیتر وجود دارد قیمت هر لیتر از مایع 
$i$
ام 
$C_i$
تومان است  و وزن هر لیتر از این مایع
$V_i$
گرم است. ما میخواهیم به بازار برویم و مقداری از این 
$n$ 
مایع ها را بفروشیم ولی متاسفانه حداکثر
$W$
گرم میتوانیم حمل کنیم و می خواهیم بدانیم حداکثر فروشی که میتوانیم در یکبار رفتن به بازار داشته باشیم چقدر است.

??? success "راه حل"
    ابتدا مایع ها را بر حسب
    $\frac {C_i} {V_i}$
    از زیاد به کم مرتب میکنیم. برای سادگی در ابتدا فرض کنید هیچ برای هیچ دوتایی این مقدار برابر نیست.
    حال به ترتیب شروع میکنیم و از هر کدام هر چقدر که میتوانیم برداریم برمیداریم.
    یعنی اگر تا کنون 
    $w$
    گرم برداشته ایم از مایع کنونی 
    $min(\frac {W-w} {V_i}  , L_i)$
    لیتر بر می داریم.

    فرض کنید حالتی وجود داشته باشد که فروش بیشتری داشته باشیم.
    بهینه ترین حالت را در نظر بگیرید.
    میدانیم مایع ای وجود دارد که نسبت به حالت اول از آن بیشتر فروخته ایم.
    این مایع را در نظر بگیرید و فرض کنید از آن 
    $l$
    لیتر بیشتر فروخته ایم . اگر مایع ای نباشد که در ترتیب ما زودتر آمده باشد و الان کمتر فروخته شده باشد پس ما از این مایع بیشینه مقدار ممکن را انتخاب نکرده بودیم که تناقض است.
    اگر مایع ای وجود داشته باشد که کمتر فروخته باشیم و در ترتیب ما زود تر آمده باشد میتوانیم از آن بیشتر بفروشیم و از این مایع کمتر و سود بیشتری کسب کنیم پس این حالتی که در نظر گرفتیم بهینه ترین حالت نبوده است که باز هم در تناقض است با فرض خلف ما.

    حال اگر 
    $i$
    و
    $j$
    وجود داشت که 
    $\frac {C_i} {V_i} = \frac {C_j} {V_j}$
    و همچنین
    $R = \frac {V_i} {V_j}$
    آنگاه اگر 
    $l$
    لیتر از مایع 
    $i$
    ام بفروشیم مانند این است که 
    $l \times R$
    لیتر از مایع
    $j$
    بفروشیم پس کافیست به مقدار مایع 
    $j$
    که داریم 
    $L_i \times R$
    واحد اضافه کنیم و خللی در اثبات به وجود نمی آید.
### Matching vs Independent Set
در این مسئله گرافی 
$3 \times n$
راسی داریم و میخواهیم یا مجموعه مستقل  حداقل
$n$
راسی پیدا کنیم یا تطابقی با حداقل 
$n$
یال.
??? success "راه حل" 
    همواره تا وقتی که گراف خالی از یال نشده یک یال را انتخاب میکنیم و رئوس دو سرش به همراه تمام یال های متصل به آن ها را حذف میکنیم حال در انتها اگر حداقل
    $n$
    راس بماند که میدانیم این رئوس یالی بینشان نیست و مجموعه مستقل هستند.
    در غیر این صورت میدانیم بیش از
    $n$
    یال انتخاب کرده ایم زیرا هر مرحله ۲ راس حذف میشوند همچنین رئوس دوسر یال ها دو به دو متفاوت هستند و در نتیجه این یال ها تطابق ما هستند.

!!! tip "نکته"
    در اثبات الگوریتم های حریصانه معمولا در ابتدا فرض خلف میکنیم که جواب بهتری وجود داشته باشد و سپس از بین جواب های بهتر جوابی رو میگیریم 
    که ویژگی خاصی داشته باشد و سپس سعی میکنیم به تناقض برسیم.


## سوال ها 
 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Printed PR](https://codeforces.com/problemsets/acmsguru/problem/99999/259){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Telecasting station](https://codeforces.com/problemsets/acmsguru/problem/99999/114){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Great Sequence](https://codeforces.com/contest/1641/problem/A){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Knapsack](https://codeforces.com/contest/1447/problem/C){:target="_blank"}|1300|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Number Game](https://codeforces.com/problemset/problem/1749/C){:target="_blank"}|1400|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Magic Powder 2](https://codeforces.com/problemset/problem/670/D2){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Zero Array](https://codeforces.com/problemset/problem/1201/B){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Tree Infectoin](https://codeforces.com/contest/1665/problem/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Keshi Is Throwing a Party](https://codeforces.com/problemset/problem/1610/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Equal Frequencies](https://codeforces.com/contest/1782/problem/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Basketball](https://codeforces.com/problemsets/acmsguru/problem/99999/165){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Two Arrays and Sum of Functions](https://codeforces.com/problemset/problem/1165/E){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[secrets](https://codeforces.com/problemset/problem/333/A){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Minimizing Difference](https://codeforces.com/problemset/problem/1244/E){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[Two Pointers](/Level1/two_pointers){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Project Planning](https://atcoder.jp/contests/abc227/tasks/abc227_d){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp){:target="_blank"}|
|[Matching vs Independent Set](https://codeforces.com/problemset/problem/1198/C){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Minimax](https://codeforces.com/contest/1530/problem/E){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[The Human Equation](https://codeforces.com/problemset/problem/1775/E){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Pokémon Army (hard version)](https://codeforces.com/contest/1420/problem/C2){:target="_blank"}|2100|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li> <li>dp</li> <li>segment</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[GukiZ hates boxes](https://codeforces.com/problemset/problem/551/C){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Level1/binary_search){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[New Game Plus!](https://codeforces.com/contest/1456/problem/C){:target="_blank"}|2200|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Coins](https://atcoder.jp/contests/agc018/tasks/agc018_c){:target="_blank"}|2400|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[DeadLee](https://codeforces.com/contest/1369/problem/E){:target="_blank"}|2400|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Taking The Middle](https://atcoder.jp/contests/agc053/tasks/agc053_b){:target="_blank"}|2700|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-atcoder: [Atcoder](https://atcoder.jp){:target="_blank"}|
|[Shop](https://codeforces.com/problemset/problem/521/D){:target="_blank"}|2800|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Candy Shop](https://codeforces.com/problemset/problem/183/E){:target="_blank"}|2900|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Outermost Maximums](https://codeforces.com/problemset/problem/1693/E){:target="_blank"}|3400|<details> <summary>Spoiler</summary> <ul><li>[الگوریتم های حریصانه](/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
