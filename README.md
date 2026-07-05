# Cyber Archives Recovery & Preservation

Güvenli dosya G/Ç işlemleri, context (bağlam) yönetimi, standart akış (stream) manipülasyonu ve savunmacı programlama tekniklerine odaklanan, 42-tarzı katı kısıtlamalar altında yazılmış çok aşamalı bir Python projesi.

## Proje Hakkında

Post-apokaliptik bir dijital dünyada, "Baş Arşivci" parçalanmış dijital bilgileri kurtarmak, dönüştürmek ve güvenli biçimde yedeklemek için sağlam araçlara ihtiyaç duyar. Bu proje; dosya yönetim protokollerine, istisna (exception) yakalamaya ve hata/çıktı akışlarının ayrıştırılmasına sıkı sıkıya bağlı kalınarak Python 3 ile geliştirilmiştir.

## 📁 Depo Yapısı

```
.
├── ex0/
│   └── ft_ancient_text.py
├── ex1/
│   └── ft_archive_creation.py
├── ex2/
│   └── ft_stream_management.py
├── ex3/
│   └── ft_vault_security.py
├── try.txt
└── README.md
```

## Alıştırmaların Detaylı İncelemesi

### 🔹 Alıştırma 0: Cyber Archives Recovery (`ex0/ft_ancient_text.py`)

**Amaç:** Komut satırından verilen bir dosyayı manuel kaynak yönetimiyle açmak, okumak ve ekrana yazdırmak.

**Uygulama Detayları:**
- Argüman sayısı `sys.argv` ile kontrol edilir; yanlış kullanımda kullanım (usage) mesajı basılır.
- `try / except / finally` yapısı ile dosya, bir hata oluşsa bile `finally` bloğunda `.close()` çağrısıyla kesin olarak kapatılır.
- Dosya değişkeni (`file`) `try` bloğunun dışında `None` olarak tanımlanarak, açma işlemi başarısız olduğunda `finally` içinde oluşabilecek `UnboundLocalError` engellenir.

### 🔹 Alıştırma 1: Digital Preservation Protocol (`ex1/ft_archive_creation.py`)

**Amaç:** Bir dosyayı okumak, içeriğine bir dönüşüm (mask) uygulamak ve kullanıcıdan yeni bir konuma kaydetmesini istemek.

**Uygulama Detayları:**
- `splitlines()` ile ayrıştırılan her satırın sonuna liste comprehension kullanılarak `#` karakteri eklenir.
- Yeni dosya adı `input()` ile istenir.
- Girilen dosya adı boşsa veya yalnızca boşluk karakterlerinden oluşuyorsa, program hatasız biçimde kaydetme adımını atlar.
- Biri okuma biri yazma için olmak üzere iki bağımsız dosya nesnesi, kendi `try / finally` bloklarıyla yönetilir.

### 🔹 Alıştırma 2: Standard Stream Management (`ex2/ft_stream_management.py`)

**Amaç:** Normal çıktıyı kritik sistem hatalarından ayırarak akış izolasyonunu bir üst seviyeye taşımak.

**Uygulama Detayları:**
- Hatalar artık `print()` yerine doğrudan `sys.stderr.write()` ile yazdırılır.
- Yeni dosya yolu, düşük seviyeli `sys.stdin.readline().strip()` ile alınır.
- Kullanıcıdan girdi istenmeden önce `sys.stdout.flush()` çağrılarak çıktı akışının anında görünmesi sağlanır.
- Her adım kendi hata yakalama bloğuna sahip olduğundan, bir aşamadaki hata programın diğer bölümlerini kesintiye uğratmaz.

### 🔹 Alıştırma 3: Vault Security (`ex3/ft_vault_security.py`)

**Amaç:** Arşivleme aracını, Python Context Manager'ları kullanan soyut ve sağlam bir modüle dönüştürmek.

**Uygulama Detayları:**
- Ana fonksiyon: `secure_archive(file_name: str, action: str = "read", content: str = "") -> tuple[bool, str]`
- Dosya açma/kapatma yaşam döngüsü tamamen `with` ifadesiyle otomatikleştirilmiştir; manuel `close()` çağrısına gerek yoktur.
- Savunmacı girdi kontrolü: `action` parametresi boş string veya yalnızca boşluk olarak gönderilirse otomatik olarak `"read"` moduna geçilir.
- Yazma modunda içerik (`content`) verilmezse bile boş bir dosya güvenle oluşturulabilir.
- Sonuç, 42 değerlendirme standartlarını yansıtacak şekilde yapılandırılmış bir `tuple` olarak döner: `(True, veri)` ya da `(False, hata_mesajı)`.

## ⚠️ Ele Alınan Uç Durumlar

- **UnboundLocalError Önleme:** Dosya değişkenleri `try` bloklarının dışında tanımlanarak, erken başarısızlık durumlarında `finally` içindeki çökmeler engellenir.
- **Girdi Temizliği:** Kullanıcı tarafından girilen tüm dosya yolları ve action değerleri `.strip()` ile işlenerek gereksiz boşluklardan arındırılır.
- **Akış Bütünlüğü:** Kritik hata kayıtları `stdout`'u kirletmez; bu sayede `2> error.log` gibi terminal yönlendirmeleriyle sorunsuz entegrasyon sağlanır.

## Kalite Güvencesi & Uyumluluk

Kod tabanı, tam tip güvenliği ve PEP 8 uyumluluğunu garanti etmek için standart statik analiz araçlarıyla doğrulanmıştır:

```bash
flake8 ex0/ ex1/ ex2/ ex3/
mypy ex0/ ex1/ ex2/ ex3/
```

## 📄 Test Verisi

`try.txt` dosyası, alıştırmaları test etmek için kullanılan örnek arşiv parçalarını içerir:

```
[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion
```