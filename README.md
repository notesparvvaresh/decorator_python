## دکوراتور‌ها در Python و Django

**Decorator** در Python یک **function** است که یک **function** دیگر را به عنوان ورودی می‌گیرد و نسخه‌ای جدید از آن را با قابلیت‌های اضافه برمی‌گرداند، بدون اینکه کد اصلی تغییر کند.
از **decorator** معمولاً برای کارهایی مثل **logging**، **validation**، **caching** و **access control** استفاده می‌شود.

### مثال ساده در Python

```python

def my_decorator(func):
    def warpper():
        print("-- start")
        func()
        print("-- finish")
    return warpper


@my_decorator
def test():
    print("this is a test")

test()

```

---

### دکوراتور در Django

Django تعداد زیادی **decorator** آماده دارد که کارهای رایج توسعه وب را ساده می‌کنند:

* **`@login_required`** → محدود کردن دسترسی یک **view** به کاربران لاگین کرده.
* **`@permission_required('app.permission')`** → بررسی داشتن **permission** خاص برای کاربر.
* **`@csrf_exempt`** → معاف کردن یک **view** از بررسی CSRF.
* **`@cache_page(timeout)`** → **cache** کردن خروجی یک **view** برای مدت مشخص.

مثال:

```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return HttpResponse("wellcode to dashboard")
```

---

**خلاصه:**
در Python، **decorator** روشی انعطاف‌پذیر برای افزودن یا تغییر رفتار **function** و **method** است.
در Django، از آن برای **authentication**، **authorization**، **security** و **performance optimization** استفاده می‌شود.

-