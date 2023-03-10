پریفیکس سام یک ایده ساده و بسیار کاربردی است که ایده اصلی آن شکستن بازه $[l, r]$ به دو بازه $[0, l - 1]$ و $[0, r]$ میباشد.

### الگوریتم

الگوریتم را با سوال کلاسیک پریفیکس سام توضیح می‌دهیم.
فرض کنید یک آرایه $A$ به طول $n$ داریم.
به شما $q$ کوئری از جنس یک بازه‌ی $[l, r]$ می‌دهند و از شما جمع مقادیر $a[l]$, $a[l + 1]$, ..., $a[r]$ را می‌خواهند.

میخواهیم راهی از $O(n + q)$ ارئه دهیم.

در ابتدا آرایه‌ی $ps[n + 1]$ را می‌سازیم و تعریف $ps[i]$ را جمع $i$ عضو اول آرایه $A$ می‌کنیم. سپس با $O(n)$ 
مقادیر آرایه $ps$ را حساب می‌کنیم.

حال برای هر کوئری به شکل $[l, r]$ جواب میشود $ps[l - 1]$ - $ps[r]$.

### کد آنلاین

```cpp
int A[N], ps[N];

int main() {
    int n; cin >>n;

    for(int i = 1; i <= n; i++) 
        cin >>A[i];

    for(int i = 1; i <= n; i++) {
        ps[i] = A[i];
        ps[i] += ps[i - 1];
    }

    int q; cin >>q;
    while(q--) {
        int l, r; cin >>l >>r;
        cout<<ps[r] - ps[l - 1] <<endl;
    }    
}
```

### کد آفلاین

```cpp
int A[N], ans[N];
vector<int> vc[N];

int main() {
      int n; cin >>n;
      for(int i = 1; i <= n; i++) cin >>A[i];

      int q; cin >>q;
      for(int i = 1; i <= q; i++) {
          int l, r; cin >>l >>r;
          vc[l - 1].push_back(-i), vc[r].push_back(i);
      }

      int sum = 0;
      for(int i = 0; i <= n; i++) {
          sum += A[i];
          for(auto j : vc[i]) {
              if(j < 0) ans[-j] -= sum;
              else ans[j] += sum;
          }
      }

      for(int i = 1; i <= q; i++) {
          cout<<ans[i] <<endl;    
      }
}
```

### کاربرد ها

در بسیاری از مسائل کوئری دار شما نمی‌توانید به صورت آنلاین جواب های کوئری ها را حساب کنید.
در این مسائل اگر کوئری ها روی بازه‌های یک دنباله باشند (میتواند دنباله‌ی اصلی خود سوال باشد یا دنباله کوئری ها باشد یا هر چیز دیگری) می‌توانید در ابتدا تمام کوئری ها را بررسی کنید و اطلاعات کوئری ها را روی بازه مورد نظر ثبت کنید و سپس با ترتیب مشخصی روی اعضای بازه فور بزنید و با شکستن هر بازه به دو بازه (در توضیحات اشاره شد) به راحتی جواب مساله خود را بدست آورید.

به طور مثال سوال [Noble Knight's Path](https://codeforces.com/problemset/problem/226/E) سایت CodeForces را در نظر بگیرید.

??? success "ایده کلی راه حل"
    برای حل این سوال می‌توان کوئری ها را به شکل یک بازه دید و به طور مثال برای کوئری $i$ام باید تمام راس هایی را که بین بازه $[y[i], i]$ هستند را ایگنور کرد از درخت و در بین بقیه راس ها راس $k$ام در مسیر را پیدا کرد. بعد از دیدن این کوئری در وکتور دو اندیس $i$ و $j$ اطلاعات این کوئری را اد میکنیم. حالا بار دیگر روی تمام کوئری ها فور میزنیم (در واقع روی اعضای دنباله فور میزنیم) و به هر اندیس که رسیدیم میتوانیم مشاهده کنیم از ابتدا تا این اندیس چند راس بین مسیر جفت راس های در وکتور این اندیس را ایگنور کرده‌ایم. یعنی در واقع برای هر کوئری مانند $i$ توانستیم یک بار راس $k$ام را با ایگنور کردن بازه $[0, y[i] - 1]$ حساب کنیم و بار دیگر راس $k$ام را با ایگنور کردن بازه $[0, i]$ حساب کنیم.
    حالا با این دو دیتا میتوانیم جواب مساله را برای کوئری $i$ام حساب کنیم(ایگنور کردن راس های بازه $[y[i], i]$). (چگونه؟) 

### مطالعه بیشتر

[آنلاین و آفلاین جواب دادن کوئری یعنی چی؟](https://www.geeksforgeeks.org/what-are-online-and-offline-query-based-questions-in-competitive-programming/)

[تابع سی پلاس پلاس برای پریفیکس سام](https://en.cppreference.com/w/cpp/algorithm/partial_sum)

[وکتور در سی پلاس پلاس](https://en.cppreference.com/w/cpp/container/vector)