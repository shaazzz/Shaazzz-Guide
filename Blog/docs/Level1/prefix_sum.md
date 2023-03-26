--- 
hide:
  - footer
comments: true
---
# پریفیکس سام

## توضیحات 
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
## سوال ها 
??? warning "نیاز به عضویت در گروه شاززز!"

    برای حل برخی از سوالات باید ابتدا در [گروه شاززز](https://quera.org/course/add_to_course/course/12879/){:target="_blank"} عضو شوید.
 <form name="cf-handel-form" class="cf-handel-form" onsubmit="return cf_status_checker()">
  <input type="text" id="cf-handel" name="cf-handel" class="handel-input" placeholder="هندل کدفرسز:"><br>
  <input type="submit" value="Submit" class="md-button cf-handel-button">
</form> | سوال | سختی | تگ ها | جاج | 
| :-----: | :----: | :----: | :----: | 
|[Prefix Sum Queries](https://cses.fi/problemset/task/2166){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi){:target="_blank"}|
|[ایکسور خفن](https://quera.org/course/assignments/48772/problems/168588){:target="_blank"}|800|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-quera: [Shaazzz](https://quera.org/course/add_to_course/course/12879/){:target="_blank"}|
|[Max Subarray Sum](https://cses.fi/problemset/task/1643){:target="_blank"}|900|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi){:target="_blank"}|
|[Subarray Sums II](https://cses.fi/problemset/task/1661){:target="_blank"}|1100|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li> <li>[مرتب سازی](/Level1/sort){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi){:target="_blank"}|
|[Ilya and Queries](https://codeforces.com/problemset/problem/313/B){:target="_blank"}|1100|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Forest Queries](https://cses.fi/problemset/task/1652){:target="_blank"}|1100|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-cses: [CSES](https://cses.fi){:target="_blank"}|
|[Star sky](https://codeforces.com/contest/835/problem/C){:target="_blank"}|1600|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Boboniu Chats with Du](https://codeforces.com/contest/1394/problem/A){:target="_blank"}|1800|<details> <summary>Spoiler</summary> <ul><li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li> <li>tow_pointers</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
|[Double Knapsack](https://codeforces.com/problemset/problem/618/F){:target="_blank"}|3000|<details> <summary>Spoiler</summary> <ul><li>[Two Pointers](/Level1/two_pointers){:target="_blank"}</li> <li>[پریفیکس سام](/Level1/prefix_sum){:target="_blank"}</li></ul> </details>|:judge-codeforces: [Codeforces](https://codeforces.com/){:target="_blank"}|
