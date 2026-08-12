---
chinese: 时间计算 (shíjiān jìsuàn)
prerequisites:
  - "[[Four Operations (Vocab)]]"
leads_to:
  - "[[Average Speed (Vocab)]]"
tags:
  - subject/mathematics
  - domain/number
  - level/IGCSE
  - curriculum/Cambridge-0580
  - syllabus/0580-E1-15
  - type/vocabulary
  - misconception/decimal-time
---

# Time Calculations 时间计算

## Definition

Time arithmetic mixes two number bases — **decimal for hours and seconds**, **base-60 for minutes and seconds**, **base-12 or base-24 for clock hours**. The classic exam mistake: treating time as if it were decimal. **$2.5$ hours = $2$ h $30$ min, not $2$ h $50$ min.**

The four key skills:

1. **Reading 12-hour vs 24-hour clocks.** $14:30$ (24-h) = $2:30$ pm (12-h).
2. **Adding and subtracting times** with carry-over at $60$ minutes / $60$ seconds.
3. **Converting decimal hours to hours-and-minutes** (and vice versa).
4. **Time-zone arithmetic** with positive/negative offsets from UTC.

### 中文锚点

**时间计算 (shíjiān jìsuàn)** = 时间相关的运算。注意：

- **时分秒进制是 60，不是 10**。
- $2.5$ 小时 = $2$ 时 $30$ 分（即半小时是 $0.5$ 而非 $0.50$ 分钟）。
- $14:30$ = 下午 $2:30$。

时区计算：UTC ± 偏移。中国标准时间 = UTC+8。纽约 (东部时间) = UTC−5（夏令时 UTC−4）。

---

## Key Vocabulary

| English | 中文 | Notes |
|---------|------|-------|
| 12-hour clock | 12 小时制 | with am / pm |
| 24-hour clock | 24 小时制 | $0:00$ to $23:59$; midnight is $00:00$ |
| am | 上午 (shàngwǔ) | from midnight to noon (latin "ante meridiem") |
| pm | 下午 (xiàwǔ) / 晚上 | from noon to midnight ("post meridiem") |
| midnight | 午夜 (wǔyè) | $00:00$ in 24-h |
| noon / midday | 正午 (zhèngwǔ) / 中午 | $12:00$ in 24-h |
| time zone | 时区 (shíqū) | UTC ± offset |
| UTC | 协调世界时 (xiétiáo shìjièshí) | global reference time |

---

## Conversion Rules

### Decimal hours ↔ hours and minutes

The trap: $0.5$ hour $= 30$ minutes, *not* $50$ minutes.

| Decimal | Hours and minutes | Why |
|---|---|---|
| $0.25$ h | $15$ min | $0.25 \times 60 = 15$ |
| $0.5$ h | $30$ min | $0.5 \times 60 = 30$ |
| $0.75$ h | $45$ min | $0.75 \times 60 = 45$ |
| $1.4$ h | $1$ h $24$ min | $0.4 \times 60 = 24$ |
| $2.6$ h | $2$ h $36$ min | $0.6 \times 60 = 36$ |

**Conversion rule:** to go decimal → minutes, *multiply the fractional part by 60*. To go minutes → decimal, *divide minutes by 60*.

> [!warning] $2.5$ hours is not $2$ hours $50$ minutes
> The minutes after the decimal point are *60ths of an hour*, not 100ths. $2.5 \text{ h} = 2 \text{ h} + 0.5 \text{ h} = 2 \text{ h} + 30 \text{ min}$. The most common 0580 calculation slip is treating the decimal point as if it separated hours from minutes directly. Always run the $\times 60$ conversion explicitly.

### 12-hour ↔ 24-hour clocks

| 12-hour | 24-hour |
|---|---|
| $12:00$ am (midnight) | $00:00$ |
| $1:00$ am | $01:00$ |
| $11:59$ am | $11:59$ |
| $12:00$ pm (noon) | $12:00$ |
| $1:00$ pm | $13:00$ |
| $11:59$ pm | $23:59$ |

