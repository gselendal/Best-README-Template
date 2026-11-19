# ERPNext Görsel Rehber ve Ekran Görüntüleri

<p align="center">
  <strong>📸 Görsel Yardım ile ERPNext'i Keşfedin</strong>
</p>

---

## 📋 İçindekiler

- [Ana Ekran ve Dashboard](#ana-ekran-ve-dashboard)
- [Modül Navigasyonu](#modül-navigasyonu)
- [İş Akışı Diyagramları](#iş-akışı-diyagramları)
- [Form ve Belge Örnekleri](#form-ve-belge-örnekleri)
- [Rapor Ekranları](#rapor-ekranları)
- [Mobil Görünümler](#mobil-görünümler)

---

## 🖥️ Ana Ekran ve Dashboard

### Giriş Ekranı

<p align="center">
  <img src="images/erpnext/screenshots/login-screen.png" alt="Giriş Ekranı" width="700">
  <br/>
  <em>ERPNext giriş ekranı - Kullanıcı adı ve şifre ile giriş</em>
</p>

**Giriş Ekranı Özellikleri:**
- 🔐 Güvenli kimlik doğrulama
- 🌐 Çok dilli arayüz seçimi
- 🔑 Şifremi unuttum özelliği
- 📱 Mobil uyumlu tasarım

---

### Ana Dashboard

```
┌────────────────────────────────────────────────────────────────────────┐
│  🏠 ERPNext              [🔍 Hızlı Arama: Ctrl+K]    👤 Admin Kullanıcı │
├────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  📊 MODÜL KISA YOLLARı                                                 │
│  ┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐  │
│  │ 💰       │ 💼       │ 🛒       │ 📦       │ 👥       │ 🏭       │  │
│  │ Muhasebe │ Satış    │ Satın A. │ Stok     │ İK       │ Üretim   │  │
│  │          │          │          │          │          │          │  │
│  │ 12 Açık  │ 8 Teklif │ 5 Sip.   │ 3 Uyarı  │ 2 İzin   │ 4 İş E.  │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘  │
│                                                                         │
│  📈 GÜNLÜK KPI KARTLARI                                                │
│  ┌─────────────────┬─────────────────┬─────────────────┬────────────┐ │
│  │ 💰 Günlük Satış │ 📦 Stok Durumu  │ 👥 Devam        │ ⏰ Görevler │ │
│  │                 │                 │                 │            │ │
│  │  ₺ 125.450      │    87%         │   45/48        │   12 Açık  │ │
│  │  ↗️ +15%        │    🟢 Normal    │   🟢 Tam       │   ⏳ 3 Acil│ │
│  └─────────────────┴─────────────────┴─────────────────┴────────────┘ │
│                                                                         │
│  📊 SATIŞ TRENDİ (Son 7 Gün)                                          │
│  ┌──────────────────────────────────────────────────────────────────┐ │
│  │                                                        *            │ │
│  │                                              *                     │ │
│  │                                    *                               │ │
│  │                          *                                         │ │
│  │                *                                                   │ │
│  │      *                                                             │ │
│  │                                                                    │ │
│  └──────────────────────────────────────────────────────────────────┘ │
│    Pzt    Sal    Çar    Per    Cum    Cmt    Paz                      │
│                                                                         │
│  📋 SON İŞLEMLER                      │  ⏰ YAKLASAN GÖREVLER          │
│  ┌────────────────────────────────────┼────────────────────────────┐  │
│  │ 📃 Satış Faturası #INV-2026-00123 │ ⏰ Bordro Hazırlama        │  │
│  │    ABC Teknoloji - 36.360 TL      │    Tarih: 25.11.2026       │  │
│  │    5 dakika önce                  │    Kalan: 6 gün            │  │
│  │                                    │                            │  │
│  │ 💰 Ödeme Girişi #PAY-2026-00089   │ 📦 Stok Sayımı            │  │
│  │    XYZ Ltd - 15.000 TL            │    Tarih: 30.11.2026       │  │
│  │    1 saat önce                    │    Kalan: 11 gün           │  │
│  │                                    │                            │  │
│  │ 📦 Stok Hareketi #STE-2026-00456  │ 📊 Aylık Raporlar         │  │
│  │    Transfer: Depo A → Depo B      │    Tarih: 01.12.2026       │  │
│  │    2 saat önce                    │    Kalan: 12 gün           │  │
│  └────────────────────────────────────┴────────────────────────────┘  │
│                                                                         │
│  [📄 Daha Fazla...]                   [✅ Tümünü Gör]                  │
└────────────────────────────────────────────────────────────────────────┘
```

<p align="center">
  <img src="images/erpnext/screenshots/main-dashboard.png" alt="Ana Dashboard" width="900">
  <br/>
  <em>ERPNext ana dashboard - Tüm iş süreçlerinizin özeti tek ekranda</em>
</p>

---

## 🧭 Modül Navigasyonu

### Modül Geçiş Haritası

```mermaid
graph LR
    A[🏠 Ana Sayfa] --> B[📊 Muhasebe]
    A --> C[💼 Satış]
    A --> D[🛒 Satın Alma]
    A --> E[📦 Stok]
    A --> F[👥 İK]
    A --> G[🏭 Üretim]
    A --> H[📈 Proje]
    A --> I[⚙️ Ayarlar]
    
    B --> B1[Fatura Kes]
    B --> B2[Ödeme Kaydet]
    B --> B3[Raporlar]
    
    style A fill:#1976d2,color:#fff
    style B fill:#4caf50,color:#fff
    style C fill:#ff9800,color:#fff
    style D fill:#9c27b0,color:#fff
    style E fill:#2196f3,color:#fff
    style F fill:#f44336,color:#fff
    style G fill:#795548,color:#fff
    style H fill:#607d8b,color:#fff
    style I fill:#9e9e9e,color:#fff
```

### Awesome Bar (Hızlı Arama)

<p align="center">
  <img src="images/erpnext/screenshots/awesomebar.png" alt="Awesome Bar" width="800">
</p>

**Awesome Bar Kullanımı:**

```
┌─────────────────────────────────────────────────────────────┐
│  🔍 Ara (Ctrl+K): inv                                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  📃 Sales Invoice (Satış Faturası)                          │
│     Yeni fatura oluştur veya mevcut faturaları listele      │
│                                                              │
│  📋 Purchase Invoice (Alış Faturası)                        │
│     Tedarikçi faturası oluştur                              │
│                                                              │
│  💰 Invoice Discounting (Fatura İskontolama)                │
│     Fatura finansmanı                                        │
│                                                              │
│  SON ARAMALAR:                                              │
│  • INV-2026-00123                                           │
│  • INV-2026-00122                                           │
│  • INV-2026-00121                                           │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 İş Akışı Diyagramları

### 1. Tam Satış Döngüsü

```mermaid
graph TD
    Start[🚀 Başlangıç] --> Lead[🔍 Lead<br/>Potansiyel Müşteri]
    Lead --> Qualify{Nitelikli?}
    
    Qualify -->|Evet| Opp[💡 Opportunity<br/>Fırsat]
    Qualify -->|Hayır| Archive1[📦 Arşivle]
    
    Opp --> Quote[📄 Quotation<br/>Teklif]
    Quote --> Approve1{Onay?}
    
    Approve1 -->|Hayır| Lost[❌ Kayboldu]
    Approve1 -->|Evet| SO[📋 Sales Order<br/>Satış Siparişi]
    
    Lost --> Followup[🔄 Follow-up]
    Followup --> Opp
    
    SO --> Stock{Stok<br/>Var mı?}
    
    Stock -->|Hayır| Purchase[🛒 Satın Alma]
    Stock -->|Evet| DN[📦 Delivery Note<br/>Sevkiyat]
    
    Purchase --> Receive[📥 Malzeme Girişi]
    Receive --> DN
    
    DN --> SI[📃 Sales Invoice<br/>Fatura]
    SI --> Payment[💰 Payment Entry<br/>Tahsilat]
    
    Payment --> Complete[✅ Tamamlandı]
    
    Complete --> Report[📊 Raporlar]
    Report --> Analysis[📈 Analiz ve İyileştirme]
    
    style Start fill:#4caf50,color:#fff
    style Complete fill:#2196f3,color:#fff
    style Lost fill:#f44336,color:#fff
    style SO fill:#ff9800,color:#fff
    style SI fill:#9c27b0,color:#fff
    style Payment fill:#00bcd4,color:#fff
```

<p align="center">
  <img src="images/erpnext/workflows/complete-sales-cycle.png" alt="Tam Satış Döngüsü" width="1000">
</p>

---

### 2. Satın Alma ve Stok Akışı

```mermaid
graph TD
    A[📊 Stok Seviyesi] --> B{Minimum<br/>Altında?}
    
    B -->|Evet| C[📝 Material Request<br/>Malzeme Talebi]
    B -->|Hayır| Wait[⏳ İzle]
    
    C --> D[📧 Tedarikçilere<br/>Teklif Talebi]
    D --> E[💵 Supplier Quotation<br/>Tedarikçi Teklifleri]
    
    E --> F[🔍 Fiyat<br/>Karşılaştırma]
    F --> G[📋 Purchase Order<br/>Satın Alma Siparişi]
    
    G --> H[✅ Onay]
    H --> I[📧 Tedarikçiye<br/>Gönder]
    
    I --> J[⏰ Teslimat<br/>Bekleme]
    J --> K[📦 Malzeme Geldi]
    
    K --> L[🔍 Kalite<br/>Kontrol]
    
    L --> M{Uygun?}
    M -->|Hayır| N[🔄 İade]
    M -->|Evet| O[📥 Purchase Receipt<br/>Malzeme Girişi]
    
    N --> D
    
    O --> P[📊 Stok Güncelle]
    P --> Q[📃 Purchase Invoice<br/>Alış Faturası]
    Q --> R[💸 Payment Entry<br/>Ödeme]
    
    R --> S[✅ Süreç Tamamlandı]
    
    style A fill:#2196f3,color:#fff
    style G fill:#ff9800,color:#fff
    style O fill:#4caf50,color:#fff
    style Q fill:#9c27b0,color:#fff
    style S fill:#4caf50,color:#fff
```

---

### 3. Üretim Planlama Akışı

```mermaid
graph TD
    A[📋 Sales Order<br/>Satış Siparişi] --> B[📊 Production Planning<br/>Üretim Planlama]
    
    B --> C[📋 BOM Kontrolü<br/>Ürün Reçetesi]
    C --> D{Hammadde<br/>Yeterli?}
    
    D -->|Hayır| E[🛒 Purchase Planning<br/>Satın Alma Planla]
    D -->|Evet| F[🏭 Work Order<br/>İş Emri]
    
    E --> E1[📝 Material Request]
    E1 --> E2[📋 Purchase Order]
    E2 --> E3[📦 Receive Materials]
    E3 --> F
    
    F --> G[✅ İş Emri Başlat]
    G --> H[🔧 Workstation 1<br/>İşlem 1]
    
    H --> I[⚙️ Workstation 2<br/>İşlem 2]
    I --> J[🔩 Workstation 3<br/>İşlem 3]
    J --> K[✅ Quality Check<br/>Kalite Kontrol]
    
    K --> L{Uygun?}
    L -->|Hayır| M[🔄 Rework<br/>Yeniden İşleme]
    L -->|Evet| N[📦 Finish Good<br/>Mamul]
    
    M --> H
    
    N --> O[📊 Stock Entry<br/>Stok Kaydı]
    O --> P[📦 Delivery Note<br/>Sevkiyat]
    P --> Q[📃 Sales Invoice<br/>Fatura]
    
    style A fill:#2196f3,color:#fff
    style F fill:#ff9800,color:#fff
    style N fill:#4caf50,color:#fff
    style Q fill:#9c27b0,color:#fff
```

---

## 📝 Form ve Belge Örnekleri

### Satış Faturası Formu

<p align="center">
  <img src="images/erpnext/screenshots/sales-invoice-form.png" alt="Satış Faturası Formu" width="900">
</p>

**Fatura Formu Anatomisi:**

```
┌─────────────────────────────────────────────────────────────────┐
│  📃 SATIŞ FATURASI                           [Taslak] [❌]      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Fatura No      : INV-2026-00123          Tarih: 19.11.2026    │
│  Müşteri        : ABC Teknoloji A.Ş.  [🔍] Vade : 30 gün       │
│  Vergi No       : 1234567890                   Vade Tarihi: ... │
│  Adres          : İstanbul, Türkiye                             │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  ÜRÜNLER                                                         │
│  ┌────┬────────────┬──────┬────────┬─────┬────────┬──────────┐ │
│  │ #  │ Ürün Kodu  │ Açık.│ Miktar │Birim│Fiyat   │Toplam    │ │
│  ├────┼────────────┼──────┼────────┼─────┼────────┼──────────┤ │
│  │ 1  │ LAPTOP-001 │Dell  │   2    │Adet │15.000  │30.000 TL │ │
│  │    │            │XPS 13│        │     │        │          │ │
│  ├────┼────────────┼──────┼────────┼─────┼────────┼──────────┤ │
│  │ 2  │ MOUSE-WL   │Kablos│   2    │Adet │  150   │  300 TL  │ │
│  │    │            │uz    │        │     │        │          │ │
│  └────┴────────────┴──────┴────────┴─────┴────────┴──────────┘ │
│                                                                  │
│  [+ Satır Ekle]                                                 │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  ÖZET                                                            │
│  ┌──────────────────────────────────────────────────┐          │
│  │  Ara Toplam                        30.300,00 TL  │          │
│  │  KDV %20                            6.060,00 TL  │          │
│  │  ─────────────────────────────────────────────── │          │
│  │  GENEL TOPLAM                      36.360,00 TL  │          │
│  └──────────────────────────────────────────────────┘          │
│                                                                  │
│  Ödeme Şartları: 30 gün vadeli                                 │
│  Not           : İyi günlerde kullanın                          │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  [💾 Kaydet]  [📤 Kaydet ve Gönder]  [🖨️ Yazdır]  [❌ İptal]   │
└─────────────────────────────────────────────────────────────────┘
```

---

### Ödeme Girişi Formu

<p align="center">
  <img src="images/erpnext/screenshots/payment-entry-form.png" alt="Ödeme Girişi" width="800">
</p>

---

### Stok Hareketi Formu

<p align="center">
  <img src="images/erpnext/screenshots/stock-entry-form.png" alt="Stok Hareketi" width="800">
</p>

---

## 📊 Rapor Ekranları

### Mali Raporlar

#### Bilanço

<p align="center">
  <img src="images/erpnext/screenshots/balance-sheet.png" alt="Bilanço" width="900">
</p>

**Bilanço Örnek Görünüm:**

```
┌─────────────────────────────────────────────────────────────┐
│  📊 BİLANÇO                                                 │
│  Şirket: ABC Teknoloji A.Ş.                                 │
│  Dönem : 01.01.2026 - 30.11.2026                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  AKTİF (VARLIKLAR)                                          │
│  ├─ 💰 Dönen Varlıklar                    2.450.000 TL     │
│  │   ├─ Kasa                                  15.000 TL     │
│  │   ├─ Bankalar                             850.000 TL     │
│  │   ├─ Alıcılar                             925.000 TL     │
│  │   └─ Ticari Mallar                        660.000 TL     │
│  │                                                           │
│  ├─ 🏢 Duran Varlıklar                    1.200.000 TL     │
│  │   ├─ Tesisler, Makine                     900.000 TL     │
│  │   ├─ Taşıtlar                             400.000 TL     │
│  │   └─ Birikmiş Amortisman               (-100.000 TL)    │
│  │                                                           │
│  └─ TOPLAM AKTİF                          3.650.000 TL     │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PASİF (KAYNAKLAR)                                          │
│  ├─ 📋 Kısa Vadeli Borçlar                1.100.000 TL     │
│  │   ├─ Satıcılar                            650.000 TL     │
│  │   ├─ Ödenecek Vergiler                    180.000 TL     │
│  │   └─ Personel Borçları                    270.000 TL     │
│  │                                                           │
│  ├─ 💼 Özkaynaklar                        2.550.000 TL     │
│  │   ├─ Sermaye                            2.000.000 TL     │
│  │   ├─ Geçmiş Yıl Kârları                  300.000 TL     │
│  │   └─ Dönem Net Kârı                      250.000 TL     │
│  │                                                           │
│  └─ TOPLAM PASİF                          3.650.000 TL     │
│                                                              │
│  ✅ Denklik: Aktif = Pasif                                  │
└─────────────────────────────────────────────────────────────┘
```

---

#### Gelir Tablosu

<p align="center">
  <img src="images/erpnext/screenshots/profit-loss.png" alt="Gelir Tablosu" width="900">
</p>

---

#### Nakit Akış Raporu

<p align="center">
  <img src="images/erpnext/screenshots/cash-flow.png" alt="Nakit Akış" width="900">
</p>

---

### Operasyonel Raporlar

#### Stok Bakiye Raporu

<p align="center">
  <img src="images/erpnext/screenshots/stock-balance.png" alt="Stok Bakiye" width="900">
</p>

**Stok Bakiye Tablosu:**

| Ürün Kodu | Ürün Adı | Depo | Miktar | Birim | Birim Fiyat | Toplam Değer | Durum |
|-----------|----------|------|--------|-------|-------------|--------------|-------|
| LAPTOP-001 | Dell XPS 13 | Mamul | 15 | Adet | 15.000 TL | 225.000 TL | 🟢 Normal |
| MOUSE-WL | Kablosuz Fare | Mamul | 125 | Adet | 150 TL | 18.750 TL | 🟢 Normal |
| KB-MEC-01 | Mekanik Klavye | Mamul | 8 | Adet | 850 TL | 6.800 TL | 🟡 Düşük |
| MON-27-4K | 27" 4K Monitör | Mamul | 3 | Adet | 4.500 TL | 13.500 TL | 🔴 Kritik |

---

#### Satış Analizi

<p align="center">
  <img src="images/erpnext/screenshots/sales-analytics.png" alt="Satış Analizi" width="900">
</p>

**Grafik Türleri:**
- 📊 Çubuk grafik (Aylık satış karşılaştırma)
- 📈 Çizgi grafik (Satış trendi)
- 🥧 Pasta grafik (Ürün grubu dağılımı)
- 🎯 Heat map (Satış yoğunluğu)

---

## 📱 Mobil Görünümler

### Mobil Dashboard

<p align="center">
  <img src="images/erpnext/screenshots/mobile-dashboard.png" alt="Mobil Dashboard" width="400">
</p>

**Mobil Özellikler:**

```
┌─────────────────────┐
│  ERPNext         ☰  │
├─────────────────────┤
│                     │
│  📊 Bugün           │
│  ┌─────────────────┐│
│  │ Satış           ││
│  │ ₺ 125.450       ││
│  │ ↗️ +15%         ││
│  └─────────────────┘│
│                     │
│  📋 Bekleyen        │
│  • 5 Onay bekliyor  │
│  • 8 Teklif aşaması │
│  • 3 Stok uyarısı   │
│                     │
│  ⚡ Hızlı İşlem     │
│  [📝 Fatura Kes]    │
│  [💰 Ödeme Kaydet]  │
│  [📦 Stok Hareketı] │
│                     │
│  📱 Offline         │
│  ✅ Etkin           │
│                     │
└─────────────────────┘
```

---

### Mobil Fatura Formu

<p align="center">
  <img src="images/erpnext/screenshots/mobile-invoice.png" alt="Mobil Fatura" width="400">
</p>

---

### Mobil Devam Kaydı

<p align="center">
  <img src="images/erpnext/screenshots/mobile-attendance.png" alt="Mobil Devam" width="400">
</p>

**Devam Kaydı - Tek Tıkla:**

```
┌─────────────────────┐
│  📅 Devam Kaydı     │
├─────────────────────┤
│                     │
│  📅 19.11.2026      │
│  🕐 14:52           │
│                     │
│  👤 Ahmet Yılmaz    │
│  💼 Satış Müdürü    │
│                     │
│  [✅ GELDİM]        │
│                     │
│  ─────────────────  │
│                     │
│  Bugünkü Durum      │
│  ✅ Sabah: 09:00    │
│  ⏸️ Öğle : 12:30    │
│  ✅ Öğle : 13:30    │
│  🏠 Akşam: --:--    │
│                     │
│  ⏱️ Toplam: 4:30    │
│                     │
└─────────────────────┘
```

---

## 🎨 Özelleştirme Örnekleri

### Özel Dashboard Tasarımı

<p align="center">
  <img src="images/erpnext/screenshots/custom-dashboard.png" alt="Özel Dashboard" width="900">
</p>

**Dashboard Bileşenleri:**
- 📊 KPI Kartları
- 📈 Trend Grafikleri
- 📋 To-Do Listesi
- 🔔 Bildirimler
- ⚡ Hızlı İşlem Butonları
- 📱 Widget'lar

---

### Özel Baskı Formatı

<p align="center">
  <img src="images/erpnext/screenshots/custom-print-format.png" alt="Özel Baskı" width="700">
</p>

**Baskı Format Öğeleri:**
- 🏢 Şirket logosu ve bilgileri
- 📋 QR kod (e-fatura için)
- 💧 Filigran
- 🎨 Özel renk şeması
- 📐 Profesyonel layout

---

## 🔍 Arama ve Filtreleme

### Gelişmiş Filtreler

<p align="center">
  <img src="images/erpnext/screenshots/advanced-filters.png" alt="Gelişmiş Filtreler" width="800">
</p>

**Filtre Örnekleri:**

```
┌─────────────────────────────────────────────────┐
│  🔍 SATIŞ FATURALARI - FİLTRELER                │
├─────────────────────────────────────────────────┤
│                                                  │
│  📅 Tarih Aralığı                               │
│  [01.11.2026] → [30.11.2026]                   │
│                                                  │
│  👤 Müşteri                                     │
│  [Tüm Müşteriler ▼]                            │
│                                                  │
│  📊 Durum                                       │
│  ☑️ Taslak                                      │
│  ☑️ Gönderildi                                  │
│  ☐ İptal                                        │
│  ☐ Ödendi                                       │
│                                                  │
│  💰 Tutar                                       │
│  Min: [10.000]  Max: [100.000]                 │
│                                                  │
│  🏢 Şirket                                      │
│  [ABC Teknoloji ▼]                             │
│                                                  │
│  [🔍 Filtrele]  [🔄 Temizle]                   │
└─────────────────────────────────────────────────┘
```

---

## 📖 Sonuç

Bu görsel rehber, ERPNext'in temel özelliklerini ekran görüntüleri ve diyagramlarla açıklamaktadır. 

**Daha Fazla Bilgi:**
- 📚 [Ana Kullanım Kılavuzu](ERPNEXT_KULLANIM_KILAVUZU.md)
- ⚡ [Hızlı Başlangıç](ERPNEXT_HIZLI_BASLANGIC.md)
- 🌐 [Resmi Dokümantasyon](https://docs.erpnext.com)

---

**Not:** Bu rehberdeki ekran görüntüleri örnek amaçlıdır. Gerçek arayüz, ERPNext sürümüne ve özelleştirmelerinize göre değişiklik gösterebilir.

**Son Güncelleme:** Kasım 2026
**Versiyon:** ERPNext v15
