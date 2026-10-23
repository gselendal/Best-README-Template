# Öztiryakiler A3 — Toyota 8 Adım (İyileştirilmiş Format)

Kaynak şablon: `A3-Toyota-8-step-templates.ods` (Toyota 8-step / Cordatus).  
Çıktı: [`Oztiryakiler_A3_Toyota_8_Adim.xlsx`](./Oztiryakiler_A3_Toyota_8_Adim.xlsx)

## Orijinaldeki sorunlar

- EN/TR karışık etiketler; uzun talimat metinleri A3 kutularını dolduruyor
- Adım numarası tutarsızlığı (Monitor 6/7, Countermeasure 5/6)
- A3 baskıya uygun olmayan boş/tekrarlı sütunlar
- Toast örneği üretim bağlamına taşınmıyor; Is/Is Not ve Fishbone boş veya bağlantısız

## Bu paketteki iyileştirmeler

| Değişiklik | Açıklama |
|---|---|
| Temiz A3 yüzeyi | Talimatlar `02_8_Adim_Rehberi` sayfasında; çalışma sayfasında yalnızca doldurma alanları |
| Doğru 8 adım | 1 Tanımla → 2 Kır → 3 Hedef → 4 Kök neden → 5 Önlem → 6 Uygula → 7 İzle → 8 Standartlaştır |
| Türkçe tutarlı dil | Sahada kullanılacak net etiketler |
| A3 yatay baskı | Landscape + A3 kağıt boyutu, fit-to-page |
| Gerçekçi örnek | Öztiryakiler GN 2/1 dik tip monoblok buzdolabı — kapı contası FPY |
| Destek formları | Is/Is Not, 5 Neden, Pareto/trend, aksiyon planı dolu |

## Örnek proje (senaryo)

- **A3-2026-07** — GN 2/1 Dik Tip BD Conta Sızdırmazlık FPY
- Hat: Soğuk Üniteler / Büyükçekmece / dik tip monoblok (örn. GN 1200 NMV)
- Hedef: FPY %86 → %96; conta red ≤ %1,5 (30.06.2026)
- Kök neden: Preventif kalıp/mastar kontrol standardı yok + sıcaklık drift + tork SWI eksik + Shore A lot varyasyonu

> Not: İsimler, metrikler ve tarihler eğitim amaçlı örnek veridir; gerçek fabrika KPI’sı değildir.

## Sayfalar

1. `00_Icindekiler`
2. `01_Analiz` — ODS analizi
3. `02_8_Adim_Rehberi`
4. `03_A3_Sablon_Bos` — yeni projeler için boş şablon
5. `03_A3_Oztiryakiler` — dolu örnek A3
6. `04_Is_IsNot` / `04_Kok_Neden`
7. `05_Pareto_Trend` — grafikler
8. `06_Aksiyon_Plani`
9. `07_Hedef_Yazimi`

Yeniden üretmek: `python3 generate_a3_workbook.py`