**Rule:** for pm times other than 12, add $12$ to the hour. For am times, the 24-hour reading is the same (except midnight, which is $00:00$, not $24:00$).

---

## Worked Examples

### Example 1 — adding times

> A train leaves at $09:48$ and the journey takes $2$ hours $35$ minutes. When does it arrive?

Add hours: $09 + 2 = 11$. Add minutes: $48 + 35 = 83$. Carry: $83 = 60 + 23$, so $11$ becomes $12$, leaving $23$ min.

**Arrival:** $12:23$.

### Example 2 — subtracting times (find duration)

> A flight departs at $14:25$ and arrives at $18:10$. How long is the flight?

Direct subtraction: $18:10 - 14:25$. Minutes can't go: $10 - 25$ would be negative. Borrow $60$ from the hours: $18:10$ becomes $17:70$. Now $70 - 25 = 45$ min, $17 - 14 = 3$ h.

**Duration:** $3$ h $45$ min.

### Example 3 — time zones

> A flight leaves Singapore (UTC+8) at $11:00$ on Monday and lands in London (UTC+0) after $13$ hours. What is the local arrival time in London?

Two approaches.

**Approach 1 — convert all times to UTC.**
- Departure: $11:00$ Singapore = $11:00 - 8 = 03:00$ UTC.
- Arrival in UTC: $03:00 + 13:00 = 16:00$ UTC.
- London local time: $16:00$ UTC + $0 = 16:00$ Monday.

**Approach 2 — direct.** Singapore is $8$ hours *ahead* of London. Departure local: 11:00. Add 13 h flight time: 11:00 + 13:00 = 00:00 next day Singapore time = 24:00 = midnight Monday/Tuesday in Singapore. Convert to London: subtract 8 h → 16:00 Monday in London.

**Answer:** $16:00$ Monday in London.

> [!tip] Two different things happen when you cross time zones
> 1. *Real* time passes during the flight (the "$+13$ hours" of clock time elapsed).
> 2. *Local* clocks read differently (the "subtract 8 h" zone offset).
>
> When the problem asks for *local* arrival time, both effects apply. The cleanest method is to convert everything to UTC, do the addition there, then convert to the destination zone. Travelers who skip the UTC step often double-count or sign-flip.

---

## Common Mistakes

1. **Treating $0.5$ hours as $50$ minutes.** It's $30$. Always $\times 60$.
2. **Forgetting to borrow $60$ when subtracting.** $10:15 - 8:40$: borrow gives $9:75 - 8:40 = 1:35$, *not* the bizarre $2:25$ you'd get without borrowing properly.
3. **24-hour clock arithmetic at midnight.** $23:50 + 0:20 = 24:10$ technically, but should be reported as $00:10$ (with the date advancing).
4. **Time zone sign errors.** Singapore is UTC**+8** (ahead of UTC), New York is UTC**−5** (behind). To go from local to UTC: *subtract* the offset. To go from UTC to local: *add* the offset.

---

## Exam Notes

### Cambridge 0580

**Syllabus ref:** E1.15 (Time) — calculate times in terms of the 24-hour and 12-hour clock; read clocks and timetables. Standard exam patterns:

- "A bus leaves at $07:42$ and arrives at $09:15$. Find the journey time in hours and minutes."
- "A film starts at $7:35$ pm and lasts $2$ hours $50$ minutes. At what time does it end?" (Cross midnight check.)
- "A flight departs Hong Kong (UTC+8) at $23:30$ on $15$ March and arrives in San Francisco (UTC−7) after $13$ hours. What is the local arrival time and date?"

---

## Connections

- **Sibling:** [[Average Speed (Vocab)]] — speed × time = distance, with proper unit-time arithmetic
- **Application:** *travel and logistics* — flight schedules, train timetables, all-night-vs-day-trip calculations
- **Forward:** *physics* — relativity adds further time-zone-like complications when speeds approach $c$ (different observers measure different elapsed times)

---

## LaTeX Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $14:30$ | `14{:}30` | use `{:}` to avoid colons being parsed as set-builder separator |
| UTC$\pm n$ | `\text{UTC}\pm n` | time-zone offset |
