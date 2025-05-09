**CMS Zaifliklarini Aniqlovchi Dasturi**

### CMS nima?
CMS (Content Management System) — bu raqamli kontentni yaratish va tahrirlashni boshqaradigan tizim. Odatda, bir nechta foydalanuvchilar hamkorlikda ishlashi uchun qulay muhit taqdim etadi. Mashhur misollar: *WordPress, Joomla, Drupal* va boshqalar.

### CMS Zaifliklarini Aniqlovchi Dastur haqida
**CMS Zaifliklarini Aniqlovchi Dastur** (CMSeeK) — bu veb-saytlarning CMS tizimlarini aniqlash va ularning zaifliklarini skaner qilish uchun mo‘ljallangan Python 3 asosidagi vosita. Ushbu dastur 180 dan ortiq CMS tizimlarini aniqlay oladi va maxsus skanerlash funksiyalari orqali sayt xavfsizligini tekshiradi.

### Asosiy funksiyalar
- **180+ CMS aniqlash**: Sayt qaysi CMSda ishlayotganini aniqlaydi.
- **Drupal**: Versiya aniqlash.
- **WordPress uchun maxsus skanerlash**:
  - Versiya aniqlash.
  - Foydalanuvchi ro‘yxatini aniqlash.
  - Plagin va tema ro‘yxatini aniqlash.
  - Zaifliklarni tekshirish va boshqalar.
- **Joomla uchun maxsus skanerlash**:
  - Versiya aniqlash.
  - Zaxira fayllarini qidirish.
  - Admin panelini topish.
  - Asosiy zaifliklarni aniqlash.
  - Konfiguratsiya oqishlarini tekshirish.
- **Modulli bruteforce tizimi**: Tayyor modullardan foydalanish yoki o‘zingiz modul yaratib ulash imkoniyati.

### Talablar va moslik
- **Python 3** talab qilinadi.
- Hozirda **Unix/Linux** tizimlarida ishlaydi (Windows qo‘llab-quvvatlashi keyinroq qo‘shiladi).
- Avtomatik yangilash uchun **git** o‘rnatilgan bo‘lishi kerak.

### O‘rnatish va foydalanish
O‘rnatish juda oson:
1. Quyidagi buyruqlar bilan dasturni yuklab oling:
   ```bash
   git clone https://github.com/Firdavs28033/cms_diplom_ishi
   cd cms_diplom_ishi
   pip3 install -r requirements.txt
   ```
2. Ishga tushirish:
   - Yo‘l-yo‘riqli skanerlash uchun: `python3 cmseek.py`
   - Maxsus saytni skanerlash uchun: `python3 cmseek.py -u <sayt_url>`

### Foydalanish misollari
```bash
python3 cmseek.py -u example.com  # example.com saytini skanerlash
python3 cmseek.py -l saytlar.txt  # saytlar.txt faylidagi saytlarni skanerlash
python3 cmseek.py -u example.com --random-agent  # Tasodifiy user-agent bilan skanerlash
python3 cmseek.py -v -u example.com  # Batafsil natijalar bilan skanerlash
```


**Eslatma**: Yangilanish uchun `git` o‘rnatilgan bo‘lishi shart.

### CMS aniqlash usullari
Dastur quyidagi usullar orqali CMSni aniqlaydi:
- HTTP sarlavhalari.
- Generator meta teglari.
- Sahifa manba kodi.
- `robots.txt` fayli.
- Direktoriya tekshiruvi.

### Qo‘llab-quvvatlanadigan CMSlar
170+ CMS tizimlari qo‘llab-quvvatlanadi. To‘liq ro‘yxatni [cmss.py](https://github.com/Firdavs28033/CMSeeK/blob/master/cmseekdb/cmss.py) faylida ko‘rishingiz mumkin.

### Natijalar saqlanishi
- Barcha skanerlash natijalari `cms.json` faylida saqlanadi.
- Har bir sayt uchun alohida loglar `Result/<Sayt>` papkasida joylashadi.
- Bruteforce natijalari txt faylida saqlanadi.

### Bruteforce modullari
O‘zingizning bruteforce modulingizni qo‘shish imkoniyati mavjud:
1. Modulda `# <CMS nomi> Bruteforce module` va `### cmseekbruteforcemodule` izohlarini qo‘shing.
2. Modulni `brutecms` papkasiga joylashtiring.
3. Keshni yangilash uchun dasturda `R` buyrug‘ini ishlatish.

### Nima uchun CMS Zaifliklarini Aniqlovchi Dasturdan foydalanish kerak?
- Oddiy va qulay interfeys.
- Ko‘p sonli CMSlarni aniqlash.
- Moslashuvchan bruteforce tizimi.
- Va hatto chiqishda turli tillarda tasodifiy xayrlashuv xabarlari! 😄

### Maslahatlar va ogohlantirishlar
- **Muammo ochishda**: Sayt, xato nusxasi, operatsion tizim va Python versiyasini ko‘rsating.
- **Ogohlantirish**: Dasturni faqat ruxsat olingan saytlarda ishlatish kerak. Noqonuniy foydalanish uchun mualliflar javobgar emas.
- **Litsenziya**: GNU General Public License v3.0.

Ushbu dastur veb-sayt xavfsizligini tekshirishda sizga yordam beradi, ammo uni mas'uliyat bilan ishlatish muhim! Agar savollaringiz bo‘lsa, yordam berishga tayyorman! 🚀