--- 
hide:
  - footer
comments: true
---
# Two Pointers

## توضیحات 
### Two Pointers
در روش __two pointers__ دو عدد نشانگر بر روی یک ارایه پیمایش داده میشوند.  
هر دو نشانگر یکنواخت میباشند؛ یعنی هر نشانگر از یک جای ارایه شروع به حرکت میکند و یک جا به پایان میرسد و فقط در یک جهت حرکت میکند.

#### مسئله

یک ارایه $a_{1}, a_{2}, \dots, a_{n}(1 \leq a_i \leq T)$ به طول $n(1 \leq n \leq 10^{6})$ و یک عدد $T$ داریم، به ازای هر $i$ میخواهیم بیشینه $j$ ای را بیابیم به طوری که $\sum_{k=i}^j a_k \leq T$.

#### راه حل

فرض کنید $f_i$ بیشینه عددی باشد که $\sum_{k=i}^{f_i} a_k \leq T$ در این صورت ادعا میکنیم:

$$\forall \quad i < j \Longrightarrow f_i \leq f_j $$

??? success "اثبات درستی"
    برهان خلف میزنیم:

    $$ \exists \quad i < j: f_i > f_j $$

    $$1) \sum_{k=j}^{f_j+1} a_k > T $$

    $$ 2) \sum_{k=i}^{j-1} a_k + \sum_{k=j}^{f_j+1} a_k + \sum_{k=f_j+2}^{f_i} a_k \leq T
    \xrightarrow{1 \leq a_m} \sum_{k=j}^{f_j+1} a_k \leq T $$

    که با توجه به نتایج بدست امده از نتیجه $1$ و نتیجه $2$ به تناقض رسیده.
    
با توجه به ادعا گفته شده میتوان نتیجه گرفت:

$$ f_1 \leq f_2 \leq \dots \leq f_n $$

حال کافیست یک نشانگر(pointer) داشته باشیم که روی ارایه پیمایش کند به نام $ptri$ و یک نشانگر دیگر به نام $ptrj$ به طوری که شرط 
$ptrj \leq f_{ptri}$
همواره برقرار بماند.

و به ازای هر مقدار 
$ptri$
مقدار 
$ptrj$
را تاجای ممکن افزایش دهیم.

!!! warning ""
    توجه کنید که با توجه به لم گفته شده با افزایش 
    $ptri$ 
    مقدار 
    $ptrj$ 
    کاهش نمیابد.

#### کد
``` cpp linenums="1"

int main(){
    int n; cin >> n;
    long long T; cin >> T;
    vector<int> a(n);
    for(int i = 0; i < n; i++) cin >> a[i];

    int ptri = 0, ptrj = -1;
    long long sum = 0; // (1)!

    while(ptri < n){
        while(ptrj < n-1 && sum + a[ptrj + 1] <= T) { // (2)!
            ptrj++;
            sum += a[ptrj];
        }
        cout << ptrj + 1 << ' '; // (3)!
        if(ptri <= ptrj) sum -= a[ptri]; // (4)!
        ptri++;
    }
}
```

1. $sum = \sum_{k=ptri}^{ptrj} a_k$

2. $ptrj$ را تا جای ممکن افزایش میدهیم

3. خروجی را به صورت یک بیس نشان میدهیم

4. برای افزایش $ptri$ مقدار $sum$ را به روز رسانی میکنیم



#### پیچیدگی زمانی

توجه کنید که با توجه به این که دو نشانگرمان همواره افزایش میابند و کمتر از 
$n$ 
هستند، و از انجایی که به ازای افزایش هر یک
$O(1)$ 
هزینه میکنیم، پس اردر کل‌مان برابر 
$O(n)$
میشود.


### منابع بیشتر:

+ [Codeforces Edu](https://codeforces.com/edu/course/2/lesson/9)
+ [8.1 - Two Pointers](https://usaco.guide/CPH.pdf#page=87)

## سوال ها 
??? warning "نیاز به عضویت در گروه شاززز!"

    برای حل برخی از سوالات باید ابتدا در [گروه شاززز](https://quera.org/course/add_to_course/course/12879/){:target="_blank"} عضو شوید.
| سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Sum of Three Values](https://cses.fi/problemset/task/1641){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi){:target="_blank"}|
|[Born this way](https://codeforces.com/problemset/problem/1148/B){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[A Tale of Two Lands](https://codeforces.com/problemset/problem/1166/C){:target="_blank"}|1200|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Mysterious Crime](https://codeforces.com/problemset/problem/1043/D){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[رژیم جسی](https://quera.org/course/assignments/48772/problems/168589){:target="_blank"}|1500|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[Same Count One](https://codeforces.com/problemset/problem/1774/D){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Binary String](https://codeforces.com/problemset/problem/1680/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Longest k-Good Segment](https://codeforces.com/problemset/problem/616/D){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Remove the Substring (hard version)](https://codeforces.com/problemset/problem/1203/D2){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Xenia and Colorful Gems](https://codeforces.com/problemset/problem/1336/B){:target="_blank"}|1700|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Read Time](https://codeforces.com/problemset/problem/343/C){:target="_blank"}|1900|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Minimizing Difference](https://codeforces.com/problemset/problem/1244/E){:target="_blank"}|2000|<details> <summary>Spoiler</summary> <ul><li>[باینری سرچ](/Shaazzz-Guide/Level1/binary_search){:target="_blank"}</li> <li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li> <li>[الگوریتم های حریصانه](/Shaazzz-Guide/Level1/greedy){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Double Knapsack](https://codeforces.com/problemset/problem/618/F){:target="_blank"}|3000|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li> <li>[پریفیکس سام](/Shaazzz-Guide/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[I Might Be Wrong](https://codeforces.com/problemset/problem/1693/F){:target="_blank"}|3400|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Shaazzz-Guide/Level1/two_pointers){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
