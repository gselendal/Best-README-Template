#!/usr/bin/env python3
"""Generate improved Toyota 8-step A3 workbook for Öztiryakiler fridge production."""

from openpyxl import Workbook
from openpyxl.styles import (
    Font, Fill, PatternFill, Border, Side, Alignment, NamedStyle
)
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.worksheet.page import PageMargins

wb = Workbook()

# --- palette ---
NAVY = "1B3A4B"
TEAL = "2A6F7F"
ACCENT = "C45C26"
LIGHT = "F4F7F8"
HEADER_BG = "1B3A4B"
STEP_BG = "2A6F7F"
SOFT = "E8EEF0"
WHITE = "FFFFFF"
DARK = "1A1A1A"
MUTED = "5A6A72"
OK_GREEN = "1F6F4A"
WARN = "B45309"

thin = Border(
    left=Side(style="thin", color="B8C4C9"),
    right=Side(style="thin", color="B8C4C9"),
    top=Side(style="thin", color="B8C4C9"),
    bottom=Side(style="thin", color="B8C4C9"),
)
thick = Border(
    left=Side(style="medium", color=NAVY),
    right=Side(style="medium", color=NAVY),
    top=Side(style="medium", color=NAVY),
    bottom=Side(style="medium", color=NAVY),
)


def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)


def font(size=10, bold=False, color=DARK, name="Calibri"):
    return Font(name=name, size=size, bold=bold, color=color)


def align(h="left", v="center", wrap=True):
    return Alignment(horizontal=h, vertical=v, wrap_text=wrap)


def style_range(ws, cell_range, **kwargs):
    from openpyxl.utils import range_boundaries
    min_c, min_r, max_c, max_r = range_boundaries(cell_range)
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            cell = ws.cell(r, c)
            if "fill" in kwargs:
                cell.fill = kwargs["fill"]
            if "font" in kwargs:
                cell.font = kwargs["font"]
            if "border" in kwargs:
                cell.border = kwargs["border"]
            if "alignment" in kwargs:
                cell.alignment = kwargs["alignment"]


