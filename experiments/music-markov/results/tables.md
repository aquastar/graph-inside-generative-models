| representation | method | order | accuracy % (mean ± sd) | macro F1 % (mean ± sd) |
|---|---|---|---|---|
| pitch class (tonic relative) | table features + LR | 1 | 70.2 ± 2.7 | 68.9 ± 4.6 |
| pitch class (tonic relative) | table features + LR | 2 | 78.2 ± 2.4 | 78.5 ± 4.1 |
| pitch class (tonic relative) | table features + LR | 1+2 | 78.4 ± 1.3 | 78.8 ± 3.8 |
| pitch class (tonic relative) | likelihood classifier | 0 | 27.2 ± 1.4 | 22.7 ± 1.9 |
| pitch class (tonic relative) | likelihood classifier | 1 | 62.6 ± 0.8 | 60.7 ± 1.1 |
| pitch class (tonic relative) | likelihood classifier | 2 | 71.8 ± 1.6 | 69.7 ± 2.2 |
| pitch class (tonic relative) | likelihood classifier | 3 | 72.3 ± 3.3 | 70.3 ± 3.5 |
| pitch class (tonic relative) | likelihood classifier | variable (PPM C, max 5) | 73.3 ± 3.7 | 71.8 ± 3.7 |
| interval | table features + LR | 1 | 74.8 ± 2.2 | 76.1 ± 2.1 |
| interval | table features + LR | 2 | 81.4 ± 2.7 | 82.0 ± 2.5 |
| interval | table features + LR | 1+2 | 82.1 ± 2.9 | 83.4 ± 2.5 |
| interval | likelihood classifier | 0 | 59.2 ± 3.2 | 57.2 ± 3.2 |
| interval | likelihood classifier | 1 | 74.8 ± 2.7 | 73.0 ± 2.7 |
| interval | likelihood classifier | 2 | 76.2 ± 5.0 | 74.5 ± 5.2 |
| interval | likelihood classifier | 3 | 72.9 ± 2.8 | 70.1 ± 2.5 |
| interval | likelihood classifier | variable (PPM C, max 5) | 76.0 ± 3.7 | 74.8 ± 3.4 |
| pitch class + duration | table features + LR | 1 | 86.8 ± 0.6 | 86.4 ± 1.8 |
| pitch class + duration | table features + LR | 2 | 86.2 ± 1.5 | 83.2 ± 2.1 |
| pitch class + duration | table features + LR | 1+2 | 87.3 ± 1.7 | 83.8 ± 5.1 |
| pitch class + duration | likelihood classifier | 0 | 73.6 ± 1.9 | 70.0 ± 3.1 |
| pitch class + duration | likelihood classifier | 1 | 86.9 ± 0.6 | 85.4 ± 1.2 |
| pitch class + duration | likelihood classifier | 2 | 87.9 ± 1.8 | 86.4 ± 1.9 |
| pitch class + duration | likelihood classifier | 3 | 85.2 ± 0.9 | 83.6 ± 1.5 |
| pitch class + duration | likelihood classifier | variable (PPM C, max 5) | 88.7 ± 1.8 | 87.1 ± 2.1 |

CONFUSED

| method | top confused pairs (pieces misassigned in either direction, pooled over folds) |
|---|---|
| pc, LR order 1 | Bach and Palestrina (73), Essen folk and Ryan's Mammoth (46), Bach and Essen folk (46) |
| pc, LR order 2 | Bach and Essen folk (61), Bach and Palestrina (42), Essen folk and Ryan's Mammoth (37) |
| pc, LL variable (PPM C, max 5) | Essen folk and Ryan's Mammoth (44), Bach and Palestrina (43), Palestrina and Trecento (30) |
| pcdur, LL variable (PPM C, max 5) | Essen folk and Ryan's Mammoth (22), Bach and Essen folk (17), Palestrina and Essen folk (16) |
| int, LR order 2 | Bach and Essen folk (46), Bach and Palestrina (34), Essen folk and Ryan's Mammoth (29) |

GEN

