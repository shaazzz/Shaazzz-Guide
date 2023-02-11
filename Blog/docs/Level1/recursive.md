--- 
hide:
  - footer
---
# توابع بازگشتی

## توضیحات 
توابع بازگشتی درواقع توابعی هستند که در طول اجرا، خودشان را دوباره صدا می‌زنند. این توابع به نحوی پیاده‌سازی می‌شوند که پایانی وجود داشته باشد و تابع تا ابد ادامه پیدا نکند. عملکرد توابع بازگشتی تاحدودی استقرا طور است. این توابع حتما قسمت‌های پایه‌ای دارند که در این حالت‌ها، تابع دوباره فراخوانده نخواهد شد. بقیه حالات هم با استفاده از تابع برای حالت‌های دیگری حل خواهند شد. برای مثال تابع زیر برای عدد نامنفی $n$، مقدار $n$ را می‌دهد. اما اگر عدد منفی باشد، تا جایی که بتواند بازگشتی پیش می‌برد و از آنجایی که هیچ گاه به پایه `#!cpp lev == 0` نخواهد رسید، به خاطر استفاده بیش از حد از توابع بازگشتی احتمالا با رانتایم ارور یا محدودیت مموری مواجه خواهد شد. از نظر منطقی هم تابع برای اعداد منفی پایان ناپذیر خواهد شد.

``` cpp linenums="1"
int f(int lev){
    if(lev == 0) // (1)!
        return 0;
    return f(lev - 1) + 1; // (2)!
}
```

1.  پایه‌ی تابع بازگشتی

2.  فراخوانی همین تابع به صورت بازگشتی برای مقادیر کمتر

!!! warning ""
    توجه کنید که لزومی ندارد یک تابع فقط یکبار خودش را صدا بزند و ممکن است چندین بار از همان تابع استفاده شده باشد!

نحوه‌ی عملکرد توابع بازگشتی را می‌توان به صورت یک درخت نمایش داد. به طوری که هر مرحله از تابع را به صورت یک رأس نمایش می‌دهیم و آن را به رئوس نماینده‌ی توابعی که صدا زده وصل می‌کنیم. ریشه درخت هم معمولا تابع اولیه هست که توسط بقیه قسمت های کد فراخوانی شده است. برای مثال در تابع بالا، درخت آن یک مسیر ساده خواهد بود که در `#!cpp lev == 0`  پایان خواهد یافت. (البته برای اعداد منفی، مسیری بی نهایت خواهد بود)

### مسئله فیبوناچی

 کد زیر، عدد فیبوناچی ‌$n$ام را به صورت بازگشتی محاسبه می‌کند.

``` cpp linenums="1"
long long fibonacci(int n){
    if(n <= 2) // (1)!
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2); // (2)!
}
```

1.  $F_1 = F_2 = 1$
2.  $F_n = F_{n - 1} + F_{n - 2}$

<figure markdown>

