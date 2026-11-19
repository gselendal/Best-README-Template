# ERPNext Hızlı Başlangıç Rehberi

<p align="center">
  <strong>10 Dakikada ERPNext'e Başlayın!</strong>
</p>

---

## 🚀 Hemen Başlayın

### 1. Hesap Oluşturma (2 dakika)

**Bulut Sürümü (Önerilen):**
1. https://frappecloud.com adresine gidin
2. "Start Free Trial" → 14 gün ücretsiz deneme
3. Site adınızı belirleyin: `sirketiniz.frappe.cloud`
4. E-posta ile kayıt olun

**Yerel Kurulum:**
```bash
# Linux/Mac için tek komut kurulum
wget https://raw.githubusercontent.com/frappe/bench/develop/install.py
sudo python3 install.py --production --user myuser
```

### 2. İlk Yapılandırma (3 dakika)

Giriş yaptıktan sonra açılan sihirbazda:

```
✅ Ülke: Türkiye
✅ Dil: Türkçe
✅ Para Birimi: TRY
✅ Saat Dilimi: Asia/Istanbul

✅ Şirket Adı: ABC Teknoloji A.Ş.
✅ Mali Yıl: 01-01-2026 / 31-12-2026

✅ Sektör: İlgili sektörü seçin
✅ Modüller: İhtiyacınız olanları seçin
```

### 3. İlk Kayıtlar (5 dakika)

#### Müşteri Ekle
```
Satış > Müşteri > Yeni
→ Ad: Örnek Müşteri A.Ş.
→ Grup: Kurumsal
→ Kaydet
```

#### Ürün Ekle
```
Stok > Ürün > Yeni
→ Ürün Kodu: PRD-001
→ Ürün Adı: Laptop Dell XPS
→ Birim: Adet
→ Kaydet
```

#### İlk Fatura Kes
```
Muhasebe > Satış Faturası > Yeni
→ Müşteri seç
→ Ürün ekle
→ Miktar: 1
→ Fiyat: 25.000
→ KDV: %20
→ Kaydet ve Gönder
```

## 📊 Günlük Kullanım Komutları

### Hızlı Arama (AwesomeBar)
```
Ctrl + K → "Satış Faturası" yaz → Enter
```

### Yeni Belge
```
Ctrl + G
```

### En Çok Kullanılan 10 İşlem

| # | İşlem | Kısayol |
|---|-------|---------|
| 1 | **Fatura Kes** | Muhasebe > Satış Faturası > Yeni |
| 2 | **Ödeme Kaydet** | Muhasebe > Ödeme Girişi > Yeni |
| 3 | **Sipariş Al** | Satış > Satış Siparişi > Yeni |
| 4 | **Stok Kontrol** | Stok > Raporlar > Stok Bakiyesi |
| 5 | **Teklif Hazırla** | Satış > Teklif > Yeni |
| 6 | **Alış Yap** | Satın Alma > Satın Alma Siparişi > Yeni |
| 7 | **Devam Kaydı** | İK > Devam > Yeni |
| 8 | **Görev Oluştur** | Proje > Görev > Yeni |
| 9 | **Rapor Al** | İlgili Modül > Raporlar |
| 10 | **Ayarlar** | Ayarlar > Sistem Ayarları |

## 🎯 İlk Hafta Hedefleri

### Gün 1: Temel Kurulum
- ✅ Şirket bilgilerini tamamla
- ✅ 3 müşteri ekle
- ✅ 5 ürün ekle
- ✅ 1 test faturası kes

### Gün 2-3: Stok Yönetimi
- ✅ Depo yapısını oluştur
- ✅ Açılış stoku gir
- ✅ İlk stok hareketi yap

### Gün 4-5: Satın Alma
- ✅ 3 tedarikçi ekle
- ✅ İlk satın alma siparişi
- ✅ Malzeme girişi yap

### Gün 6-7: Raporlar
- ✅ Stok raporu al
- ✅ Satış raporu incele
- ✅ Kâr-zarar raporu kontrol et

## 💡 İpuçları

### Veri Girişi
```
📌 Excel'den toplu veri aktarımı için:
Araçlar > Veri İçe Aktar
```

