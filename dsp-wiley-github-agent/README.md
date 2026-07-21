# Digital Audio Signal Processing (Zölzer / Wiley) GitHub Agent

Separate agent for **Udo Zölzer, *Digital Audio Signal Processing*, 2nd Edition** (Wiley, 2008).

**Source PDF:**  
https://shop.pearlacoustics.com/wp-content/uploads/woocommerce_uploads/2023/01/Wiley-Digital-Audio-Signal-Processing-2nd-Edition-82cqs3.pdf

## Contents

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `dsp_kb/` | Queryable knowledge (9 chapters, concepts, recipes) |
| `knowledge/Wiley_Digital_Audio_Signal_Processing_2nd_Edition.pdf` | Local PDF (~7 MB, 334 pages) |
| `knowledge/manual_extract.txt` | Full text extract (~528 KB) |

## Chapters

1. Introduction  
2. Quantization  
3. AD/DA Conversion  
4. Audio Processing Systems  
5. Equalizers  
6. Room Simulation  
7. Dynamic Range Control  
8. Sampling Rate Conversion  
9. Audio Coding  

## CLI

```bash
cd dsp-wiley-github-agent
python -m dsp_kb info
python -m dsp_kb list-chapters
python -m dsp_kb chapter 5
python -m dsp_kb define dither
python -m dsp_kb recipe design_eq
python -m dsp_kb search "Schroeder"
```

## Notes

- Academic textbook; requires DSP background.
- Companion demos: http://ant.hsu-hh.de/dasp/ · DAFX: http://www.dafx.de  
- © John Wiley & Sons / author rights apply to the book. Agent scaffolding is for local study only—do not republish the PDF.