| order | sampler | style acc, order 1 judge % | style acc, order 1+2 judge % | longest copied span (notes) | 4 grams seen in training % | distinct 4 grams % | pairwise edit distance |
|---|---|---|---|---|---|---|---|
| real held out | n/a | 55.4 ± 2.0 | 48.2 ± 3.0 | 10.9 | 91.0 | 57.3 | 0.75 |
| 1 | ancestral | 64.7 ± 2.0 | 49.3 ± 3.0 | 7.6 | 80.2 | 68.3 | 0.75 |
| 1 | temp 0.7 | 70.0 ± 4.6 | 49.2 ± 2.5 | 8.2 | 89.0 | 52.4 | 0.72 |
| 1 | temp 1.3 | 56.0 ± 2.7 | 43.8 ± 3.6 | 7.0 | 71.5 | 78.3 | 0.77 |
| 1 | top k 3 | 59.3 ± 3.1 | 35.0 ± 2.2 | 8.8 | 95.9 | 19.4 | 0.67 |
| 1 | max copy L=6 | 63.5 ± 3.6 | 45.3 ± 3.3 | 6.0 | 78.7 | 70.7 | 0.75 |
| 2 | ancestral | 62.0 ± 1.9 | 66.5 ± 1.6 | 8.3 | 90.2 | 62.8 | 0.75 |
| 2 | temp 0.7 | 65.8 ± 2.2 | 66.2 ± 1.4 | 9.4 | 96.5 | 45.1 | 0.71 |
| 2 | temp 1.3 | 56.8 ± 1.9 | 60.7 ± 3.3 | 7.7 | 80.5 | 74.7 | 0.77 |
| 2 | top k 3 | 66.3 ± 3.3 | 60.3 ± 2.4 | 9.7 | 99.0 | 25.6 | 0.70 |
| 2 | max copy L=6 | 59.2 ± 2.2 | 62.2 ± 2.1 | 6.0 | 87.3 | 69.4 | 0.76 |
| 3 | ancestral | 59.8 ± 3.9 | 60.7 ± 3.7 | 9.0 | 92.5 | 63.5 | 0.76 |
| 3 | temp 0.7 | 68.7 ± 2.0 | 63.7 ± 4.7 | 10.0 | 98.9 | 46.2 | 0.72 |
| 3 | temp 1.3 | 49.5 ± 4.4 | 58.7 ± 2.5 | 8.1 | 80.4 | 77.1 | 0.78 |
| 3 | top k 3 | 63.7 ± 3.1 | 63.7 ± 2.2 | 10.3 | 99.9 | 32.5 | 0.71 |
| 3 | max copy L=6 | 53.0 ± 7.5 | 60.8 ± 6.5 | 6.0 | 88.1 | 72.9 | 0.77 |
| variable (PPM C) | ancestral | 63.0 ± 5.1 | 67.5 ± 2.2 | 12.1 | 99.4 | 57.7 | 0.75 |
| variable (PPM C) | temp 0.7 | 62.5 ± 2.8 | 66.0 ± 2.1 | 13.1 | 99.9 | 48.7 | 0.72 |
| variable (PPM C) | temp 1.3 | 55.8 ± 3.3 | 62.5 ± 1.5 | 10.8 | 98.1 | 63.8 | 0.76 |
| variable (PPM C) | top k 3 | 66.2 ± 6.0 | 65.5 ± 2.3 | 12.5 | 99.9 | 47.2 | 0.72 |
| variable (PPM C) | max copy L=6 | 56.7 ± 4.3 | 61.8 ± 3.4 | 6.0 | 96.2 | 69.4 | 0.77 |

BYSTYLE

| order | sampler | Bach | Palestrina | Monteverdi | Trecento | Essen folk | Ryan's Mammoth |
|---|---|---|---|---|---|---|---|
| real held out | n/a | 61 | 58 | 36 | 41 | 65 | 71 |
| 1 | ancestral | 54 | 66 | 42 | 63 | 82 | 81 |
| 1 | max copy L=6 | 47 | 63 | 41 | 64 | 74 | 92 |
| 2 | ancestral | 56 | 63 | 37 | 64 | 67 | 85 |
| 2 | max copy L=6 | 45 | 66 | 33 | 61 | 64 | 86 |
| 3 | ancestral | 41 | 64 | 29 | 66 | 73 | 86 |
| 3 | max copy L=6 | 33 | 60 | 25 | 57 | 63 | 80 |
| var | ancestral | 59 | 65 | 34 | 55 | 76 | 89 |
| var | max copy L=6 | 42 | 49 | 32 | 59 | 76 | 82 |

SENS

| Lidstone alpha | order 1 | order 2 | order 3 |
|---|---|---|---|
| 0.01 | 62.7 | 71.7 | 70.2 |
| 0.1 | 62.6 | 71.8 | 72.3 |
| 1.0 | 62.7 | 73.2 | 74.0 |
