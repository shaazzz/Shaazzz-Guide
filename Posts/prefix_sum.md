پریفیکس سام یک ایده ساده و بسیار کاربردی است که ایده اصلی آن شکستن بازه $[l, r]$ به دو بازه $[0, l - 1]$ و $[0, r]$ میباشد.

### الگوریتم

الگوریتم را با سوال کلاسیک پریفیکس سام توضیح می‌دهیم.
فرض کنید یک آرایه $A$ به طول $n$ داریم.
به شما $q$ کوئری از جنس یک بازه‌ی $[l, r]$ می‌دهند و از شما جمع مقادیر $a[l], a[l + 1], ..., a[r]$ را می‌خواهند.

میخواهیم راهی از $O(n + q)$ ارئه دهیم.

در ابتدا آرایه‌ی $ps[n + 1]$ را می‌سازیم و $ps[i]$ را برابر با جمع $i$ عضو اول آرایه $A$ قرار می‌دهیم. (مقادیر آرایه $ps$ از $O(n)$
قابل محاسبه هستند)

حال برای هر کوئری به شکل $[l, r]$ جواب میشود $ps[l - 1] - ps[r]$.

### کد

```cpp linenums="1"

int A[N], ps[N];

int main() {
    int n; cin >> n;

    for(int i = 1; i <= n; i++)
        cin >> A[i];

    for(int i = 1; i <= n; i++) {
        ps[i] = A[i];
        ps[i] += ps[i - 1];
    }

    int q; cin >>q;
    while(q--) {
        int l, r; cin >> l >> r;
        cout << ps[r] - ps[l - 1] << endl;
    }
}
```

### کد آفلاین

در روش قبلی می‌توانستیم بعد از دریافت هر کوئری، جواب آن را سریعا اعلام کنیم. در این روش جواب کوئری‌ها در لحظه محاسبه نمی‌شوند و در انتها جواب تمام کوئری ها داده خواهد شد. این روش در این مسئله‌ی خاص به نسبت روش آنلاین ضعیف تر است و حدودا مزیت خاصی ندارد اما ایده‌ی به کار رفته ممکن است در سوالات دیگری به کار آید.

```cpp linenums="1"

int A[N], ans[N];
vector<int> vc[N];

int main() {
    int n; cin >> n;
    for(int i = 1; i <= n; i++) cin >> A[i];

    int q; cin >>q;
    for(int i = 1; i <= q; i++) {
        int l, r; cin >> l >> r;
        vc[l - 1].push_back(-i);
        vc[r].push_back(i);
    }

    int sum = 0;
    for(int i = 0; i <= n; i++) {
        sum += A[i];
        for(auto j : vc[i]) {
            if(j < 0)
                ans[-j] -= sum;
            else
                ans[j] += sum;
        }
    }

    for(int i = 1; i <= q; i++) {
        cout << ans[i] << endl;
    }
}
```

### کاربرد ها

در بسیاری از مسائل کوئری دار شما نمی‌توانید به صورت آنلاین جواب کوئری ها را حساب کنید.
در این مسائل اگر کوئری ها روی بازه‌های یک دنباله باشند، می‌توانید در ابتدا تمام کوئری ها را بررسی کنید و اطلاعات کوئری ها را روی بازه مورد نظر ثبت کنید و سپس با ترتیب مشخصی روی اعضای بازه فور بزنید و با شکستن هر بازه به دو بازه (در توضیحات اشاره شد) به راحتی جواب مساله خود را بدست آورید.

### مطالعه بیشتر

[آنلاین و آفلاین جواب دادن کوئری یعنی چی؟](https://www.geeksforgeeks.org/what-are-online-and-offline-query-based-questions-in-competitive-programming/)

[تابع سی پلاس پلاس برای پریفیکس سام](https://en.cppreference.com/w/cpp/algorithm/partial_sum)