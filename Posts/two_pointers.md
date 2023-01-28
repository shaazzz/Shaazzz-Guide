### Two Pointers
در روش __two pointers__ دو عدد نشانگر بر روی یک ارایه پیمایش داده میشوند.  
هر دو نشانگر یکنواخت میباشند؛ یعنی هر نشانگر از یک جای ارایه شروع به حرکت میکند و یک جا به پایان میرسد و فقط در یک جهت حرکت میکند.

#### مسئله

یک ارایه $a_{1}, a_{2}, \dots, a_{n}(1 \leq a_i \leq 10^{9})$ به طول $n(1 \leq n \leq 10^{6})$ و یک عدد $T$ داریم، به ازای هر $i$ میخواهیم بیشینه $j$ ای را بیابیم به طوری که $\sum_{k=i}^j a_k \leq T$.

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