### Yedekleme
```
⚠️ ÖNEMLİ: Günlük yedek alın!
Ayarlar > Sistem Ayarları > Yedekleme
→ Günlük otomatik yedek: ✅ Aktif
```

### Roller ve İzinler
```
👥 Kullanıcı eklerken doğru rol atayın:
- Muhasebeci → Accounts Manager
- Satış → Sales Manager
- Depo → Stock Manager
```

### Performans
```
⚡ Sistem yavaşlarsa:
1. Önbelleği temizle: Araçlar > Önbelleği Temizle
2. Eski kayıtları arşivle
3. Raporları filtreleyerek çalıştır
```

## 🆘 Acil Durum Çözümleri

### Şifremi Unuttum
```
Giriş ekranında "Şifremi Unuttum" → E-posta gelecek
```

### Yanlış Fatura Kestim
```
Faturayı aç → İptal Et butonu → Düzelt (Amend)
```

### Negatif Stok Hatası
```
Ayarlar > Stok Ayarları
→ "Negatif Stoğa İzin Ver" ✅
```

### Yetki Hatası
```
Ayarlar > Kullanıcılar > [Kullanıcı]
→ Rolleri kontrol et ve ekle
```

## 📱 Mobil Kullanım

### iOS
```
App Store > "ERPNext" ara > İndir
→ Site URL'i gir
→ Kullanıcı adı ve şifre ile giriş
```

### Android
```
Play Store > "ERPNext" ara > İndir
→ Site URL'i gir
→ Kullanıcı adı ve şifre ile giriş
```

### Mobilde En Çok Kullanılanlar
- ✅ Devam kaydı
- ✅ Onay bekleyen belgeler
- ✅ Hızlı fatura kesme
- ✅ Raporları görüntüleme

## 🎓 Öğrenme Kaynakları

### Video Eğitimler
```
YouTube'da arayın:
→ "ERPNext Tutorial Türkçe"
→ "ERPNext Muhasebe"
→ "ERPNext Stok Yönetimi"
```

### Dokümantasyon
```
📚 Resmi Dokümantasyon:
https://docs.erpnext.com

🇹🇷 Türkçe Topluluk Forum:
https://discuss.erpnext.com
```

### Pratik Yapma
```
💪 Test sitesi oluşturun:
→ Gerçek verilerinizi kullanmadan
→ Tüm işlemleri deneyin
→ Hata yapın ve öğrenin!
```

## 🔥 İlk 24 Saatte Yapılması Gerekenler

### Öncelik 1 (Mutlaka)
- [x] Şirket bilgilerini tamamla
- [x] Hesap planını kontrol et
- [x] Otomatik yedeklemeyi aç
- [x] E-posta ayarlarını yap
- [x] Logo yükle

### Öncelik 2 (Önerilen)
- [ ] Baskı formatlarını özelleştir
- [ ] Kullanıcı rollerini belirle
- [ ] Temel ürünleri ekle
- [ ] Müşterileri aktar
- [ ] İlk stok sayımını yap

### Öncelik 3 (İlerisi için)
- [ ] Özel alanlar ekle
- [ ] İş akışları oluştur
- [ ] Raporları özelleştir
- [ ] Entegrasyonları kur
- [ ] Topluluğa katıl

## 📞 Destek

### Ücretsiz Kaynaklar
- **Forum:** https://discuss.erpnext.com
- **GitHub:** https://github.com/frappe/erpnext
- **Telegram:** ERPNext Türkiye grubu

### Ücretli Destek
- **Frappe Cloud:** support@frappe.cloud
- **Danışmanlık:** Forum'da firma listesi

## ✅ Kontrol Listesi

İlk haftanın sonunda şunları yapabilmelisiniz:

- [ ] Fatura kesebiliyorum
- [ ] Ödeme kaydı yapabiliyorum
- [ ] Stok hareketi girebiliyorum
- [ ] Temel raporları alabiliyorum
- [ ] Kullanıcı ekleyebiliyorum
- [ ] Yedek alabiliyorum

Hepsi tamam mı? 🎉 Tebrikler! ERPNext kullanmaya hazırsınız!

---

**Daha Detaylı Bilgi:** `ERPNEXT_KULLANIM_KILAVUZU.md` dosyasına bakın.

**Sürüm:** ERPNext v15 | **Güncelleme:** Kasım 2026