def set_cols(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def merge_write(ws, cell_range, value, f=None, fl=None, al=None, br=None):
    ws.merge_cells(cell_range)
    cell = ws[cell_range.split(":")[0]]
    cell.value = value
    if f:
        cell.font = f
    if fl:
        cell.fill = fl
    if al:
        cell.alignment = al
    if br:
        style_range(ws, cell_range, border=br)
    else:
        style_range(ws, cell_range, border=thin)
    if f:
        style_range(ws, cell_range, font=f)
    if fl:
        style_range(ws, cell_range, fill=fl)
    if al:
        style_range(ws, cell_range, alignment=al)
    return cell


# =============================================================================
# SHEET 1: Analiz & İyileştirmeler
# =============================================================================
ws = wb.active
ws.title = "01_Analiz"

set_cols(ws, [4, 28, 55, 40, 4])
ws.row_dimensions[1].height = 28
merge_write(
    ws, "B1:D1",
    "A3 Toyota 8-Adım Şablon Analizi ve İyileştirme Notları",
    f=font(16, True, WHITE), fl=fill(NAVY), al=align("left", "center"),
)

content = [
    ("Kaynak", "A3-Toyota-8-step-templates.ods (Cordatus / Bernie Rushe; TR uyarlama: Cevdet Dal)"),
    ("Kapsam", "Toyota 8 adımlı problem çözme + A3 tek sayfa raporlama"),
    ("", ""),
    ("Orijinaldeki sorunlar", ""),
    ("1. Karışık dil", "Kutu başlıkları EN/TR karışık; talimat metinleri hücreleri dolduruyor, yazılacak alan daralıyor."),
    ("2. Adım numarası tutarsızlığı", "Monitor kutusu başlıkta 6, TR etiketinde 7; Countermeasure seçimi 5/6 karışık."),
    ("3. Talimat kirliliği", "Her kutuda uzun İngilizce prosedür listesi var → A3 okunabilirliğini düşürüyor."),
    ("4. Yazdırma düzeni", "Çok sayıda boş/tekrarlı sütun; A3 (420×297 mm) baskıya uygun değil."),
    ("5. Örnek zayıf", "Toast örneği eğitim amaçlı ama üretim bağlamına taşınmıyor."),
    ("6. Yardımcı formlar boş", "Is/Is Not ve Fishbone şablonları doldurulmamış veya örnekle bağlantısız."),
    ("", ""),
    ("Bu paketteki iyileştirmeler", ""),
    ("A. Temiz A3 yüzeyi", "Talimatlar ayrı sayfada; çalışma sayfasında yalnızca başlık + doldurma alanları."),
    ("B. Doğru 8 adım sırası", "1 Tanımla → 2 Kır → 3 Hedef → 4 Kök neden → 5 Önlem geliştir → 6 Uygula → 7 İzle → 8 Standartlaştır."),
    ("C. Türkçe tutarlı dil", "Üretim / kalite ekiplerinin sahada kullanacağı net TR etiketler."),
    ("D. A3 yatay baskı", "Sayfa boyutu A3 landscape, sütun/satır oranları tek sayfaya sığacak şekilde."),
    ("E. Gerçekçi örnek", "Öztiryakiler GN 2/1 dik tip monoblok buzdolabı hattı — kapı contası FPY."),
    ("F. Destek sayfaları", "Is/Is Not, 5 Neden, Balık kılçığı, Pareto verisi, aksiyon planı dolu."),
    ("", ""),
    ("Örnek proje özeti", ""),
    ("Firma / Hat", "Öztiryakiler — Soğuk Üniteler / GN 2/1 Dik Tip Monoblok Buzdolabı (örn. GN 1200 NMV)"),
    ("Problem", "Final testte kapı contası sızdırmazlık ve sıcaklık kararlılığı redleri yüksek; FPY düşük."),
    ("Hedef", "FPY %86 → %96; conta kaynaklı red ≤ %1,5 (30.06.2026)"),
    ("Kök neden", "Conta kanal toleransı + yapıştırma sıcaklığı drift + montaj tork standardı yok."),
]

r = 3
for title, body in content:
    ws.row_dimensions[r].height = 22 if body else 10
    if title and not body:
        merge_write(ws, f"B{r}:D{r}", title, f=font(12, True, WHITE), fl=fill(TEAL), al=align("left"))
    elif title:
        ws.cell(r, 2, title).font = font(10, True, NAVY)
        ws.cell(r, 2).fill = fill(SOFT)
        ws.cell(r, 2).border = thin
        merge_write(ws, f"C{r}:D{r}", body, f=font(10), fl=fill(WHITE), al=align("left"))
    r += 1

ws.page_setup.orientation = "landscape"
ws.page_setup.paperSize = ws.PAPERSIZE_A4

# =============================================================================
# SHEET 2: 8 Adım Rehberi (talimatlar ayrı)
# =============================================================================
ws = wb.create_sheet("02_8_Adim_Rehberi")
set_cols(ws, [6, 28, 55, 40])
merge_write(ws, "A1:D1", "Toyota 8 Adımlı Problem Çözme — Kısa Rehber (A3’e yazılmaz)",
            f=font(14, True, WHITE), fl=fill(NAVY), al=align("left"))
headers = ["Adım", "Amaç", "Soru / Odak", "Tipik araçlar"]
for i, h in enumerate(headers, 1):
    c = ws.cell(2, i, h)
    c.font = font(10, True, WHITE)
    c.fill = fill(TEAL)
    c.border = thin
    c.alignment = align("center")

steps = [
    ("1. Problemi netleştir", "Kapsamı ve müşteri etkisini tanımla", "Nedir / Ne değildir? Kim etkileniyor?", "VOC, Is/Is Not, Gemba, paydaş analizi"),
    ("2. Problemi kır", "Boyut, parçalar, veri", "Ne kadar büyük? Nerede yoğunlaşıyor?", "Pareto, SIPOC, proses haritası, run chart"),
    ("3. Hedef koy", "Ölçülebilir, gerçekçi hedef", "Fiilden tarihe kadar net hedef cümlesi", "Hedef formatı: Fiil + nesne + from→to + tarih"),
    ("4. Kök neden analizi", "Gerçek kök nedeni bul", "Neden–neden…? Kanıt var mı?", "5 Neden, balık kılçığı, FMEA, stratifikasyon"),
    ("5. Önlemleri geliştir", "Birçok karşı önlem üret, önceliklendir", "Kök nedene doğrudan etki ediyor mu?", "Beyin fırtınası, etki–çaba matrisi"),
    ("6. Önlemi seç & uygula", "Pratik + etkili olanı uygula", "Kim / ne / ne zaman? Pilot?", "Aksiyon planı, Gantt, Poka-yoke, SMED"),
    ("7. Sonuç & süreci izle", "Etkiyi doğrula, sapmaları yakala", "Hedefe yaklaşıyor muyuz?", "Kontrol grafiği, FPY trend, PIR"),
    ("8. Standartlaştır & paylaş", "Yeni standardı kilitle, yay", "Prosedür güncellendi mi? Yatay yayılım?", "Standart iş, görsel yönetim, eğitim, yatay deployment"),
]
for i, row in enumerate(steps, 3):
    for j, val in enumerate(row, 1):
        c = ws.cell(i, j, val)
        c.font = font(10, bold=(j == 1))
        c.border = thin
        c.alignment = align("left")
        c.fill = fill(SOFT if i % 2 == 0 else WHITE)
    ws.row_dimensions[i].height = 36

# =============================================================================
# Helper to build A3 sheet layout
# =============================================================================

def build_a3_sheet(ws, filled=True):
    """Landscape A3-like grid: header + 8 step boxes in classic left/right story flow."""
    # Column widths tuned for A3 landscape (~12 cols usable)
    widths = [3.2, 14, 14, 14, 14, 14, 3.2, 14, 14, 14, 14, 14, 3.2]
    set_cols(ws, widths)
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.page_setup.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 1
    ws.page_margins = PageMargins(left=0.4, right=0.4, top=0.35, bottom=0.35)
    ws.print_area = "A1:M42"

    # Row heights
    for r in range(1, 43):
        ws.row_dimensions[r].height = 15
    ws.row_dimensions[1].height = 22
    ws.row_dimensions[2].height = 18
    ws.row_dimensions[3].height = 18
    ws.row_dimensions[4].height = 18

    # --- Header band ---
    merge_write(ws, "B1:F1", "A3 NO / PROJE ADI", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))
    merge_write(ws, "H1:J1", "TAKIM ÜYELERİ", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))
    merge_write(ws, "K1:L1", "PAYDAŞLAR", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))

    if filled:
        merge_write(ws, "B2:F3",
                    "A3-2026-07  |  GN 2/1 Dik Tip BD Conta Sızdırmazlık FPY\nÖztiryakiler — Soğuk Üniteler / Büyükçekmece",
                    f=font(11, True, NAVY), fl=fill(WHITE), al=align("left", "center"))
        merge_write(ws, "H2:J3",
                    "1. Ayşe Kaya — Kalite Müh. (Lider)\n2. Mehmet Yıldız — Montaj Usta\n3. Elif Demir — Proses Müh.\n4. Can Öztürk — Bakım",
                    f=font(9), al=align("left", "top"))
        merge_write(ws, "K2:L3",
                    "1. Üretim Md.\n2. Kalite Md.\n3. Satınalma\n4. Servis / CS",
                    f=font(9), al=align("left", "top"))
    else:
        merge_write(ws, "B2:F3", "", f=font(11, True), al=align("left"))
        merge_write(ws, "H2:J3", "1.\n2.\n3.\n4.", f=font(9), al=align("left", "top"))
        merge_write(ws, "K2:L3", "1.\n2.\n3.\n4.", f=font(9), al=align("left", "top"))

    merge_write(ws, "B4:C4", "Takım lideri / iletişim", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))
    merge_write(ws, "D4:F4",
                "Ayşe Kaya · a.kaya@oztiryakiler.example · Dahili 2140" if filled else "",
                f=font(9), al=align("left"))
    merge_write(ws, "H4:I4", "Bölüm / Hat", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))
    merge_write(ws, "J4:J4",
                "Soğuk Üniteler — Dik Tip Hattı" if filled else "",
                f=font(9), al=align("left"))
    merge_write(ws, "K4:K4", "Başlangıç / süre", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))
    merge_write(ws, "L4:L4",
                "03.02.2026 · 16 hafta" if filled else "",
                f=font(9), al=align("left"))

    merge_write(ws, "B5:F5", "Firma hedefi / bağ", f=font(8, True, MUTED), fl=fill(SOFT), al=align("left"))
    merge_write(ws, "H5:L5",
                "FPY ≥ %96 · Müşteri şikâyeti −%40 · Enerji sınıfı / soğuk muhafaza kalitesinde sıfır kritik red" if filled
                else "Sürekli iyileştirme / KPI ile bağlantı yazın",
                f=font(9, True, NAVY if filled else MUTED), al=align("left"))

    # Title strip
    merge_write(ws, "B6:L6",
                "TOYOTA 8 ADIM  ·  A3 PROBLEM ÇÖZME RAPORU  ·  ÖZTİRYAKİLER",
                f=font(10, True, WHITE), fl=fill(NAVY), al=align("center"))

    # ========== LEFT COLUMN: Steps 1,2,3,5,6 ==========
    # Step 1
    merge_write(ws, "B7:F7", "1. PROBLEMİ NETLEŞTİR", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s1 = (
            "Nedir: GN 2/1 dik tip monoblok buzdolabı (GN 1200 / 650 / 400 NMV ailesi) final testte "
            "kapı contası sızdırmazlık + kabin içi sıcaklık kararlılığı redleri.\n"
            "Ne değildir: Kompresör arızası, elektronik kart, cam kapı modellerinin optik kusurları, "
            "tezgah tipi / slim hat.\n"
            "Problem söylemi: Son 12 haftada dik tip hattında FPY %86’ya düştü; redlerin %62’si "
            "conta sızdırmazlık / sıcaklık sapması. Yeniden iş + geciken sevkiyat müşteri teslimat "
            "performansını ve ihracat kalite imajını zedeliyor."
        )
    else:
        s1 = "Nedir:\nNe değildir:\nProblem söylemi:"
    merge_write(ws, "B8:F12", s1, f=font(8.5), al=align("left", "top"))
    for r in range(8, 13):
        ws.row_dimensions[r].height = 18

    # Step 2
    merge_write(ws, "B13:F13", "2. PROBLEMİ KIR (VERİ)", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s2 = (
            "Kapsam: Büyükçekmece — Dik Tip Hattı, Şubat–Nisan 2026 (n=1.248 ünite).\n"
            "Pareto (final red nedeni): Conta sızdırmazlık %38 · Sıcaklık sapması %24 · "
            "Kabin gövde/kaynak %14 · Monoblok sızıntı %11 · Diğer %13.\n"
            "Odak: Conta + sıcaklık (birlikte %62). En yoğun model: GN 1200 NMV çift kapı.\n"
            "Proses haritası kritik adımlar: Conta kanalı şekillendirme → Conta kesim/ekleme → "
            "Yapıştırma → Kapı montajı → Final sızdırmazlık & 4 saat sıcaklık testi.\n"
            "Trend: FPY haftalık %84–%89 bandında; Cuma vardiyasında red +%9."
        )
    else:
        s2 = "Boyut / n:\nPareto:\nOdak alt-problem:\nProses özeti:"
    merge_write(ws, "B14:F18", s2, f=font(8.5), al=align("left", "top"))
    for r in range(14, 19):
        ws.row_dimensions[r].height = 18

    # Step 3
    merge_write(ws, "B19:F19", "3. HEDEF KOY", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s3 = (
            "1) Dik tip hattı FPY’yi %86’dan %96’ya yükselt (30.06.2026).\n"
            "2) Conta kaynaklı final red oranını %3,9’dan ≤ %1,5’e düşür.\n"
            "3) Final testte sıcaklık sapması redini %2,5’ten ≤ %0,8’e düşür.\n"
            "4) Conta kaynaklı yeniden iş süresini ünite başına 42 dk → ≤ 15 dk.\n"
            "Başarı tanımı: 4 ardışık hafta hedef bandında + müşteri şikâyeti (conta) 0 kritik."
        )
    else:
        s3 = "Fiil + nesne + from → to + tarih:\n1)\n2)\n3)"
    merge_write(ws, "B20:F23", s3, f=font(8.5), al=align("left", "top"))
    for r in range(20, 24):
        ws.row_dimensions[r].height = 17

    # Step 5
    merge_write(ws, "B24:F24", "5. ÖNLEMLERİ GELİŞTİR", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s5 = (
            "Önlem | Etki | Çaba | Öncelik\n"
            "A. Conta kanalı CNC mastar + %100 go/no-go | Yüksek | Orta | 1\n"
            "B. Yapıştırma sıcaklığı PID + alarm (42±2°C) | Yüksek | Orta | 1\n"
            "C. Kapı menteşe tork standardı + dijital anahtar | Orta | Düşük | 2\n"
            "D. Conta tedarikçi lot kabul (sertlik Shore A) | Yüksek | Orta | 2\n"
            "E. Final testte duman/ışık sızdırmazlık jig’i | Orta | Yüksek | 3\n"
            "F. Operatör yeniden eğitim (Cuma vardiyası) | Orta | Düşük | 2"
        )
    else:
        s5 = "Önlem | Etki | Çaba | Öncelik\n1)\n2)\n3)"
    merge_write(ws, "B25:F29", s5, f=font(8), al=align("left", "top"))
    for r in range(25, 30):
        ws.row_dimensions[r].height = 16

    # Step 6
    merge_write(ws, "B30:F30", "6. ÖNLEMİ SEÇ & UYGULA", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s6 = (
            "Seçilen paket: A+B+C+D (kök nedene doğrudan).\n"
            "Plan: Hafta 1–2 mastar imalatı · Hafta 2–3 PID & alarm · Hafta 3 tork SWI · "
            "Hafta 4 tedarikçi lot protokolü · Hafta 5–6 pilot 120 ünite · Hafta 7 yayılım.\n"
            "Sorumlular: Proses (A,B) · Montaj (C) · Kalite/Satınalma (D).\n"
            "Bütçe: ~185.000 TL (mastar, sensör, anahtar, jig revizyonu).\n"
            "Durum: Pilot tamamlandı (Nisan); yayılım Mayıs’ta %100 hatta."
        )
    else:
        s6 = "Seçilen önlem(ler):\nAksiyon özeti / Gantt:\nSorumlu / bütçe:"
    merge_write(ws, "B31:F35", s6, f=font(8.5), al=align("left", "top"))
    for r in range(31, 36):
        ws.row_dimensions[r].height = 16

    # ========== RIGHT COLUMN: Steps 4,7,8 ==========
    merge_write(ws, "H7:L7", "4. KÖK NEDEN ANALİZİ", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s4 = (
            "Balık kılçığı özeti (4M):\n"
            "• Makine: Conta yapıştırma plakası sıcaklığı ±6°C drift (kalibrasyon 6 ay gecikmiş).\n"
            "• Metot: Kapı menteşe torku operatöre bağlı; SWI’de sayısal tork yok.\n"
            "• Malzeme: Conta Shore A 58–72 aralığında lot varyasyonu; kabul limiti tanımsız.\n"
            "• İnsan: Cuma vardiyası yeni operatör oranı yüksek; conta yerleşim eğitimi yok.\n\n"
            "5 Neden (sızdırmazlık red):\n"
            "1) Conta kapı kanalına tam oturmuyor → 2) Kanal derinliği 0,4–0,9 mm sapmalı → "
            "3) Pres kalıp aşınması ölçülmeden devam → 4) Kalıp bakım KM planı yok → "
            "5) KÖK: Preventif kalıp/mastar kontrol standardı tanımlanmamış.\n\n"
            "Doğrulama: Mastarsız 40 ünite vs mastarlı 40 ünite — sızdırmazlık red %7,5 → %1,0."
        )
    else:
        s4 = "4M / balık kılçığı:\n5 Neden:\nKök neden:\nKanıt:"
    merge_write(ws, "H8:L18", s4, f=font(8.5), al=align("left", "top"))

    merge_write(ws, "H19:L19", "7. SÜREÇ & SONUÇLARI İZLE", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s7 = (
            "Metrikler (haftalık):\n"
            "• FPY: %86 → %91 (pilot) → %95,4 (yayılım 4. hafta)\n"
            "• Conta red: %3,9 → %1,6 → %1,2\n"
            "• Sıcaklık red: %2,5 → %1,1 → %0,7\n"
            "• Yeniden iş dk/ünite: 42 → 18\n\n"
            "Kontrol: Yapıştırma sıcaklığı SPC (X̄-R); tork kayıtları MES’e.\n"
            "Snag: GN 650 tek kapıda mastar adaptörü eksik → aksiyon açık (BK-03).\n"
            "Paydaş gözden geçirme: Her Cuma 15 dk stand-up."
        )
    else:
        s7 = "Before / After metrikler:\nKontrol yöntemi:\nSnag / aksiyon:"
    merge_write(ws, "H20:L27", s7, f=font(8.5), al=align("left", "top"))
    for r in range(20, 28):
        ws.row_dimensions[r].height = 16

    merge_write(ws, "H28:L28", "8. STANDARTLAŞTIR & PAYLAŞ", f=font(9, True, WHITE), fl=fill(STEP_BG), al=align("left"))
    if filled:
        s8 = (
            "• SWI-SU-014 Kapı Conta Montajı rev.C (tork 4,5±0,3 Nm + görsel).\n"
            "• Kalıp/mastar kontrol kartı — her vardiya başı go/no-go.\n"
            "• Conta tedarikçi spesifikasyonu: Shore A 62–66; lot başına 5 numune.\n"
            "• Eğitim: 28 montaj operatörü + 6 kalite; yeterlilik matrisi güncellendi.\n"
            "• Yatay yayılım: Tezgah tipi soğutucu kapı contası (Q3 2026 planı).\n"
            "• Kazanç (tahmini): Yeniden iş −1,1 M TL/yıl; sevkiyat gecikmesi −%70.\n"
            "• Kutlama / ders: “Ölçülmeyen mastar = gizli varyasyon.” Sonraki A3: monoblok sızıntı."
        )
    else:
        s8 = "Standart iş / prosedür:\nEğitim:\nYatay yayılım:\nKazanç / dersler:"
    merge_write(ws, "H29:L35", s8, f=font(8.5), al=align("left", "top"))
    for r in range(29, 36):
        ws.row_dimensions[r].height = 16

    # Footer KPIs strip
    merge_write(ws, "B36:L36", "ÖZET KPI ŞERİDİ (tek bakışta)", f=font(9, True, WHITE), fl=fill(ACCENT), al=align("left"))
    kpis = [
        ("B37:C37", "FPY önce", "%86" if filled else ""),
        ("D37:E37", "FPY şimdi", "%95,4" if filled else ""),
        ("F37:H37", "Conta red", "%3,9 → %1,2" if filled else ""),
        ("I37:J37", "Hedef tarih", "30.06.2026" if filled else ""),
        ("K37:L37", "Durum", "Yayılım / kontrol" if filled else ""),
    ]
    for rng, label, val in kpis:
        start = rng.split(":")[0]
        merge_write(ws, rng, f"{label}\n{val}", f=font(9, True, NAVY), fl=fill(LIGHT), al=align("center", "center"))
    ws.row_dimensions[37].height = 32

    merge_write(ws, "B38:L39",
                "Not: Bu A3 yaşayan belgedir. Her adım tamamlandıkça güncellenir. Talimatlar için bkz. 02_8_Adim_Rehberi. "
                "Detay veri: 05_Pareto_Trend · 04_Kok_Neden · 06_Aksiyon_Plani."
                if filled else
                "Boş şablon — talimatlar 02_8_Adim_Rehberi sayfasındadır. Kutulara yalnızca bulgu, veri ve karar yazın.",
                f=font(8, False, MUTED), fl=fill(SOFT), al=align("left", "center"))

    # Lesson / reflection mini box
    merge_write(ws, "B40:F40", "YANSIMA / DERSLER", f=font(8, True, WHITE), fl=fill(NAVY), al=align("left"))
    merge_write(ws, "H40:L40", "ONAYLAR", f=font(8, True, WHITE), fl=fill(NAVY), al=align("left"))
    if filled:
        merge_write(ws, "B41:F42",
                    "1) Preventif mastar kontrolü yoksa proses yeteneği düşer.\n"
                    "2) Tedarikçi spesifikasyonu sayısal olmalı.\n"
                    "3) Vardiya bazlı eğitim açığı Pareto’da görünür.",
                    f=font(8), al=align("left", "top"))
        merge_write(ws, "H41:L42",
                    "Takım lideri: Ayşe Kaya ____  Kalite Md: ________  Üretim Md: ________\n"
                    "Tarih: 22.05.2026",
                    f=font(8), al=align("left", "top"))
    else:
        merge_write(ws, "B41:F42", "1)\n2)\n3)", f=font(8), al=align("left", "top"))
        merge_write(ws, "H41:L42", "Takım lideri: ____  Sponsor: ____  Tarih: ____", f=font(8), al=align("left", "top"))


# =============================================================================
# SHEETS: blank + filled A3
# =============================================================================
ws_blank = wb.create_sheet("03_A3_Sablon_Bos")
build_a3_sheet(ws_blank, filled=False)

ws_fill = wb.create_sheet("03_A3_Oztiryakiler")
build_a3_sheet(ws_fill, filled=True)

# =============================================================================
# SHEET: Is / Is Not
# =============================================================================
ws = wb.create_sheet("04_Is_IsNot")
set_cols(ws, [28, 40, 40, 28])
merge_write(ws, "A1:D1", "IS / IS NOT ANALİZİ — A3-2026-07 Öztiryakiler Dik Tip BD Conta",
            f=font(13, True, WHITE), fl=fill(NAVY), al=align("left"))
for i, h in enumerate(["Açıklama", "IS (Gözlem)", "IS NOT", "Not"], 1):
    c = ws.cell(2, i, h)
    c.font = font(10, True, WHITE)
    c.fill = fill(TEAL)
    c.border = thin
    c.alignment = align("center")

rows = [
    ("Kusur nedir?", "Kapı contası sızdırmazlık kaçağı; kabin sıcaklık sapması (>±1,5°C)", "Kompresör arızası, kart hatası, boya/optik kusur", "Final test istasyonu"),
    ("Hangi proses?", "Conta kanalı → yapıştırma → kapı montaj → final test", "Sac kesim, kaynak, boyahane, monoblok gaz dolum", "Odak montaj sonu"),
    ("Prosesin neresi?", "Conta yerleşimi + menteşe tork + yapıştırma sıcaklığı", "Soğutma devresi kaçak testi (ayrı Pareto)", ""),
    ("Kim etkileniyor?", "Final test, sevkiyat, ihracat müşterileri, servis", "Sadece iç lojistik / depo", "VOC: geciken teslimat"),
    ("Ne zaman?", "Şubat 2026’dan itibaren belirgin artış", "2025 Q3–Q4 stabil dönem", "Kalıp bakım gecikmesiyle örtüşüyor"),
    ("Ne sıklıkla?", "Haftalık ~%3,9 conta red; Cuma +%9", "Tek seferlik / rastgele", "Vardiya paterni var"),
    ("Patern?", "GN 1200 çift kapı yoğun; Cuma vardiyası", "Tüm modeller eşit değil", "Pareto sayfasına bak"),
    ("Maliyet?", "~1,1 M TL/yıl yeniden iş + gecikme cezası riski", "Saha garanti maliyeti henüz ana kalem değil", "Tahmini"),
]
for i, row in enumerate(rows, 3):
    for j, val in enumerate(row, 1):
        c = ws.cell(i, j, val)
        c.font = font(9)
        c.border = thin
        c.alignment = align("left", "top")
        c.fill = fill(SOFT if i % 2 == 0 else WHITE)
    ws.row_dimensions[i].height = 36

merge_write(ws, "A12:D12", "Problem söylemi (IS sütunundan):", f=font(10, True, WHITE), fl=fill(ACCENT), al=align("left"))
merge_write(
    ws, "A13:D15",
    "Öztiryakiler Büyükçekmece dik tip monoblok buzdolabı hattında, GN 2/1 ailesinde (özellikle GN 1200 NMV), "
    "final testte kapı contası sızdırmazlık ve sıcaklık kararlılığı redleri son 12 haftada FPY’yi %86’ya düşürmüştür. "
    "Sorun kompresör/elektronik kaynaklı değildir; conta kanalı, yapıştırma prosesi ve montaj torku ile sınırlıdır.",
    f=font(10), al=align("left", "top"),
)

# =============================================================================
# SHEET: Root cause 5 Whys + Fishbone text
# =============================================================================
ws = wb.create_sheet("04_Kok_Neden")
set_cols(ws, [14, 55, 20, 25])
merge_write(ws, "A1:D1", "KÖK NEDEN — 5 NEDEN & 4M ÖZETİ", f=font(13, True, WHITE), fl=fill(NAVY), al=align("left"))

merge_write(ws, "A3:D3", "5 NEDEN — Conta sızdırmazlık red", f=font(11, True, WHITE), fl=fill(TEAL), al=align("left"))
whys = [
    ("Neden 1", "Final testte kapı kenarından kaçak / sıcaklık sapması oluşuyor.", "Gözlem"),
    ("Neden 2", "Conta kapı kanalına tam oturmuyor; lokal boşluk kalıyor.", "Kesit ölçümü"),
    ("Neden 3", "Conta kanal derinliği 0,4–0,9 mm tolerans dışı.", "CMM / mastar"),
    ("Neden 4", "Pres kalıp aşınması ölçülmeden üretime devam edilmiş.", "Bakım kaydı"),
    ("Neden 5 / KÖK", "Preventif kalıp & mastar kontrol standardı ve go/no-go disiplini tanımlı değil.", "Sistemik"),
]
ws.cell(4, 1, "Adım").font = font(9, True, WHITE)
ws.cell(4, 2, "İfade").font = font(9, True, WHITE)
ws.cell(4, 3, "Kanıt tipi").font = font(9, True, WHITE)
ws.cell(4, 4, "").font = font(9, True, WHITE)
for col in range(1, 4):
    ws.cell(4, col).fill = fill(STEP_BG)
    ws.cell(4, col).border = thin
for i, (a, b, c) in enumerate(whys, 5):
    ws.cell(i, 1, a).font = font(9, True, ACCENT if "KÖK" in a else DARK)
    ws.cell(i, 2, b).font = font(9)
    ws.cell(i, 3, c).font = font(9)
    for col in range(1, 4):
        ws.cell(i, col).border = thin
        ws.cell(i, col).alignment = align("left", "center")
        ws.cell(i, col).fill = fill(SOFT if "KÖK" in a else WHITE)
    ws.row_dimensions[i].height = 28

merge_write(ws, "A11:D11", "4M BALIK KILÇIĞI — Katkılar", f=font(11, True, WHITE), fl=fill(TEAL), al=align("left"))
fish = [
    ("Makine", "Yapıştırma plakası sıcaklık drift ±6°C; kalibrasyon gecikmiş; kalıp aşınması"),
    ("Metot", "Menteşe torku SWI’de sayısal değil; mastar kontrolü vardiya başında yok"),
    ("Malzeme", "Conta Shore A 58–72 lot varyasyonu; kabul limiti tanımsız"),
    ("İnsan", "Cuma vardiyası yeni operatör oranı yüksek; conta yerleşim OJT eksik"),
]
for i, (m, t) in enumerate(fish, 12):
    ws.cell(i, 1, m).font = font(10, True, NAVY)
    ws.cell(i, 1).fill = fill(SOFT)
    merge_write(ws, f"B{i}:D{i}", t, f=font(9), al=align("left"))
    ws.row_dimensions[i].height = 24

merge_write(ws, "A17:D17", "Doğrulama deneyi", f=font(11, True, WHITE), fl=fill(ACCENT), al=align("left"))
merge_write(
    ws, "A18:D20",
    "Aynı model (GN 1200 NMV), aynı vardiya: Mastarsız 40 ünite → sızdırmazlık red %7,5. "
    "Mastar + sıcaklık alarmı + tork anahtarı ile 40 ünite → red %1,0. "
    "Kök neden hipotezi doğrulandı; önlem paketi A+B+C seçildi.",
    f=font(10), al=align("left", "top"),
)

# =============================================================================
# SHEET: Pareto + Trend data + charts
# =============================================================================
ws = wb.create_sheet("05_Pareto_Trend")
set_cols(ws, [28, 12, 12, 14, 14, 14, 14, 14])
merge_write(ws, "A1:H1", "VERİ — Final Red Pareto & FPY Trend (Öztiryakiler Dik Tip Hattı)",
            f=font(13, True, WHITE), fl=fill(NAVY), al=align("left"))

ws["A3"] = "Red nedeni"
ws["B3"] = "Adet"
ws["C3"] = "Pay %"
ws["D3"] = "Kümülatif %"
for col in range(1, 5):
    ws.cell(3, col).font = font(9, True, WHITE)
    ws.cell(3, col).fill = fill(TEAL)
    ws.cell(3, col).border = thin

pareto = [
    ("Conta sızdırmazlık", 68, 38, 38),
    ("Sıcaklık sapması", 43, 24, 62),
    ("Kabin gövde/kaynak", 25, 14, 76),
    ("Monoblok sızıntı", 20, 11, 87),
    ("Diğer", 23, 13, 100),
]
for i, (name, n, p, c) in enumerate(pareto, 4):
    ws.cell(i, 1, name).border = thin
    ws.cell(i, 2, n).border = thin
    ws.cell(i, 3, p / 100).border = thin
    ws.cell(i, 3).number_format = "0%"
    ws.cell(i, 4, c / 100).border = thin
    ws.cell(i, 4).number_format = "0%"

chart1 = BarChart()
chart1.type = "col"
chart1.title = "Final red nedenleri (adet)"
chart1.y_axis.title = "Adet"
chart1.x_axis.title = "Neden"
data = Reference(ws, min_col=2, min_row=3, max_row=8)
cats = Reference(ws, min_col=1, min_row=4, max_row=8)
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
chart1.shape = 4
chart1.width = 15
chart1.height = 8
ws.add_chart(chart1, "A10")

# FPY trend
ws["F3"] = "Hafta"
ws["G3"] = "FPY %"
ws["H3"] = "Conta red %"
for col in range(6, 9):
    ws.cell(3, col).font = font(9, True, WHITE)
    ws.cell(3, col).fill = fill(TEAL)
    ws.cell(3, col).border = thin

trend = [
    ("W06", 0.86, 0.041),
    ("W07", 0.85, 0.043),
    ("W08", 0.87, 0.038),
    ("W09", 0.86, 0.039),
    ("W10", 0.88, 0.035),  # mastar pilot start
    ("W11", 0.91, 0.022),
    ("W12", 0.93, 0.018),
    ("W13", 0.94, 0.015),
    ("W14", 0.95, 0.013),
    ("W15", 0.954, 0.012),
]
for i, (w, fpy, cr) in enumerate(trend, 4):
    ws.cell(i, 6, w).border = thin
    ws.cell(i, 7, fpy).border = thin
    ws.cell(i, 7).number_format = "0.0%"
    ws.cell(i, 8, cr).border = thin
    ws.cell(i, 8).number_format = "0.0%"

chart2 = LineChart()
chart2.title = "FPY ve conta red trendi"
chart2.y_axis.title = "Oran"
chart2.x_axis.title = "Hafta"
data2 = Reference(ws, min_col=7, min_row=3, max_col=8, max_row=13)
cats2 = Reference(ws, min_col=6, min_row=4, max_row=13)
chart2.add_data(data2, titles_from_data=True)
chart2.set_categories(cats2)
chart2.width = 15
chart2.height = 8
ws.add_chart(chart2, "F10")

merge_write(
    ws, "A20:H22",
    "Kaynak: Örnek / eğitim verisi — Öztiryakiler dik tip monoblok buzdolabı hattı senaryosu. "
    "W10 itibarıyla mastar + PID alarm + tork standardı pilotu başlamıştır. "
    "Hedef FPY %96; W15’te %95,4 ile hedef bandına girilmiştir.",
    f=font(9, False, MUTED), fl=fill(SOFT), al=align("left", "top"),
)

# =============================================================================
# SHEET: Action plan
# =============================================================================
ws = wb.create_sheet("06_Aksiyon_Plani")
set_cols(ws, [6, 42, 16, 14, 14, 14, 18])
merge_write(ws, "A1:G1", "AKSİYON PLANI — A3-2026-07", f=font(13, True, WHITE), fl=fill(NAVY), al=align("left"))
headers = ["#", "Aksiyon", "Sorumlu", "Başlangıç", "Bitiş", "Durum", "Kanıt / çıktı"]
for i, h in enumerate(headers, 1):
    c = ws.cell(2, i, h)
    c.font = font(9, True, WHITE)
    c.fill = fill(TEAL)
    c.border = thin
    c.alignment = align("center")

actions = [
    (1, "Conta kanalı CNC mastar imalatı + go/no-go kartı", "Elif Demir", "03.02.26", "21.02.26", "Tamam", "Mastar M-SU-07"),
    (2, "Yapıştırma plakası PID + alarm (42±2°C) kurulum", "Can Öztürk", "10.02.26", "28.02.26", "Tamam", "Kalibrasyon raporu"),
    (3, "SWI-SU-014 rev.C — tork 4,5±0,3 Nm", "Ayşe Kaya", "17.02.26", "07.03.26", "Tamam", "SWI rev.C"),
    (4, "Dijital tork anahtarı temini (6 adet)", "Satınalma", "17.02.26", "14.03.26", "Tamam", "Kabul formu"),
    (5, "Conta Shore A 62–66 tedarikçi spesifikasyonu", "Kalite / Satınalma", "01.03.26", "28.03.26", "Tamam", "Spec SP-CT-12"),
    (6, "Pilot 120 ünite (GN 1200) + ölçüm", "Mehmet Yıldız", "24.03.26", "18.04.26", "Tamam", "Pilot raporu"),
    (7, "Tüm dik tip hatta yayılım", "Üretim", "21.04.26", "16.05.26", "Tamam", "Yayılım checklist"),
    (8, "GN 650 mastar adaptörü", "Elif Demir", "12.05.26", "30.05.26", "Açık", "BK-03"),
    (9, "Operatör yeterlilik eğitimi (28 kişi)", "İK / Kalite", "01.04.26", "30.04.26", "Tamam", "Yeterlilik matrisi"),
    (10, "Tezgah tipi yatay yayılım planı (Q3)", "Kalite Md.", "01.06.26", "30.09.26", "Planlı", "A3-2026-12 taslak"),
]
status_fill = {
    "Tamam": OK_GREEN,
    "Açık": WARN,
    "Planlı": TEAL,
}
for i, row in enumerate(actions, 3):
    for j, val in enumerate(row, 1):
        c = ws.cell(i, j, val)
        c.font = font(9, True if j == 6 else False, WHITE if j == 6 else DARK)
        c.border = thin
        c.alignment = align("center" if j != 2 else "left", "center")
        if j == 6:
            c.fill = fill(status_fill.get(val, MUTED))
        else:
            c.fill = fill(SOFT if i % 2 == 0 else WHITE)
    ws.row_dimensions[i].height = 22

# =============================================================================
# SHEET: Goal writing helper (TR)
# =============================================================================
ws = wb.create_sheet("07_Hedef_Yazimi")
set_cols(ws, [18, 28, 50])
merge_write(ws, "A1:C1", "NET HEDEF YAZMA REHBERİ", f=font(13, True, WHITE), fl=fill(NAVY), al=align("left"))
ws["A3"] = "Sıra"
ws["B3"] = "Öğe"
ws["C3"] = "Öztiryakiler örneği"
for col in range(1, 4):
    ws.cell(3, col).font = font(9, True, WHITE)
    ws.cell(3, col).fill = fill(TEAL)
    ws.cell(3, col).border = thin
goal_rows = [
    ("1", "Fiil", "Yükselt / Düşür / Azalt"),
    ("2", "Nesne", "Dik tip hattı FPY"),
    ("3", "Mevcut durumdan", "%86’dan"),
    ("4", "Hedef duruma", "%96’ya"),
    ("5", "Tarih", "30.06.2026’ya kadar"),
]
for i, row in enumerate(goal_rows, 4):
    for j, val in enumerate(row, 1):
        c = ws.cell(i, j, val)
        c.font = font(10)
        c.border = thin
merge_write(
    ws, "A10:C12",
    'Tam cümle: "Dik tip monoblok buzdolabı hattında FPY’yi %86’dan %96’ya yükselt, 30.06.2026’ya kadar."',
    f=font(11, True, NAVY), fl=fill(LIGHT), al=align("left", "center"),
)

# =============================================================================
# SHEET: Index
# =============================================================================
ws = wb.create_sheet("00_Icindekiler", 0)
set_cols(ws, [8, 32, 55])
merge_write(ws, "A1:C1", "Öztiryakiler A3 Paketi — Toyota 8 Adım (İyileştirilmiş Format)",
            f=font(16, True, WHITE), fl=fill(NAVY), al=align("left"))
merge_write(ws, "A2:C2", "Endüstriyel mutfak / Soğuk üniteler — GN 2/1 dik tip monoblok buzdolabı örneği",
            f=font(10, False, WHITE), fl=fill(TEAL), al=align("left"))

index = [
    ("00_Icindekiler", "Bu sayfa"),
    ("01_Analiz", "Orijinal ODS analizi ve iyileştirme kararları"),
    ("02_8_Adim_Rehberi", "8 adım kısa rehber (A3’e yazılmaz)"),
    ("03_A3_Sablon_Bos", "Boş A3 şablonu — yeni projeler için"),
    ("03_A3_Oztiryakiler", "Dolu örnek A3 — conta sızdırmazlık FPY"),
    ("04_Is_IsNot", "Is / Is Not analizi (dolu)"),
    ("04_Kok_Neden", "5 Neden + 4M balık kılçığı"),
    ("05_Pareto_Trend", "Pareto ve FPY trend grafikleri"),
    ("06_Aksiyon_Plani", "Uygulama aksiyon planı"),
    ("07_Hedef_Yazimi", "Hedef cümlesi yazma rehberi"),
]
ws.cell(4, 1, "#").font = font(9, True, WHITE)
ws.cell(4, 2, "Sayfa").font = font(9, True, WHITE)
ws.cell(4, 3, "İçerik").font = font(9, True, WHITE)
for col in range(1, 4):
    ws.cell(4, col).fill = fill(STEP_BG)
    ws.cell(4, col).border = thin
for i, (name, desc) in enumerate(index, 5):
    ws.cell(i, 1, i - 4).border = thin
    ws.cell(i, 2, name).border = thin
    ws.cell(i, 2).font = font(10, True, NAVY)
    ws.cell(i, 3, desc).border = thin
    for col in range(1, 4):
        ws.cell(i, col).fill = fill(SOFT if i % 2 == 0 else WHITE)
        ws.cell(i, col).alignment = align("left")

merge_write(
    ws, "A17:C20",
    "Kullanım: Yeni A3 için 03_A3_Sablon_Bos sayfasını kopyalayın. "
    "Örnek akışı görmek için 03_A3_Oztiryakiler + 04–06 sayfalarına bakın. "
    "A3’ü yazdırırken sayfa yönü yatay (landscape) ve kağıt A3 seçilmelidir. "
    "Orijinal dosyadaki talimat kirliliği bilerek ayrılmıştır — sahada tek sayfa okunabilir kalsın.",
    f=font(10), fl=fill(LIGHT), al=align("left", "top"),
)

out = "/workspace/a3-raporlama/Oztiryakiler_A3_Toyota_8_Adim.xlsx"
wb.save(out)
print("Wrote", out)