![fib.png](https://i.postimg.cc/MZ76sKzw/fib.png)

  <figcaption>درخت توابع فیبوناچی</figcaption>

</figure>


??? success "پیچیدگی زمانی"
    کد بالا، از $\theta (F_n)$ هزینه میبرد. می‌توان با بررسی درخت متوجه شد که برگ‌ها $F_1$ و $F_2$ هستند که برابر با ۱ هستند. تمام رئوس دیگر صرفا مجموع جواب بچه‌هایشان را محاسبه می‌کنند. پس ما به $F_n$ تا برگ نیاز خواهیم داشت. همچنین چون هر راس غیر برگ لاقل ۲ بچه دارد، تعداد آن‌ها هم حداکثر $F_n$ هست که در مجموع می‌شود از $\theta (F_n)$.


!!! tip "مثال‌های بیشتر"
    می‌توانید درخت توابع بازگشتی پیچیده تری را در قسمت [مرج سورت](/Shaazzz-Guide/Level1/sort/#_7) مشاهده کنید.


### بک‌ترک

الگوریتم های بک‌ترک (Backtracking Algorithms)، الگوریتم‌هایی هستند که برای پیدا کردن جواب مسئله تمام حالات مطلوب را به صورت بازگشتی ساخته و پیمایش خواهند کرد. حتی ممکن است این الگوریتم‌ها با پیمایش کل حالات در جستجوی مقدار خاصی باشند، نه صرفا تمام حالات.

#### مسئله جایگشت‌ها

کد زیر تمام جایگشت‌های $n$تایی را خروجی می‌دهد. تابع `#!cpp perm`  از جایگاه ۰ تا `#!cpp ind - 1`  را با اعدادی که هنوز استفاده نشده‌اند می‌پوشاند. بدین ترتیب اگر در ابتدا تابع `#!cpp perm(n)` فراخوانده شود، خروجی تمام جایگشت‌های ‌$n$  تایی خواهد بود.

``` cpp linenums="1"
int n, a[maxn];
bool mark[maxn];

void perm(int ind){
    if(ind == 0){ // (1)!
        for(int i = 0; i < n; i++)
            cout << a[i] << ' ';
        cout << endl;
        return;
    }
    for(int i = 1; i <= n; i++) if(!mark[i]){ // (2)!
        mark[i] = true; // (3)!
        a[ind - 1] = i;
        perm(ind - 1); // (4)!
        mark[i] = false;
    }
    return;
}
```

1.  تمام اعداد چیده شده‌اند و یک جایگشت ساخته شده است.

2.  اگر $i$ استفاده نشده بود، می‌خواهیم مقدار $ind - 1$ ام از جایگشت ما برابر با $i$ باشد.

3.  مقدار `#!cpp mark[i]`  را `#!cpp true`  می‌کنیم تا مشخص شود استفاده شده است.

4.  ادامه‌ی جایگشت را به صورت بازگشتی می‌سازیم.

??? success "پیچیدگی زمانی"
    اگر درخت این توابع را در نظر بگیرید، می‌توان دید تعداد برگ‌ها $n!$ است. و هر کدام از رئوس دیگر نیز لاقل دو بچه دارند، پس تعداد رئوس درخت از $\theta (n!)$ است. در هر تابع هم مستقل از توابع دیگری که صدا می‌شوند، از $\theta (n)$ هزینه می‌دهیم. پس در کل این کد از $\theta (n \times n!)$ زمان می‌برد.


### ممویز کردن

ممویز کردن (Memoization)، روشی برای بهینه‌سازی زمان اجرای بعضی الگوریتم هاست. به طور خاص در الگوریتم‌های بازگشتی، می‌توان خیلی از توابع که چندین بار در حال محاسبه هستند را حذف کرد. به طور مثال در مسئله‌ی فیبوناچی، می‌توان هر بار یک مقدار از فیبوناچی محاسبه می‌شود آن را نگه داریم تا سری بعدی صدا شدن این تابع، نیازی به محاسبه‌ی دوباره نباشد. با این کار درخت توابع بازگشتی تبدیل به یک مسیر می‌شود که صرفا تعدادی یال به آن اضافه شده است. زمان اجرای کد از $\theta (F_n)$ به $O(n)$ کاهش خواهد یافت! زیرا هر مقدار از 1 تا $n$ حداکثر یکبار محاسبه می‌شود و هر تابع مستقل از توابعی که صدا می‌کند از $O(1)$ است.

``` cpp linenums="1" hl_lines="6"
long long fib[maxn];

long long fibonacci(int n){
    if(n <= 2)
        return 1;
    if(fib[n] != 0) // (1)!
        return fib[n];
    fib[n] = fibonacci(n - 1) + fibonacci(n - 2);
    return fib[n];
}
```

1.  اگر این مقدار از قبل محاسبه شده است، آن را برمی‌گرداند و دیگر محاسبه نمی‌کند.

### هرس کردن

این روش، با حذف بعضی شاخه‌ها از درخت توابع بازگشتی مسائل بک‌ترک، زمان اجرای این توابع را بهتر می‌کند. درواقع بعضی از زیردرخت‌ها از یک درخت هیچ حالت مطلوبی را شامل نمی‌شوند و اگر بتوان سریع متوجه این موضوع شد، می‌توانیم کلا وارد آن‌ها نشویم. برای درک بیشتر، مسئله‌ی زیر را در نظر بگیرید:

#### مسئله پریش

به یک جایگشت از اعداد $1$ تا $n$، پریش گفته می‌شود اگر هیچ عنصری در مکان خودش نباشد. به عبارتی اگر جایگشت را با $\langle p_1, p_2, ..., p_n \rangle \,$ نشان دهیم، شرط $p_i \neq i$ برای تمامی اعضا برقرار باشد. چند جایگشت پریش $n$ تایی وجود دارد؟

یک روش برای حل این مسئله، ساختن تمام جایگشت‌ها و چک کردن پریش بودن یا نبودن آن‌ها در انتهاست. با این کار از $\theta (n \times n!)$ هزینه خواهیم داد. خیلی از این جایگشت‌ها نامطلوب هستند ولی ما تمام آن‌ها را تا آخر ساخته‌ایم. می‌توان به جای این کار، هر جایگشت را صرفا تا اولین جایی که مقدار جایگاهی از آن برابر با خودش شد، ادامه داد. 

``` cpp linenums="1" hl_lines="11"
int n, a[maxn];
bool mark[maxn];

void perm(int ind){
    if(ind == 0){
        for(int i = 0; i < n; i++)
            cout << a[i] << ' ';
        cout << endl;
        return;
    }
    for(int i = 1; i <= n; i++) if(!mark[i] && ind != i){ // (1)!
        mark[i] = true;
        a[ind - 1] = i;
        perm(ind - 1);
        mark[i] = false;
    }
    return;
}
```

1.  تنها در صورتی $i$ را در این خانه می‌گذارد که $i$ برابر با اندیس این خانه نباشد و استفاده هم نشده باشد.


!!! warning ""
    با این کار، زمان اجرا بسیار کاهش میابد. شاید نتوانیم دقیقا مشخص کنیم چقدر بهتر می‌شود، اما به طور واضحی خیلی از جایگشت‌ها از زمان خوبی قطع شده و ادامه داده نمی‌شوند.


### منابع بیشتر

+ [الگوریتم‌های بازگشتی](https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/)
+ [بک‌ترک و تفاوت‌های آن با بازگشتی](https://www.geeksforgeeks.org/backtracking-algorithms/?ref=lbp)
+ [ممویز کردن](https://www.interviewcake.com/concept/java/memoization#:~:text=Memoization%20ensures%20that%20a%20method,usually%20in%20a%20hash%20map)
## سوال ها 
??? warning "نیاز به عضویت در گروه شاززز!"

    برای حل برخی از سوالات باید ابتدا در [گروه شاززز](https://quera.org/course/add_to_course/course/12879/){:target="_blank"} عضو شوید.
| سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[فاکتوریل](https://quera.org/problemset/589/){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li> <li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[الگویابی](https://quera.org/course/assignments/48772/problems/166209){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[پریش](https://quera.org/course/assignments/48772/problems/166207){:target="_blank"}|900|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[Permutations](https://leetcode.com/problems/permutations/){:target="_blank"}|900|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/){:target="_blank"}|900|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[کاشی‌کاری ](https://quera.org/problemset/605/){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Quera](https://quera.org){:target="_blank"}|
|[بی‌ فاصله](https://quera.org/course/assignments/48772/problems/166206){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[جم‌زی](https://quera.org/course/assignments/48772/problems/166208){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[اول‌دایره](https://quera.org/course/assignments/48772/problems/166211){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[شتر](https://quera.org/course/assignments/48772/problems/166212){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[1000-digit Fibonacci number](https://projecteuler.net/problem=25){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li> <li>[پیاده سازی](/Shaazzz-Guide/Level1/implementation){:target="_blank"}</li></ul> </details>|[Project Euler](https://projecteuler.net/){:target="_blank"}|
|[Combinations](https://leetcode.com/problems/combinations/){:target="_blank"}|1000|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li> <li>combinatorics</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Next Permutation](https://leetcode.com/problems/next-permutation/){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-leetcode: [LeetCode](https://leetcode.com/){:target="_blank"}|
|[Easy modified sudoku](https://www.spoj.com/problems/EZSUDOKU/){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-spoj: [Spoj](https://spoj.com/){:target="_blank"}|
|[Little Queens](https://codeforces.com/problemsets/acmsguru/problem/99999/224){:target="_blank"}|1300|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[The Towers of Hanoi Revisited](https://codeforces.com/problemsets/acmsguru/problem/99999/202){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-codeforces: [SGU](https://codeforces.com/problemsets/acmsguru){:target="_blank"}|
|[Xor](https://codeforces.com/problemset/problem/194/D){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Keep Xor Low](https://codeforces.com/problemset/problem/1616/H){:target="_blank"}|2900|<details> <summary>Spoiler</summary> <ul><li>[عملیات های بیتی](/Shaazzz-Guide/Level1/bitmask){:target="_blank"}</li> <li>[توابع بازگشتی](/Shaazzz-Guide/Level1/recursive){:target="_blank"}</li> <li>[تقسیم و حل](/Shaazzz-Guide/Level1/divide){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
